<h1>Text Generation API</h1>

This API allows you to generate new text based on a given seed text. It uses a Recurrent Neural Network (RNN) to learn patterns from a provided text dataset and generate text that follows similar patterns.

<h2>How to Use</h2>
To use the Text Generation API, follow these steps:

Install the API by cloning the repository and installing the required dependencies.

Start the API server by running the app.py file.

Make a POST request to the /generate endpoint of the API with the following information:

seed_text: The initial text to start generating from.
length: The desired length of the generated text.
The API will respond with the generated text, which you can use for your desired application or purpose.

API Endpoints
/generate (POST): Generates text based on the provided seed text and length. Send a POST request to this endpoint with a JSON object containing the seed text and desired length. The API will respond with the generated text.
Examples
Here are a few examples of how you can use the API:

Example Request:

Endpoint: /generate
Method: POST
Request Body:
json
Copy code
{
  "seed_text": "Hello",
  "length": 100
}
Response:
json
Copy code
{
  "generated_text": "Generated text..."
}
Example Request:

Endpoint: /generate
Method: POST
Request Body:
json
Copy code
{
  "seed_text": "Lorem ipsum",
  "length": 200
}
Response:
json
Copy code
{
  "generated_text": "Generated text..."
}
Feel free to experiment with different seed texts and lengths to generate diverse and interesting text outputs!

<h2>Model Training</h2>
The Text Generation API uses a Recurrent Neural Network (RNN) model with GRU layers for training. The model is trained on the provided text dataset to learn the underlying patterns and structures in the text. This enables it to generate new text that is coherent and follows similar patterns.