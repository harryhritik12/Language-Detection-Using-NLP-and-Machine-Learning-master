from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)

# Load the model
model = pickle.load(open('lrmodel2.pckl', 'rb'))

@app.route('/detect', methods=['POST'])
def detect_language():
    data = request.get_json()
    text = data.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    prediction = model.predict([text])[0]
    return jsonify({'language': prediction})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
