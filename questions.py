from pydantic import BaseModel

class Question(BaseModel):
    question: str
    key: str

questions = [
    Question(question="What is your full name?", key="name"),
    Question(question="Can you provide your contact information?", key="contact_info"),
    Question(question="Please give a brief professional summary.", key="summary"),
    Question(question="Tell me about your work experience.", key="work_experience"),
    Question(question="What is your educational background?", key="education"),
    Question(question="List your skills.", key="skills"),
    Question(question="Do you have any certifications?", key="certifications"),
    Question(question="Describe any projects you have worked on.", key="projects"),
    Question(question="What languages do you speak?", key="languages"),
    Question(question="Can you provide references?", key="references")
]
