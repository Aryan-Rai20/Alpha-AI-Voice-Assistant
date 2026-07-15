from google import genai
from config import GEMINI_API_KEY

client = genai.Client(api_key=GEMINI_API_KEY)

API_KEY = "API_KEY_HERE"

client = genai.Client(api_key=API_KEY)


def ask_ai(prompt):
    try:
        response = client.models.generate_content(
            model="gemini-3.1-flash-lite",
            contents=f"""
You are Alpha, a voice assistant.

Rules:
- Reply in maximum 3-4 lines.
- Keep answers short.
- If the user asks for code, provide only the code.

User: {prompt}
"""
        )

        return response.text

    except Exception as e:
        return f"AI Error: {e}"
