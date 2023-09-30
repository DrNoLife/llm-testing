from flask import Flask, request, jsonify
from transformers import pipeline
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.get_json()
    text = data.get('Text', '')
    model_name = data.get('Model', 'sshleifer/distilbart-cnn-12-6')

    summarizer = pipeline("summarization", model=model_name)

    input_length = len(text.split())
    max_length = 100

    if input_length > 250:
        max_length = 150
    elif input_length > 150:
        max_length = 100
    else:
        max_length = 50
    
    try:
        summary = summarizer(text, max_length=max_length, min_length=40, do_sample=False)
        summary_text = summary[0]["summary_text"]
    except Exception as e:
        return jsonify(error=str(e)), 400

    return jsonify(summary=summary_text)

@app.route('/generate-title', methods=['POST'])
def generate_title():
    data = request.get_json()
    text = data.get('Text', '')
    model_name = data.get('Model', 'gpt2')

    generator = pipeline("text-generation", model=model_name)

    # Create a prompt for title generation
    prompt = f"Title: {text}"
    
    try:
        title_data = generator(
            prompt, 
            max_length=60, 
            do_sample=True, 
            temperature=0.5, 
            num_beams=10, 
            early_stopping=True)

        title = title_data[0]['generated_text'].replace(prompt, '').strip()
    except Exception as e:
        logging.exception("Exception occurred during title generation")
        return jsonify(error=str(e)), 400

    return jsonify(title=title)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
