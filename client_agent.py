"""A second agent that calls the research team remotely over A2A."""
from google.adk.agents import Agent
from google.adk.agents.remote_a2a_agent import RemoteA2aAgent

remote_research_team = RemoteA2aAgent(
    name="remote_research_team",
    description="Remote research team reachable over A2A.",
    agent_card="http://localhost:8001/.well-known/agent-card.json",
)

root_agent = Agent(
    name="assistant",
    model="gemini-2.5-flash",
    instruction="Delegate any research request to remote_research_team.",
    sub_agents=[remote_research_team],
)
