from mcp.server.fastmcp import FastMCP

# Create the FastMCP server instance for STDIO
mcp = FastMCP("mcp-documentation-server")

# Create the FastMCP server instance for streamable-http
# mcp = FastMCP("mcp-documentation-server", port = 8080, host = "localhost")

# Register the tool using FastMCP decorator
@mcp.tool()
def get_documentation_from_database() -> dict:
    """
    This tool returns the documentation from the database for the project. 
    It is very useful for figuring out what the project is about.
    """
    ## actual implementation would query a real database here

    return {
        "title": "How to Use MCP Servers",
        "body": "This is a mocked documentation entry from the database. MCP servers expose tools and resources for AI agents.",
        "source": "mocked_database"
    }

if __name__ == "__main__":
    #local'de ayağa kaldırmak için
    mcp.run(transport= "stdio")

    #remote olarak ayağa kaldırmak için
    # mcp.run(transport= "streamable-http")
