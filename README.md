# Resume Builder ChatBot

This is a FastAPI-based chatbot that helps users build professional resumes by asking a series of questions and generating responses using the LLMChain model from LangChain and Ollama.

## Installation and Setup

### Step 1: Download Ollama

Download and install Ollama from the links below:
- **MacOS**: [Download](https://ollama.com/download/Ollama-darwin.zip)
- **Linux**: `curl -fsSL https://ollama.com/install.sh | sh`
- **Windows**: [Download](https://ollama.com/download/OllamaSetup.exe)

### Step 2: Start Ollama

After installing, start Ollama with the command:
```sh
ollama start
```
### Step 3: Pull and Run the Llama3 Model

Use the following commands to pull and run the Llama3 model:
```sh
ollama pull llama3
ollama run llama3
```
### Step 4: Install Python Packages
```sh
pip install -r requirements.txt
```
### Step 5: Run the FastAPI Server
```sh
uvicorn main:app --reload
```

### Usage
To interact with the chatbot, you can use curl or any API client to send POST requests. Example:
```sh
curl -X POST "http://127.0.0.1:8000/resume_bot" -H "Content-Type: application/json" -d '{"context": "", "question": "What is your full name?"}'
```
To retrieve all responses:
```sh
curl -X GET "http://127.0.0.1:8000/responses"
```
### Project Structure
**main.py**: The main FastAPI application code. 

**requirements.txt**: List of Python dependencies.

**README.md**: Project overview and setup instructions.

**.gitignore**: Git ignore file.

