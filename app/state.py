from typing import List, Dict, TypedDict

class ConversationState(TypedDict):
    human_name: str
    human_age: int
    human_location: str
    temperament: str
    round_number: int
    history: List[Dict[str, str]]
    summary: str
    personas: List[Dict]
    session_closed: bool
