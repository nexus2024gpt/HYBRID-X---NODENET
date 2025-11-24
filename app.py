from fastapi import FastAPI
from pydantic import BaseModel
from mvp.mvp import MVP_HybridXNodeNet

app = FastAPI()
system = MVP_HybridXNodeNet(debug_mode=True)

class Query(BaseModel):
    text: str

@app.post("/simulate")
def simulate(query: Query):
    return system.process_input(query.text)

