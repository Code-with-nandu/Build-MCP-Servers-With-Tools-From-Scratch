from mcp.server.fastmcp import FastMCP
mcp = FastMCP("Math")

@mcp.tool()
def add (a:int ,b:int)->int:
    """
    __summary__
    Add to numbers
    """
    return a+b

@mcp.tool()
def multiple(a:int ,b:int)->int:
    """
    Multiply Tow numbers 
    """
    return a*b
    