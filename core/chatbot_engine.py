import os
from dotenv import load_dotenv
from google import genai

# Load environment variables
load_dotenv()

# Get API key
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

# Create Gemini client
client = genai.Client(api_key=GEMINI_API_KEY)


# Function that app.py can import
def chatbot_response(user_input):

    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input
    )

    return response.text