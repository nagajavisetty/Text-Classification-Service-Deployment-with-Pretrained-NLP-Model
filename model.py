from transformers import pipeline
from flask import Flask, request, render_template

app = Flask(__name__)

# Load the model only once when the application starts
classifier = pipeline(
    "zero-shot-classification",
    model="facebook/bart-large-mnli"
)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Validate input
        sentence = request.form['sentence']
        labels = eval(request.form['labels'])  # Convert string to list
        if not sentence or not labels:
            raise ValueError("Invalid input: Sentence or labels missing")

        # Make prediction
        prediction = classifier(sentence, labels)
        output = prediction['labels'][0]

        return render_template(
            'index.html', prediction_text='Prediction: {}'.format(output))

    except Exception as e:
        return render_template('index.html', prediction_text='Error: {}'.format(str(e)))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)
