from langgraph.graph import StateGraph, END
from openai import OpenAI
from .state import ConversationState
from .prompts import build_prompt
from .guardrails import topic_allowed, guardrail_instruction
from .summarizer import summarize
from .config import MODEL_NAME, TEMPERATURE

client = OpenAI()

def conversation_node(state: ConversationState):

    if state["session_closed"]:
        return state

    if state["round_number"] >= 4:
        state["session_closed"] = True
        return state

    last_message = state["history"][-1]["message"]

    if not topic_allowed(last_message):
        state["history"].append({
            "speaker": "System",
            "message": "Let's keep the discussion fun and respectful 😊. Maybe we switch topics?"
        })
        return state

    prompt = build_prompt(state, state["personas"])

    response = client.chat.completions.create(
        model=MODEL_NAME,
        temperature=TEMPERATURE,
        messages=[
            {"role": "system", "content": guardrail_instruction()},
            {"role": "user", "content": prompt}
        ],
        max_tokens=700
    )

    output = response.choices[0].message.content

    state["history"].append({
        "speaker": "AI_Group",
        "message": output
    })

    state["round_number"] += 1

    # Compress after round 2
    if state["round_number"] == 2:
        state["summary"] = summarize(state["history"])
        state["history"] = state["history"][-4:]

    # Close logically at round 4
    if state["round_number"] >= 4:
        state["history"].append({
            "speaker": "System",
            "message": "That was fun! Let's continue another time 😊"
        })
        state["session_closed"] = True

    return state


def build_graph():
    builder = StateGraph(ConversationState)

    builder.add_node("conversation", conversation_node)
    builder.set_entry_point("conversation")
    builder.add_edge("conversation", END)

    return builder.compile()
