BANNED_TOPICS = [
    "religion",
    "politics",
    "sex",
    "violence",
    "terrorism",
    "drugs",
]

def topic_allowed(text: str) -> bool:
    lowered = text.lower()
    for topic in BANNED_TOPICS:
        if topic in lowered:
            return False
    return True


def guardrail_instruction():
    return """
You must strictly avoid religion, politics, sex, violence,
illegal activities, personal attacks, or security-related topics.

If any speaker attempts such content:
- Politely redirect the conversation.
- Do not preach.
- Keep tone friendly.
"""
