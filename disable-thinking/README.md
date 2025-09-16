<h1>
  <span class="headline">Flask Gemini API</span>
  <span class="subhead">Lesson</span>
</h1>

## Setup

- [Python Genai Codegen Instructions](https://github.com/googleapis/python-genai/blob/main/codegen_instructions.md)
- [Gemini Developer API](https://ai.google.dev/gemini-api/docs)
- [Gemini API quickstart](https://ai.google.dev/gemini-api/docs/quickstart)
- [Test](https://aistudio.google.com/app/apikey?_gl=1*yfj1cc*_ga*NzAyMTQ5NDA3LjE3NTc5NjkzODQ.*_ga_P1DBVKWT6V*czE3NTc5NjkzODMkbzEkZzEkdDE3NTc5Njk5MTMkajYwJGwwJGgxOTQ5MDI4OTI0)

- [Thinking Docs](https://ai.google.dev/gemini-api/docs/thinking)
## Turn off thinking

refresh browser after adding dog question

```py
from google import genai

# The client gets the API key from the environment variable `GEMINI_API_KEY`.
client = genai.Client()

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="What's the best breed of dog for allergies"
)
print(response.text)
```

![](./assets/with-thinking.png)

## Without

1. Add types

```py
from google.genai import types
```

2. Your index route should look like so:

```py
@app.route('/')
def index():
    response = client.models.generate_content(
        model="gemini-2.5-flash", contents="Explain how AI works in a few words",
        config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
        ),
    )
    print(response.text)
    return "Hello, world!"
```

3. restart server and refresh browser

![](./assets/without-thinking.png)
