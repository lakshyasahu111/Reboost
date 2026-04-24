from crewai import Task

def load_resume():
    with open("fake_resume.md", "r") as f:
        return f.read()


def get_tasks(job_researcher, resume_analyst, application_writer):

    resume = load_resume()

    resume_analysis_task = Task(
        description=f"""
        Analyze the following resume and suggest improvements:

        {resume}
        """,
        expected_output="Detailed resume improvement suggestions",
        agent=resume_analyst,
        async_execution=False
    )

    job_search_task = Task(
        description=f"""
        Based on this resume:

        {resume}

        Find relevant job openings using search tools.
        """,
        expected_output="List of relevant jobs with links",
        agent=job_researcher,
        async_execution=False
    )

    application_task = Task(
        description=f"""
        Using this resume:

        {resume}

        Create a tailored resume and cover letter for a selected job.
        """,
        expected_output="Optimized resume and cover letter",
        agent=application_writer,
        async_execution=False,
        output_file="tailored_resume.md" 
    )

    return [resume_analysis_task, job_search_task, application_task]