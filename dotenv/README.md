<h1>
  <span class="headline">Add dotenv to Flask</span>
  <span class="subhead"></span>
</h1>

## Install `dotenv`

We don't want to hard code our Gemini API Key for security reasons. We'll use a package called `dotenv` to hide the key in  development.

In a previous lesson setup, we installed `python-dotenv` for storing our Postgresql connection credentials securely in a `.env` file. Let's make use of that package in our Flask application now.

Install the package:

```bash
pipenv install dotenv
```

First create the `.env` file:

```bash
touch .env
```

Within the `.env`, add your GEMINI_API_KEY like so:

```plaintext
GEMINI_API_KEY='AIzaSyBpj2hUOrj_ObGo2z1bWGtLSjoFVU1mc3o'
```

To access these environment variables, we'll need to add an import to the top of `app.py`:

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

With our environment variables accessible, we can build out a connection to Gemini.