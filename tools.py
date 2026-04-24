from crewai_tools import SerperDevTool

def get_tools():
    search_tool = SerperDevTool()
    return search_tool