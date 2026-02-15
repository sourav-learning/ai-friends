from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from .graph import build_graph
from .personas import generate_personas

app = FastAPI()
app.mount("/static", StaticFiles(directory="app/static"), name="static")
graph = build_graph()

sessions = {}  # in-memory for POC


class StartSession(BaseModel):
    human_name: str
    human_age: int
    human_location: str
    temperament: str


class ChatInput(BaseModel):
    session_id: str
    message: str

@app.get("/", response_class=HTMLResponse)
def serve_home():
    with open("app/static/index.html", "r") as f:
        return f.read()
    
@app.post("/start-session")
def start_session(data: StartSession):

    session_id = data.human_name + "_session"

    personas = generate_personas(
        data.human_name,
        data.human_age,
        data.human_location,
        data.temperament
    )

    sessions[session_id] = {
        "human_name": data.human_name,
        "human_age": data.human_age,
        "human_location": data.human_location,
        "temperament": data.temperament,
        "round_number": 0,
        "history": [],
        "summary": "",
        "personas": personas,
        "session_closed": False
    }

    return {
        "session_id": session_id,
        "ai_friends": personas
    }


@app.post("/chat")
def chat(data: ChatInput):

    state = sessions.get(data.session_id)

    if not state:
        return {"error": "Invalid session"}

    if state["session_closed"]:
        return {"message": "Session closed"}

    state["history"].append({
        "speaker": state["human_name"],
        "message": data.message
    })

    updated_state = graph.invoke(state)
    sessions[data.session_id] = updated_state

    return {
        "conversation": updated_state["history"],
        "session_closed": updated_state["session_closed"]
    }
