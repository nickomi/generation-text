# Text Generation API

This API allows you to generate new text based on a given seed text. It uses a Recurrent Neural Network (RNN) to learn patterns from a provided text dataset and generate text that follows similar patterns.

## How to Use

To use the Text Generation API, follow these steps:

1. Install the API by cloning the repository and installing the required dependencies.

2. Start the API server by running the `app.py` file.

3. Make a POST request to the `/generate` endpoint of the API with the following information:

   - `seed_text`: The initial text to start generating from.
   - `length`: The desired length of the generated text.

4. The API will respond with the generated text, which you can use for your desired application or purpose.

## API Endpoints

- `/generate` (POST): Generates text based on the provided seed text and length. Send a POST request to this endpoint with a JSON object containing the seed text and desired length. The API will respond with the generated text.

## Examples

Here are a few examples of how you can use the API:

1. Example Request:
   - Endpoint: `/generate`
   - Method: POST
   - Request Body:
     ```json
     {
       "seed_text": "Hello",
       "length": 100
     }
     ```
   - Response:
     ```json
     {
       "generated_text": "Generated text..."
     }
     ```

2. Example Request:
   - Endpoint: `/generate`
   - Method: POST
   - Request Body:
     ```json
     {
       "seed_text": "Lorem ipsum",
       "length": 200
     }
     ```
   - Response:
     ```json
     {
       "generated_text": "Generated text..."
     }
     ```

Feel free to experiment with different seed texts and lengths to generate diverse and interesting text outputs!

## Model Training

The Text Generation API uses a Recurrent Neural Network (RNN) model with GRU layers for training. The model is trained on the provided text dataset to learn the underlying patterns and structures in the text. This enables it to generate new text that is coherent and follows similar patterns.
