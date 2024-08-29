from tkinter import filedialog
import requests
from pypdf import PdfReader
import os

file_path = filedialog.askopenfilename(
    filetypes=[("PDF files", "*.pdf")])  # Open a dialog to select a file

if file_path:
    # Reading the PDF
    with open(file_path, 'rb') as file:
        reader = PdfReader(file)

        text = ""
        for page in reader.pages:
            text += page.extract_text()
        print(text)

        url = "https://realistic-text-to-speech.p.rapidapi.com/v3/generate_voice_over_v2"

        payload = {
            "voice_obj": {
                "id": 2014,
                "voice_id": "en-US-Neural2-A",
                "gender": "Male",
                "language_code": "en-US",
                "language_name": "US English",
                "voice_name": "John",
                "sample_text": "Hello, hope you are having a great time making your video.",
                "sample_audio_url": "https://s3.ap-south-1.amazonaws.com/invideo-uploads-ap-south-1/speechen-US-Neural2-A16831901130600.mp3",
                "status": 2,
                "rank": 0,
                "type": "google_tts",
                "isPlaying": False
            },
            "json_data": [
                {
                    "block_index": 0,
                    "text": text
                }
            ]
        }
        headers = {
            "x-rapidapi-key": os.getenv("API_KEY"),
            "x-rapidapi-host": "realistic-text-to-speech.p.rapidapi.com",
            "Content-Type": "application/json"
        }

        response = requests.post(url, json=payload, headers=headers)

        print(response.json())
