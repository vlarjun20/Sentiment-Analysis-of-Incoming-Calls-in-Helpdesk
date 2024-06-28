from flask import Flask, render_template, request, jsonify
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import os
import speech_recognition as sr
import io

app = Flask(__name__)

sentiment_labels = ["Very Negative", "Negative", "Neutral", "Positive", "Very Positive"]

def convert_mp3_to_text(audio_file):
    try:
        # Initialize the recognizer
        recognizer = sr.Recognizer()
        
        # Load the audio file
        with sr.AudioFile(audio_file) as source:
            # Listen for the data from the audio file
            audio_data = recognizer.record(source)
            
            # Convert speech to text
            text = recognizer.recognize_google(audio_data)
            
            return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
    
def analyze_sentiment(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)

    # Perform inference
    with torch.no_grad():
        outputs = model(**inputs)
    
    # Extract predicted sentiment
    predicted_scores = torch.softmax(outputs.logits, dim=1)
    predicted_label = sentiment_labels[predicted_scores.argmax().item()]

    return predicted_label

# Load the sentiment analysis model and tokenizer
saved_model_dir = r"D:\Sentimental analysis\bert_sentiment_model"
tokenizer = AutoTokenizer.from_pretrained(saved_model_dir)
model = AutoModelForSequenceClassification.from_pretrained(saved_model_dir)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/transcribe', methods=['POST'])
def transcribe():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'})

    audio_file = request.files['audio']
    audio_data = audio_file.read()
    
    # Convert audio to text
    derived_text = convert_mp3_to_text(io.BytesIO(audio_data))
    if derived_text is None:
        return jsonify({'error': 'Failed to transcribe audio'})

    # Perform sentiment analysis
    derived_sentiment = analyze_sentiment(derived_text)
    
    return jsonify({'transcription': derived_text, 'sentiment': derived_sentiment})

if __name__ == '__main__':
    app.run(debug=True)
