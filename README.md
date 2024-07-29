# Resume Builder ChatBot

This project contains a full-fledged web application for building resumes using FastAPI for the backend and Nuxt.js for the frontend.

## Backend (FastAPI)

The FastAPI backend handles the chatbot logic and interacts with the LLMChain model from LangChain and Ollama to build a resume.

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
### Backend (FastAPI)
**main.py**: The main FastAPI application code.

**questions.py**: Contains the question definitions and keys.

**resume_format.py**: Contains the function to format the resume.

**templates/resume_template.html**: The HTML template for the resume.

**requirements.txt**: List of Python dependencies.

**README.md**: Project overview and setup instructions.

**.gitignore**: Git ignore file.

### Frontend (Nuxt.js)
**components/QuestionForm.vue**: Component for handling user inputs and displaying questions.

**pages/index.vue**: Main page for the resume builder.

**nuxt.config.js**: Nuxt.js configuration file.

**package.json**: Node.js dependencies and scripts.

**README.md**: Project overview and setup instructions.

## Steps to create the Nuxt.js project:
### Step 1: Initialize the Nuxt.js Project:
```sh
npx create-nuxt-app resume-builder
cd resume-builder
```

### Step 2: Install Axios for HTTP requests and Configure Axios in nuxt.config.js
```sh
npm install @nuxtjs/axios
```

### Step 3: Create Components and Pages
Codes are mentioned in the above file 
### Step 4: Run the Nuxt.js App
Ensure your FastAPI backend is running. Then start the Nuxt.js development server:
```sh
npm run dev
```
Your Nuxt.js app should now be running at http://localhost:3000.
