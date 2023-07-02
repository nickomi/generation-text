from flask import Flask, request, jsonify
import numpy as np
import tensorflow as tf

app = Flask(__name__)

# Load the text data for training
text = open("your_file.txt", "r").read()  # Replace "your_file.txt" with the path to your text file

# Create a character dictionary
chars = sorted(list(set(text)))
char_to_index = {char: index for index, char in enumerate(chars)}
index_to_char = {index: char for index, char in enumerate(chars)}

# Prepare the training data
input_length = 100
step = 3
sentences = []
next_chars = []
for i in range(0, len(text) - input_length, step):
    sentences.append(text[i:i + input_length])
    next_chars.append(text[i + input_length])

# Convert the training data into a numerical format
x = np.zeros((len(sentences), input_length, len(chars)), dtype=np.bool)
y = np.zeros((len(sentences), len(chars)), dtype=np.bool)
for i, sentence in enumerate(sentences):
    for t, char in enumerate(sentence):
        x[i, t, char_to_index[char]] = 1
    y[i, char_to_index[next_chars[i]]] = 1

# Create and train the RNN model
model = tf.keras.models.Sequential([
    tf.keras.layers.GRU(256, input_shape=(input_length, len(chars)), return_sequences=True),
    tf.keras.layers.GRU(256),
    tf.keras.layers.Dense(len(chars), activation='softmax')
])
model.compile(loss='categorical_crossentropy', optimizer='adam')
model.fit(x, y, batch_size=128, epochs=50)

# Function to generate text
def generate_text(seed_text, length):
    generated_text = seed_text
    for _ in range(length):
        x_pred = np.zeros((1, input_length, len(chars)))
        for t, char in enumerate(seed_text):
            x_pred[0, t, char_to_index[char]] = 1
        preds = model.predict(x_pred)[0]
        next_char_index = np.random.choice(len(chars), p=preds)
        next_char = index_to_char[next_char_index]
        generated_text += next_char
        seed_text = seed_text[1:] + next_char
    return generated_text

# Define the API endpoint
@app.route('/generate', methods=['POST'])
def generate():
    data = request.get_json()
    seed_text = data['seed_text']
    length = data['length']
    generated_text = generate_text(seed_text, length)
    return jsonify({'generated_text': generated_text})

if __name__ == '__main__':
    app.run()