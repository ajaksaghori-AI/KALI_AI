import speech_recognition as sr


class SpeechToText:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("\n🎤 Listening...")
            print("Speak now...\n")

            # Reduce background noise
            self.recognizer.adjust_for_ambient_noise(source, duration=1)

            audio = self.recognizer.listen(source)

        try:
            text = self.recognizer.recognize_google(audio)
            print(f"🗣 You said: {text}")
            return text

        except sr.UnknownValueError:
            print("❌ Sorry, I couldn't understand you.")
            return ""

        except sr.RequestError as e:
            print(f"❌ Speech Recognition service error: {e}")
            return ""