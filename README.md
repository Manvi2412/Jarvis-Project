# Jarvis – A Python-Based Virtual Voice Assistant

## Overview

**Jarvis** is a Python-based voice-controlled virtual assistant designed to perform various tasks such as answering questions, playing music, reading the news, and opening web pages. Leveraging OpenAI’s GPT-3.5 and various Python libraries, Jarvis demonstrates intelligent interaction through speech recognition and synthesis.

## Features

- **Speech Recognition & Wake Word Detection**  
  Listens for the keyword “Jarvis” and responds to voice commands.

- **Conversational AI with GPT-3.5**  
  Uses OpenAI's API to generate intelligent and contextual responses.

- **Web Automation**  
  Opens frequently used websites like Google, YouTube, LinkedIn, and Facebook via voice.

- **Real-Time News Updates**  
  Fetches and reads current top headlines from NewsAPI.

- **Music Playback**  
  Plays predefined YouTube links based on voice commands.

- **Text-to-Speech Support**  
  Dual support with `pyttsx3` (offline) and `gTTS` + `pygame` (online).

## Technologies Used

- **Python 3.x**
- `speech_recognition` – for voice input
- `pyttsx3`, `gTTS`, `pygame` – for speech output
- `webbrowser`, `requests` – for automation and API calls
- `openai` – for GPT-3.5 integration
- `NewsAPI` – for news retrieval

## Key Files

- `main.py`: Main voice assistant logic, command routing, and speech processing.
- `musicLibrary.py`: Predefined dictionary of music titles and YouTube links.
- `client.py`: Standalone sample to demonstrate OpenAI GPT integration.

## Setup Instructions

### 1. Clone the Repository
git clone https://github.com/your-username/jarvis-voice-assistant.git
cd jarvis-voice-assistant
### 2. Set Up Virtual Environment (Recommended)
python -m venv venv
source venv/bin/activate   # On Windows: venv\Scripts\activate
### 3. Install Dependencies
pip install -r requirements.txt
### 4. Run the Application
python main.py
Speak “Jarvis” to activate the assistant, followed by a command.



### Example Commands
"Jarvis, what is machine learning?"

"Jarvis, open YouTube."

"Jarvis, play skyfall."

"Jarvis, read the news."

### Sample Output
Initializing Jarvis...
Listening!
Jarvis Active!
You said: What is Python?
Jarvis: Python is a high-level, interpreted programming language known for its simplicity and readability...

### Known Limitations
Limited noise tolerance in speech recognition.

Music playback is hardcoded to predefined YouTube links.

API keys are exposed in current implementation (requires refactoring for production).

### Future Enhancements
Integration with Google Calendar or reminders.

Spotify API or dynamic music search.

Personalized assistant profiles with persistent memory.

GUI version of Jarvis.

