<h1>
  <span class="headline">Dot Env</span>
  <span class="subhead">Lesson</span>
</h1>

## Setup

- [Python Genai Codegen Instructions](https://github.com/googleapis/python-genai/blob/main/codegen_instructions.md)
- [Gemini Developer API](https://ai.google.dev/gemini-api/docs)
- [Gemini API quickstart](https://ai.google.dev/gemini-api/docs/quickstart)
- [Test](https://aistudio.google.com/app/apikey?_gl=1*yfj1cc*_ga*NzAyMTQ5NDA3LjE3NTc5NjkzODQ.*_ga_P1DBVKWT6V*czE3NTc5NjkzODMkbzEkZzEkdDE3NTc5Njk5MTMkajYwJGwwJGgxOTQ5MDI4OTI0)


In our initial setup, we installed `psycopg2`, a popular PostgreSQL Python driver, and `python-dotenv` for storing our connection credentials securely in a `.env` file. Let's make use of these packages in our Flask application now.

Install the package:

```bash
pipenv install dotenv
```

First create the `.env` file:

```bash
touch .env
```

Within the `.env`, add your local PostgreSQL credentials like so:

```plaintext
GEMINI_API_KEY='AIzaSyBpj2hUOrj_ObGo2z1bWGtLSjoFVU1mc3o'
```

To access these environment variables, we'll need to add an import in `app.py`:

```python
# app.py
from dotenv import load_dotenv
```

Next we'll call upon `load_dotenv` directly above the initialization of our Flask app:

```python
# app.py
# Add the following:
load_dotenv()

app = Flask(__name__)
```

> 💡 By default, `load_dotenv()` looks for a file named `.env` in the current directory. It loads the environment variables defined in that file, and makes them accessible through `os.environ`. 

With our environment variables accessible, we can build out a connection to our database. We can consult the [Psycopg documentation](https://www.psycopg.org/docs/usage.html) for basic guidance on connecting to our PostgreSQL database from Python.


