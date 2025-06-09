import os
from dotenv import load_dotenv
import sys
from google import genai
from google.genai import types

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")

messages = [
    types.Content(role="user", parts=[types.Part(text=user_prompt)])
]

client = genai.Client(api_key=api_key)

if len(sys.argv) < 2:
    print("Error: No prompt provided. Usage: python3 main.py \"Your prompt here\"")
    sys.exit(1)

prompt = " ".join(sys.argv[1:])

response = client.models.generate_content(
    model="gemini-2.0-flash-001",
    contents=messages,
)

print(response.text)

usage = response.usage_metadata
print(f"Prompt tokens: {usage.prompt_token_count}")
print(f"Response tokens: {usage.candidates_token_count}")