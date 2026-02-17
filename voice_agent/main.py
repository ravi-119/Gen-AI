import speech_recognition as sr
from google import genai
from google.genai import types
from dotenv import load_dotenv
import os
import sounddevice as sd
import numpy as np

load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=GEMINI_API_KEY)

def play_audio(pcm_bytes, rate=24000, channels=1, sample_width=2):
    dtype_map = {1: np.int8, 2: np.int16, 4: np.int32}
    dtype = dtype_map.get(sample_width, np.int16)
    audio_array = np.frombuffer(pcm_bytes, dtype=dtype)
    if channels > 1:
        audio_array = audio_array.reshape((-1, channels))
    sd.play(audio_array, samplerate=rate)
    sd.wait()

def main():
    r = sr.Recognizer()
    r.energy_threshold = 300
    r.dynamic_energy_threshold = False
    r.pause_threshold = 0.6
    r.phrase_threshold = 0.3

    with sr.Microphone() as source:
        print("Calibrating mic...")
        r.adjust_for_ambient_noise(source, duration=0.3)
        print("Speak something...")
        audio = r.listen(source, timeout=3, phrase_time_limit=5)

    try:
        user_text = r.recognize_google(audio)
        print("You said:", user_text)
    except sr.UnknownValueError:
        print("Could not understand audio")
        return
    except sr.RequestError as e:
        print("STT Error:", e)
        return

    tts_text = f"You said: {user_text}. Hello! This is your voice assistant speaking back."

    response = client.models.generate_content(
        model="gemini-2.5-flash-preview-tts",
        contents=tts_text,
        config=types.GenerateContentConfig(
            response_modalities=["AUDIO"],
            speech_config=types.SpeechConfig(
                voice_config=types.VoiceConfig(
                    prebuilt_voice_config=types.PrebuiltVoiceConfig(voice_name="Kore")
                )
            )
        )
    )

    audio_data = response.candidates[0].content.parts[0].inline_data.data
    play_audio(audio_data)
    print("Finished speaking!")

if __name__ == "__main__":
    main()
