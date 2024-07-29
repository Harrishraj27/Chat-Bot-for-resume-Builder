from fastapi import FastAPI, HTTPException, Depends
from pydantic import BaseModel
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from typing import List, Dict
from questions import questions, Question
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader

# Initialize the model and prompt template
model = OllamaLLM(model="llama3")
template = """
You are a helpful assistant for building resumes. You will ask the user a series of questions to gather all the necessary information for creating a professional resume.

Here is the conversation history: {context}

Question: {question}

Answer:
"""
prompt = ChatPromptTemplate.from_template(template)
chain = LLMChain(llm=model, prompt=prompt)

# Define the FastAPI app
app = FastAPI()

# Define request and response models
class UserInput(BaseModel):
    context: str
    question: str

class BotResponse(BaseModel):
    output: str
    next_question: str

class UserResponse(BaseModel):
    responses: Dict[str, str]

user_data: Dict[str, str] = {}
current_question_index: int = 0

# Jinja2 environment setup
env = Environment(loader=FileSystemLoader('templates'))

# Function to get the next question
def get_next_question():
    global current_question_index
    if current_question_index < len(questions):
        return questions[current_question_index]
    return None

# Endpoint to handle user input and generate a response
@app.post("/resume_bot", response_model=BotResponse)
async def resume_bot(user_input: UserInput):
    global current_question_index
    try:
        response = chain.invoke({"context": user_input.context, "question": user_input.question})
        if 'output' in response:
            user_data[questions[current_question_index].key] = user_input.question
            current_question_index += 1
            next_question = get_next_question()
            if next_question:
                return BotResponse(output=response['output'], next_question=next_question.question)
            else:
                return BotResponse(output=response['output'], next_question="All questions completed. Thank you!")
        else:
            raise HTTPException(status_code=500, detail="Invalid response format from the model")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint to get all user responses
@app.get("/responses", response_model=UserResponse)
async def get_responses():
    return UserResponse(responses=user_data)

# Endpoint to generate formatted resume
@app.get("/generate_resume", response_class=HTMLResponse)
async def generate_resume():
    template = env.get_template('resume_template.html')
    resume_html = template.render(user_data)
    return HTMLResponse(content=resume_html)

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
