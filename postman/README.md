<h1>
  <span class="headline">Use Postman to Send Requests to the Gemini API</span>
</h1>

## Helpful Gemini Links

- [Python Genai Codegen Instructions](https://github.com/googleapis/python-genai/blob/main/codegen_instructions.md)
- [Gemini Developer API](https://ai.google.dev/gemini-api/docs)
- [Gemini API quickstart](https://ai.google.dev/gemini-api/docs/quickstart)
- [Thinking Docs](https://ai.google.dev/gemini-api/docs/thinking)

## Refactor the `/ai` route

Currently, our Gemini request is hardcoded in the `contents` property. Let's refactor our route and make it more dynamic so that we can send custom requests from Postman.

1. Currently, our `/ai` route is defined with the `GET` http verb. We need to re-define it as a `POST` route by adding a `methods` property. Convention dictates that `POST` request is used to create something (or, in this case, it expects to receive a body or some data in the request).

    ```py
    @app.route('/ai', methods=['POST'])
    ```

<br>


2. Next, we need to import the Flask `request` module at the top of `app.py`. This wilo allow us to parse the bosy of the request.

    ```py
    from flask import Flask, request
    ```

<br>

3. Flask will expect a `query` property in the body of the request. We'll set up this property in Postman shortly. Flask will access it like so: `request.json['query']`. 

    We'll assign the value of `request.json['query']` to the `contents` property. Here's our refactored `/ai` route:

    ```py
    @app.route('/ai', methods=['POST'])
    def ai_request():
        response = client.models.generate_content(
            model="gemini-2.5-flash", contents=request.json['query'],
            config=types.GenerateContentConfig(
            thinking_config=types.ThinkingConfig(thinking_budget=0) # Disables thinking
            ),
        )
        print(response.text)
        return response.text
    ```
<br>

4. Make sure to restart your server.

<br>

5. Let's test our code using Postman. Follow the screenshot below. 

    - Make a `POST` request to `http://127.0.0.1:5000/ai`. 
    - The body of the request should be a raw JSON object with a `query` property like so:

    ![](./assets/postman-query.png)


#### Send a few queries of your own!