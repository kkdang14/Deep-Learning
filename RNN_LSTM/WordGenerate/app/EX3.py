from flask import Flask, render_template, request
import os
import collections
import numpy as np

os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
import tensorflow as tf

app = Flask(__name__, template_folder='templates')

model = tf.keras.models.load_model(r'C:\Users\HP\PycharmProjects\DeepLearning\RNN_LSTM\WordGenerate\app\model\train.h5')
print(model)

def read_data(fname):
    with open(fname) as f:
        content = f.readlines()
        content = [x.strip() for x in content]
        words = []
        for line in content:
            words.extend(line.split())
    return np.array(words)

def build_dataset(words):
    count = collections.Counter(words).most_common()
    # Add <UNK> token with ID 0 for unknown words
    word2id = {}
    for word, _ in count:
        if word not in word2id:
            word2id[word] = len(word2id)

    id2word = {id: word for word, id in word2id.items()}
    return word2id, id2word
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def index():
    generated_words = []  # Initialize as empty list by default
    if request.method == 'POST':
        input_text = request.form['input_text']

        data = read_data('AliceInTheDreamWorld.txt')
        w2i, i2w = build_dataset(data)

        def encode(sent):
            encoded_sent = [w2i[w] for w in sent.split()]
            encoded_sent = np.array(encoded_sent).reshape(1, 3, 1)
            return encoded_sent

        def generate_text(model, seed_text, num_words=7):
            generated_words = seed_text.split()

            for _ in range(num_words):
                input_text = ' '.join(generated_words[-3:])
                encoded_input = encode(input_text)
                pred = model.predict(encoded_input)
                pred_word = i2w[np.argmax(pred)]
                generated_words.append(pred_word)

            return generated_words  # Return as list for word-by-word display

        generated_words = generate_text(model, input_text)
        generated_words = ' '.join(generated_words)

        return render_template('result.html', input_text=input_text, generated_words=generated_words)
    return render_template('result.html', generated_words=[], input_text="")

if __name__ == '__main__':
    app.run(debug=True)
