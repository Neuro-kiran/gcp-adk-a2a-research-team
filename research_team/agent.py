"""Multi-agent research team built with Google's Agent Development Kit (ADK).

Pipeline: parallel Researchers -> Analyst -> Writer, orchestrated by a Coordinator.
The same root agent can be exposed over the A2A protocol (see a2a_server.py).
"""
import os

from google.adk.agents import Agent, ParallelAgent, SequentialAgent
from google.adk.tools import google_search

MODEL = os.getenv("MODEL", "gemini-2.5-flash")

news_researcher = Agent(
    name="news_researcher",
    model=MODEL,
    description="Finds the latest news and announcements on the user's topic.",
    instruction="Search the web for the latest news on the user's topic. "
    "Return 5 concise bullet points with dates and source names.",
    tools=[google_search],
    output_key="news_findings",
)

technical_researcher = Agent(
    name="technical_researcher",
    model=MODEL,
    description="Finds technical docs, benchmarks and implementation details.",
    instruction="Search the web for technical documentation, benchmarks and "
    "implementation guidance on the user's topic. Return 5 concise bullets with sources.",
    tools=[google_search],
    output_key="technical_findings",
)

parallel_research = ParallelAgent(
    name="parallel_research",
    description="Runs news and technical research concurrently.",
    sub_agents=[news_researcher, technical_researcher],
)

analyst = Agent(
    name="analyst",
    model=MODEL,
    description="Synthesises research findings into insights and risks.",
    instruction="You are a senior analyst. Using these findings:\n"
    "NEWS: {news_findings}\nTECHNICAL: {technical_findings}\n"
    "Identify key insights, contradictions and risks. Be concise.",
    output_key="analysis",
)

writer = Agent(
    name="writer",
    model=MODEL,
    description="Writes the final briefing.",
    instruction="Write a clear one-page briefing in Markdown from this analysis:\n"
    "{analysis}\nInclude: Summary, Key Insights, Risks, Next Steps.",
    output_key="briefing",
)

root_agent = SequentialAgent(
    name="research_coordinator",
    description="Researches a topic in parallel, analyses it, and writes a briefing.",
    sub_agents=[parallel_research, analyst, writer],
)
