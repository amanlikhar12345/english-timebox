import speech_recognition as sr


class SpeechToTextService:

    def convert_audio_to_text(self, audio_path):
        recognizer = sr.Recognizer()

        with sr.AudioFile(audio_path) as source:
            audio = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio)
            return text

        except sr.UnknownValueError:
            return "Could not understand the audio."

        except sr.RequestError:
            return "Speech recognition service is unavailable."