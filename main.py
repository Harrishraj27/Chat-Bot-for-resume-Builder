from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from typing import List, Dict

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

# Endpoint to handle user input and generate a response
@app.post("/resume_bot", response_model=BotResponse)
async def resume_bot(user_input: UserInput):
    try:
        response = chain.invoke({"context": user_input.context, "question": user_input.question})
        if 'output' in response:
            return BotResponse(output=response['output'])
        else:
            raise HTTPException(status_code=500, detail="Invalid response format from the model")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
