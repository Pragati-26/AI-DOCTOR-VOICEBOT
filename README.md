# AI Doctor VoiceBot

This repository contains an AI-based voice bot for a doctor-patient interaction demo.

## Files

- `brain_of_the_doctor.py`: core logic for doctor agent.
- `gradio_app.py`: web UI using Gradio.
- `voice_of_the_doctor.py`: TTS voice generation for doctor.
- `voice_of_the_patient.py`: TTS voice generation for patient.
- `Dockerfile`: containerization configuration.
- `Pipfile` / `requirements.txt`: Python dependencies.

## Setup

1. Install dependencies:
   - `pip install -r requirements.txt`
   - or `pipenv install`.
2. Run the app:
   - `python gradio_app.py`
3. Open the local Gradio URL shown in terminal.

## Notes

- This project is designed as a prototype and may require valid API keys (e.g., OpenAI, ElevenLabs) depending on the voice model backends.
- Update configuration details in source files as necessary.
