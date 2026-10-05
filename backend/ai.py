import json
import ollama


MODEL_NAME = "qwen2.5-coder:3b"


def analyze_mood(name: str, mood: str):

    prompt = f"""
You are an AI music recommendation assistant.

Analyze the user's mood and determine what kind of music would suit them.

User name: {name}

User's description:
{mood}

Return ONLY valid JSON.

Use exactly this structure:

{{
    "mood": "happy",
    "energy": "high",
    "music_style": "pop",
    "description": "short description of the user's mood"
}}

Rules:

- mood must be one of:
  happy, sad, relaxed, energetic, romantic, angry,
  focused, nostalgic, stressed, calm, motivational

- energy must be one of:
  low, medium, high

- music_style should be a short music style such as:
  pop, rock, indie, acoustic, lo-fi, classical,
  hip-hop, electronic, bollywood, rnb, jazz

Do not add markdown.
Do not add explanations outside the JSON.
"""

    response = ollama.generate(
        model=MODEL_NAME,
        prompt=prompt,
        format="json"
    )

    result = json.loads(response["response"])

    return result
