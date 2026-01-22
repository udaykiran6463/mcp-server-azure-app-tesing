from fastmcp import FastMCP
mcp = FastMCP(
    name="basic-caluclator",
)


@mcp.tool(
        name="add",
        description="add two numbers",
        tags=["add", "math"],
)
def add(a, b):
    return a + b

@mcp.tool(
        name="subtract",
        description="subtract two numbers",
        tags=["subtract", "math"],
)
def subtract(a, b):
    return a - b   

@mcp.tool(
        name="multiply",
        description="multiply two numbers",
        tags=["multiply", "math"],
)
def multiply(a, b):
    return a * b

@mcp.tool(
        name="divide",
        description="divide two numbers",
        tags=["divide", "math"],
)
def divide(a, b):
    return a / b



if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0", port=8000)