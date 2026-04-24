from crewai import Crew
from agents import get_agents
from tasks import get_tasks

def run():

    job_researcher, resume_analyst, application_writer = get_agents()

    tasks = get_tasks(
        job_researcher,
        resume_analyst,
        application_writer
    )

    crew = Crew(
        agents=[job_researcher, resume_analyst, application_writer],
        tasks=tasks,
        verbose=True
    )

    result = crew.kickoff()
    print("\nFINAL RESULT:\n")
    print(result)


if __name__ == "__main__":
    run()