class Question:
    def __init__(self, question, key):
        self.question = question
        self.key = key

questions = [
    Question("What is your full name?", key="name"),
    Question("Can you provide your contact information?", key="contact_info"),
    Question("Please give a brief professional summary.", key="summary"),
    Question("Tell me about your work experience.", key="work_experience"),
    Question("What is your educational background?", key="education"),
    Question("List your skills.", key="skills"),
    Question("Do you have any certifications?", key="certifications"),
    Question("Describe any projects you have worked on.", key="projects"),
    Question("What languages do you speak?", key="languages"),
    Question("Can you provide references?", key="references")
]
