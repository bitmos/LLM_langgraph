from langchain_mcp_adapters.client import MultiServerMCPClient
from langgraph.prebuilt import create_react_agent
from langchain_core.messages import SystemMessage

from langchain_groq import ChatGroq
from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
    {
        "math":{
            "command":"python",
            "args":["mathserver.py"],
            "transport":"stdio",
        },
         "weather":{
            "url":"http://127.0.0.1:8000/mcp",
            "transport":"streamable_http",
        },
    })
    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model="llama-3.1-8b-instant")
    agent = create_react_agent(model,tools)

    math_response = await agent.ainvoke({"messages":[SystemMessage(content="You may only use the math and weather tools provided. Do not call any search tools.You must produce a final answer after one tool call or less."),
                                                     {"role":"user", "content":"What is 3+2 add"}]})
    print(math_response)

    print(math_response["messages"][-1].content)


asyncio.run(main())