from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

template = """
You are a helpful assistant for building resumes. You will ask the user a series of questions to gather all the necessary information for creating a professional resume.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

# Initialize the model
model = OllamaLLM(model="llama3")

# Initialize the prompt template
prompt = ChatPromptTemplate.from_template(template)

# Create the LLM chain with the prompt and model
chain = LLMChain(llm=model, prompt=prompt)

def handle_conversation():
    context = ""
    questions = [
        "What is your full name?",
        "Can you provide your contact information?",
        "Please give a brief professional summary.",
        "Tell me about your work experience.",
        "What is your educational background?",
        "List your skills.",
        "Do you have any certifications?",
        "Describe any projects you have worked on.",
        "What languages do you speak?",
        "Can you provide references?"
    ]
    
    question_index = 0
    
    print("Welcome to the Resume Builder ChatBot! Type 'exit' to quit.")
    
    while question_index < len(questions):
        question = questions[question_index]
        user_input = input(f"{question} ")
        if user_input.lower() == "exit":
            break
        
        try:
            response = chain.invoke({"context": context, "question": user_input})
            print("Debug - Full Response: ", response)
            if 'output' in response:
                result = response['output']
                print("Bot: ", result)
                context += f"\nUser: {user_input}\nAI: {result}"
                question_index += 1
            else:
                print("Error: Missing 'output' key in response")
        except Exception as e:
            print(f"An error occurred: {e}")
    
    # Summarize the collected information
    print("\nThank you! Here is the collected resume information:")
    print(context)

def save_resume(context):
    with open("resume.txt", "w") as file:
        file.write("Resume:\n")
        file.write(context)
    print("Resume saved as resume.txt")
    
if __name__ == "__main__":
    handle_conversation()
    save_resume(context)
