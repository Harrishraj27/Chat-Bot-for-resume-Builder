from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Dict
from app.services import resume_service

router = APIRouter()

class UserInput(BaseModel):
    context: str
    question: str

class BotResponse(BaseModel):
    output: str
    next_question: str

class UserResponse(BaseModel):
    responses: Dict[str, str]

@router.post("/resume_bot", response_model=BotResponse)
async def resume_bot(user_input: UserInput):
    return await resume_service.handle_resume_bot(user_input)

@router.get("/responses", response_model=UserResponse)
async def get_responses():
    return resume_service.get_responses()

@router.get("/generate_resume")
async def generate_resume():
    return resume_service.generate_resume()
