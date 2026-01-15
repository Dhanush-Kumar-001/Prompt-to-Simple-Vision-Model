import os
import json
from groq import Groq

from llm.validator import validate_pipeline_json

MODEL = "llama-3.3-70b-versatile"


def generate_pipeline_json(user_prompt: str) -> dict:
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY")

    client = Groq(api_key=api_key)

    with open("llm/system_prompt.txt", "r", encoding="utf-8") as f:
        system_prompt = f.read()

    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0
    )

    raw = response.choices[0].message.content

    try:
        parsed = json.loads(raw)
        # 🔹 Normalize task to array (schema requires list)
        if isinstance(parsed.get("task"), str):
            parsed["task"] = [parsed["task"]]

    except json.JSONDecodeError:
        raise ValueError("LLM did not return valid JSON")

    validate_pipeline_json(parsed)
    return parsed
