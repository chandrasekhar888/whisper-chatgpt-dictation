# 🎙️ Whisper ChatGPT Dictation  
### Voice → Text → ChatGPT Automation using OpenAI Whisper

Turn your **voice into instant text** inside ChatGPT (or any text field) — using OpenAI’s Whisper model and a simple hotkey.  
Hold **Alt + C**, speak naturally, and your words will be typed automatically.  

---

## 🚀 What It Does  
A lightweight Python tool that listens to your voice, transcribes it using **Whisper**, and types it out live using **PyAutoGUI** — perfect for ChatGPT, coding, note-taking, or dictation.

---

## 💡 Why It’s Useful  
- Speak naturally — no need to type long prompts manually  
- Works offline (Whisper runs locally)  
- Great for creators, coders, and multitaskers  
- Simple setup — 3 commands and you’re dictating!  

---

## ✨ Features  
- 🎧 Hold-to-talk voice recording (`Alt + C`)  
- 🔤 Real-time transcription with Whisper  
- 💬 Auto-typing text in active window (ChatGPT, Docs, etc.)  
- 🧠 30-second capture window for smoother continuous dictation  
- ⏹️ Stop anytime — just release the hotkey  
- ⚙️ Lightweight, clean, and open-source  

---

## ⚙️ Installation  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/chandrasekhar888/whisper-chatgpt-dictation.git
cd whisper-chatgpt-dictation
2️⃣ Create and Activate Virtual Environment
bash
Copy code
python -m venv venv
# On Windows
venv\Scripts\activate.bat
# On Mac/Linux
source venv/bin/activate
3️⃣ Install Dependencies
bash
Copy code
pip install -r requirements.txt
Dependencies:

Copy code
openai-whisper
keyboard
pyautogui
sounddevice
numpy
🔧 FFmpeg Setup
Whisper needs FFmpeg for audio handling.

Download FFmpeg full build from:
👉 https://www.gyan.dev/ffmpeg/builds/

Extract it (e.g. D:\AI\ffmpeg-8.0-full_build)

Copy the path of the bin folder (e.g. D:\AI\ffmpeg-8.0-full_build\bin)

Add it to System Environment Variables → Path

Verify it’s working:

bash
Copy code
ffmpeg -version
▶️ How to Use
Open Command Prompt or PowerShell and run:

bash
Copy code
cd whisper-chatgpt-dictation
venv\Scripts\activate.bat
python dictate_continuous.py
Then:

Open ChatGPT or any text editor

Hold Alt + C and start speaking

Release Alt + C to stop recording

Your speech instantly appears as text 🎤💬
