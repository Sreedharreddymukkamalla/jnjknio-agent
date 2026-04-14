from google.adk.agents.llm_agent import Agent
from google.adk.tools.mcp_tool import McpToolset
from google.adk.tools.mcp_tool.mcp_session_manager import StreamableHTTPConnectionParams

root_agent = Agent(
    model='gemini-2.5-flash',
    name='jnjknio',
    description='jnjknio',
    instruction="""
        njnoj
    """,
    tools=[
        McpToolset(
            connection_params=StreamableHTTPConnectionParams(
                url="https://aeo-mcp-server.amdal-dev.workers.dev/mcp",
            ),
        )
    ]
)
