import os

class Settings:
    GROQ_API_KEY = os.getenv('GROQ_API_KEY', 'API KEY FROM GROQ')

settings = Settings()
