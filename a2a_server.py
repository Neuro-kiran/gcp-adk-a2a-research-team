"""Expose the research team as an A2A (Agent2Agent) server.

Run:  uvicorn a2a_server:a2a_app --host 0.0.0.0 --port 8001
Agent card: http://localhost:8001/.well-known/agent-card.json
"""
from google.adk.a2a.utils.agent_to_a2a import to_a2a

from research_team.agent import root_agent

a2a_app = to_a2a(root_agent, port=8001)
