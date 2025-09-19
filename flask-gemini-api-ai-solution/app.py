# app.py
from dotenv import load_dotenv

# Import the 'Flask' class from the 'flask' library.
from flask import Flask, request
from google import genai
from google.genai import types

# Initialize Flask
# We'll use the pre-defined global '__name__' variable to tell Flask where it is.
load_dotenv()
app = Flask(__name__)
client = genai.Client()


# Define our route
# This syntax is using a Python decorator, which is essentially a
# succinct way to wrap a function in another function.
@app.route("/")
def index():
    return "Hello, world!"


@app.route("/ai", methods=["POST"])
def ai_request():
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.json["query"],
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0)  # Disables thinking
        ),
    )
    print(response.text)
    return response.text

# Run our application, by default on port 5000
app.run()
