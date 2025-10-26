"""
Whisper ChatGPT Dictation
-------------------------

This script allows you to dictate into ChatGPT (or any active text field) using your voice.
Hold Alt+C, speak, and the script will automatically type your speech in real-time.

Requirements:
- Python 3.7+
- FFmpeg installed and in PATH
- Python packages in requirements.txt

Author: Chandra Sekhar
"""

import whisper
import pyautogui
import keyboard
import sounddevice as sd
import numpy as np
import tempfile
import wave
import time

# -----------------------------
# Load Whisper model (small for speed)
# -----------------------------
model = whisper.load_model("small")

# -----------------------------
# Function to record audio
# -----------------------------
def record_audio(duration=30, fs=16000):
    """
    Records audio from the microphone for the given duration (default 30 seconds)
    Returns the path to a temporary WAV file
    """
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()

    tmp_file = tempfile.NamedTemporaryFile(suffix=".wav", delete=False)
    with wave.open(tmp_file.name, "wb") as wf:
        wf.setnchannels(1)
        wf.setsampwidth(2)
        wf.setframerate(fs)
        wf.writeframes(recording.tobytes())
    return tmp_file.name

# -----------------------------
# Function to transcribe audio using Whisper
# -----------------------------
def transcribe_audio(filename):
    result = model.transcribe(filename)
    return result['text']

# -----------------------------
# Main loop for dictation
# -----------------------------
def dictate_loop():
    """
    Continuously record and type while Alt+C is held
    """
    print("Recording... release Alt+C to stop.")
    while keyboard.is_pressed("alt+c"):
        audio_file = record_audio(duration=30)
        text = transcribe_audio(audio_file)
        if text.strip():
            print(f"Typing: {text}")
            pyautogui.write(text + " ", interval=0.02)  # small delay per character
        time.sleep(0.1)

# -----------------------------
# Bind Alt+C hotkey to start dictation
# -----------------------------
keyboard.add_hotkey("alt+c", dictate_loop)

# -----------------------------
# Main program
# -----------------------------
print("Press Alt+C and hold to dictate into ChatGPT or any text editor.")
print("Press ESC to quit.")
keyboard.wait('esc')


"""
--> Usage for Users
git clone https://github.com/chandrasekhar888/whisper-chatgpt-dictation.git
cd whisper-chatgpt-dictation
python -m venv venv
venv\Scripts\activate.bat
pip install -r requirements.txt
python main.py

Open ChatGPT or any text editor
Hold Alt+C to speak
Release to stop dictation

--> Recommended Repo Folder Structure
whisper-chatgpt-dictation/
│
├─ assets/                     # Screenshots or GIFs for demo
│   └─ demo_screenshot.png
│
├─ main.py                     # Your Python dictation script
├─ requirements.txt            # List of dependencies
├─ README.md                   # Instructions & project info
└─ .gitignore                  # Ignore venv, temp audio files, etc.

"""
