from openai import OpenAI
from .config import MODEL_NAME

client = OpenAI()

def summarize(history):
    text_block = "\n".join([f"{h['speaker']}: {h['message']}" for h in history])

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[
            {"role": "system", "content": "Summarize briefly for memory compression."},
            {"role": "user", "content": text_block}
        ],
        max_tokens=150
    )

    return response.choices[0].message.content
