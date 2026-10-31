from research_team.agent import root_agent


def test_pipeline_shape():
    assert [a.name for a in root_agent.sub_agents] == ["parallel_research", "analyst", "writer"]


def test_parallel_researchers():
    names = {a.name for a in root_agent.sub_agents[0].sub_agents}
    assert names == {"news_researcher", "technical_researcher"}
