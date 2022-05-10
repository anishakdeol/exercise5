
### The app is hosted on https://lap4-flask-exercise.herokuapp.com/

- To receive a list of animes use the `/anime` endpoint
- An anime can be posted to the anime endpoint in a test suite e.g. Insomnia
    - The data is sent in the post request is in the JSON format e.g:
    ```json
    {
		"name": "Naruto",
		"year": 2002
    }
    ```
    - The id is automatically generated so it doesn't need to be included in the post request
