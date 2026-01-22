from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="MCP Calculator Server")

class CalcRequest(BaseModel):
    a: float
    b: float

@app.get("/")
def root():
    return {"status": "MCP Server is running"}

@app.post("/tools/add")
def add(req: CalcRequest):
    return {"result": req.a + req.b}

@app.post("/tools/subtract")
def subtract(req: CalcRequest):
    return {"result": req.a - req.b}

@app.post("/tools/multiply")
def multiply(req: CalcRequest):
    return {"result": req.a * req.b}

@app.post("/tools/divide")
def divide(req: CalcRequest):
    if req.b == 0:
        return {"error": "Division by zero"}
    return {"result": req.a / req.b}
