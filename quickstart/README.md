<h1>
  <span class="headline">Flask Gemini API Quickstart</span>
  <span class="subhead"></span>
</h1>

## Helpful Gemini Links

- [Python Genai Codegen Instructions](https://github.com/googleapis/python-genai/blob/main/codegen_instructions.md)
- [Gemini Developer API](https://ai.google.dev/gemini-api/docs)
- [Gemini API quickstart](https://ai.google.dev/gemini-api/docs/quickstart)

<br>

## Connect Flask to Gemini

To connect Flask to Gemini we'll follow the [Gemini quick start instructions](https://ai.google.dev/gemini-api/docs/quickstart).

![](./assets/quickstart.png)

<br>

## Install the Google GenAI SDK

First, we need to install the Google GenAI SDK. Note - your install command may be slightly different if you're using `pipenv`.

```bash
pipenv install google-genai
```

<br>

## Make Your First Gemini Request

1. Following the [Gemini quick start instructions](https://ai.google.dev/gemini-api/docs/quickstart), we first need to add this to the top of `app.py` with our other imports. This will import the SDK.

    ```py
    from google import genai
    ```

    <br>


2. We need to establish a connection to the Gemini API. We will need out API key for this step. Note that the documentation states... 

    > If you set your API key as the environment variable GEMINI_API_KEY, it will be picked up automatically by the client when using the Gemini API libraries.

    <br>

    To establish a connection, I added the following line just below `app = Flask(__name__)` in `app.py`.

    ```py
    # The client gets the API key from the environment variable `GEMINI_API_KEY`.
    client = genai.Client()
    ```

    <br>
    
3. Next, let's define a new route named `/ai`. This is where we'll add the additional bit of code from the documentation:

    ```py
    @app.route('/ai')
    def ai_request():
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents="Explain how AI works in a few words"
        )
        print(response.text)
        return response.text # I added this return statement because Flask requires one.
    ```

    You can read more about the various `models` available in the Gemini documentation. We're using the free option.
    
    <br>
    
4. Restart your server and navigate to http://127.0.0.1:5000/ai in your browser. If everything works correctly you should see the value of the `response.text` in your server logs.


   ![](./assets/terminal-output.png)

5. The text should also return to the browser.

   ![](./assets/browser-output.png)

#### Congrats! You've successfully made a request to an AI!