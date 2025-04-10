# 🗣️ Jarvis – Voice-Controlled Virtual Assistant (Python)

Jarvis is a voice-activated personal assistant built using Python. It can respond to voice commands, perform web-based tasks, and interact with APIs to provide useful, real-time information.

## 🤖 Features

- Voice-activated command recognition using `speech_recognition`
- Converts text to speech responses using `pyttsx3` and `gTTS`
- Performs tasks like:
  - Opening websites (Google, YouTube, etc.)
  - Fetching latest news headlines via NewsAPI
  - Time and date updates
  - Responding using OpenAI's GPT API (if enabled)

## 🛠️ Technologies Used

- **Language**: Python  
- **Libraries**: `speech_recognition`, `pyttsx3`, `gTTS`, `webbrowser`, `pygame`, `requests`, `datetime`  
- **Environment**: VS Code / Jupyter Notebook

## 🚀 How It Works

1. Listens for a wake word (“Jarvis”)
2. Recognizes the voice input and converts it to text
3. Matches the command and executes the appropriate function
4. Gives verbal feedback using a text-to-speech engine

## 📁 Project Structure

- `main.py` – core script with command logic
- `voice.py` – handles voice input/output
- `api_handler.py` – (optional) news/GPT integration
- `requirements.txt` – all dependencies

