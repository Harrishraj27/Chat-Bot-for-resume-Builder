# Example utility function for formatting resumes
from jinja2 import Environment, FileSystemLoader

def format_resume(user_data):
    env = Environment(loader=FileSystemLoader('app/templates'))
    template = env.get_template('resume_template.html')
    return template.render(user_data)
