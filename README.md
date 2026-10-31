# GCP Multi-Agent Research Team (ADK + A2A + Gemini)

A multi-agent system on Google Cloud using the **Agent Development Kit (ADK)**, **Gemini on Vertex AI**, and the **Agent2Agent (A2A) protocol**.

```
User topic -> [news_researcher || technical_researcher] -> analyst -> writer -> briefing
                        (ParallelAgent)                    (SequentialAgent)
```

- `research_team/agent.py` - parallel research agents with Google Search grounding, analyst, writer
- `a2a_server.py` - exposes the team as an A2A server (agent card + JSON-RPC)
- `client_agent.py` - another agent that calls the team remotely via `RemoteA2aAgent`
- `Dockerfile`, `deploy.sh` - deploy to Cloud Run

## Quickstart

```bash
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env   # set your project / credentials
gcloud auth application-default login
adk web                # local dev UI, pick "research_team"
```

Run as an A2A service:

```bash
uvicorn a2a_server:a2a_app --port 8001
curl http://localhost:8001/.well-known/agent-card.json
```

Test: `pytest`

## Deploy to Cloud Run

```bash
export GOOGLE_CLOUD_PROJECT=your-project
./deploy.sh
```

## Stack
Python, google-adk, Gemini (Vertex AI), A2A, Cloud Run.
