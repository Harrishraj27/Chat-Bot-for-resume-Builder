from .resume import Resume
from pydantic import BaseModel
from typing import List, Optional

class Resume(BaseModel):
    name: str
    contact_info: str
    summary: str
    work_experience: List[str]
    education: List[str]
    skills: List[str]
    certifications: Optional[List[str]] = []
    projects: Optional[List[str]] = []
    languages: Optional[List[str]] = []
    references: Optional[List[str]] = []
