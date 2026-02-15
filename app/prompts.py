import random

def build_prompt(state, personas):

    speaker_driver = random.choice(personas)["name"]

    return f"""
You are simulating a group of 3 close friends with the human user using the application.

Human:
Name: {state['human_name']}
Age: {state['human_age']}
Temperament: {state['temperament']}

AI Friends:
{personas}

Conversation Rules:
- 4 total rounds only.
- Random participation (NOT round robin).
- Natural human-like tone.
- Mild humour.
- One friend subtly drives conversation but not bossy.
- Allow human to interact naturally.
- Avoid sensitive topics.
- If any speaker approaches sensitive topic, politely redirect.
- Follow local culture context if possible.
- Avoid sounding robotic or repetitive.
- End round 4 logically and warmly.

Conversation so far:
Summary:
{state['summary']}

Recent Messages:
{state['history'][-6:]}

Generate next round conversation as dialogue:

Format:
Name: message
Name: message
...
"""
