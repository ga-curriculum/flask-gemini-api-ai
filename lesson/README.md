<h1>
  <span class="headline">Flask Gemini API</span>
  <span class="subhead">Lesson</span>
</h1>

## Setup

tktk The below is a generic starting point for lecture setup. You may need to make adjustments to this.

Open your Terminal application and navigate to your <code class="filepath">~/code/ga/lectures</code> directory:

```bash
cd ~/code/ga/lectures
```

Make a new directory called <code class="filepath">tktk-module-name</code>, then enter this directory:

```bash
mkdir tktk-module-name
cd tktk-module-name
```

Open the contents of the directory in VS Code:

```bash
code .
```

tktk Are there more lecture setup steps? Don't forget to add them here.

## tktk Next Section Title

- [Python Genai Codegen Instructions](https://github.com/googleapis/python-genai/blob/main/codegen_instructions.md)
- [Gemini Developer API](https://ai.google.dev/gemini-api/docs)
- [Gemini API quickstart](https://ai.google.dev/gemini-api/docs/quickstart)
- [Test](https://aistudio.google.com/app/apikey?_gl=1*yfj1cc*_ga*NzAyMTQ5NDA3LjE3NTc5NjkzODQ.*_ga_P1DBVKWT6V*czE3NTc5NjkzODMkbzEkZzEkdDE3NTc5Njk5MTMkajYwJGwwJGgxOTQ5MDI4OTI0)

```py
# # app.py
from flask import Flask, request
from google import genai
from google.genai import types

client = genai.Client(api_key='AIzaSyBpj2hUOrj_ObGo2z1bWGtLSjoFVU1mc3o')

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route('/ai', methods=['POST'])
def create_ai():
    print(request.json)
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=request.json['query'],
        config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
        ),
)
    print(response.text)
    return response.text


if __name__ == "__main__":
    app.run()
```


tktk Write the content for the lesson here.
