import os
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()

# Read API keys
openai_key = os.getenv("OPENAI_API_KEY")
google_key = os.getenv("GOOGLE_API_KEY")
anthropic_key = os.getenv("ANTHROPIC_API_KEY")

print("OpenAI key configured:", bool(openai_key))
print("Google API key configured:", bool(google_key))
print("Anthropic API key configured:", bool(anthropic_key))