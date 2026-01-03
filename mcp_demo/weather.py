from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Weather")

@mcp.tool()

async def get_weather(location:str)->str:
    """Get the weather"""
    # api to get the weather
    return "Its raiy"


if __name__ == "__main__":
    mcp.run(transport="streamable-http")


