def format_resume(responses: dict) -> str:
    resume = f"""
    Name: {responses.get('name', 'N/A')}
    Contact Information: {responses.get('contact_info', 'N/A')}
    
    Professional Summary:
    {responses.get('summary', 'N/A')}
    
    Work Experience:
    {responses.get('work_experience', 'N/A')}
    
    Education:
    {responses.get('education', 'N/A')}
    
    Skills:
    {responses.get('skills', 'N/A')}
    
    Certifications:
    {responses.get('certifications', 'N/A')}
    
    Projects:
    {responses.get('projects', 'N/A')}
    
    Languages:
    {responses.get('languages', 'N/A')}
    
    References:
    {responses.get('references', 'N/A')}
    """
    return resume
