import requests
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from fastapi.responses import HTMLResponse
from jinja2 import Environment, FileSystemLoader
from app.questions import questions
from app.settings import settings

model = OllamaLLM(model="llama3")
template = """
You are a helpful assistant for building resumes. You will ask the user a series of questions to gather all the necessary information for creating a professional resume.

Here is the conversation history: {context}

Question: {question}

Answer:
"""
prompt = ChatPromptTemplate.from_template(template)
chain = LLMChain(llm=model, prompt=prompt)

user_data = {}
current_question_index = 0
env = Environment(loader=FileSystemLoader('app/templates'))

def get_next_question():
    global current_question_index
    if current_question_index < len(questions):
        return questions[current_question_index]
    return None

async def handle_resume_bot(user_input):
    global current_question_index
    response = chain.invoke({"context": user_input.context, "question": user_input.question})
    if 'output' in response:
        user_data[questions[current_question_index].key] = user_input.question
        current_question_index += 1
        next_question = get_next_question()
        if next_question:
            return {"output": response['output'], "next_question": next_question.question}
        else:
            return {"output": response['output'], "next_question": "All questions completed. Thank you!"}
    else:
        raise HTTPException(status_code=500, detail="Invalid response format from the model")

def get_responses():
    return {"responses": user_data}

def generate_resume():
    template = env.get_template('resume_template.html')
    resume_html = template.render(user_data)
    return HTMLResponse(content=resume_html)

def call_groq_api(endpoint, data):
    headers = {
        'Authorization': f'Bearer {settings.GROQ_API_KEY}',
        'Content-Type': 'application/json'
    }
    response = requests.post(endpoint, json=data, headers=headers)
    response.raise_for_status()
    return response.json()
