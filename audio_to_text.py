import os
import speech_recognition as sr

def convert_mp3_to_text(input_file):
    try:
        # Initialize the recognizer
        recognizer = sr.Recognizer()
        
        # Load the audio file
        with sr.AudioFile(input_file) as source:
            # Listen for the data from the audio file
            audio_data = recognizer.record(source)
            
            # Convert speech to text
            text = recognizer.recognize_google(audio_data)
            
            return text
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

# Define the path to the input MP3 file
input_file = r"D:\workspace\codespace\Sentimental analysis\inputs_wav_form\review_5.wav"

