from crewai import Agent
from config import LLM_MODEL

def get_agents():

    resume_analyst = Agent(
        role="Resume Analyst",
        goal="Analyze and improve resumes for job applications",
        backstory="Expert in resume screening and ATS optimization",
        llm=LLM_MODEL,
        verbose=True
    )

    job_researcher = Agent(
        role="Job Researcher",
        goal="Find relevant job roles based on candidate profile",
        backstory="Expert in job market research",
        llm=LLM_MODEL,
        verbose=True
    )

    application_writer = Agent(
        role="Application Writer",
        goal="Write tailored resumes and cover letters",
        backstory="Expert in crafting job-winning applications",
        llm=LLM_MODEL,
        verbose=True
    )

    return resume_analyst, job_researcher, application_writer