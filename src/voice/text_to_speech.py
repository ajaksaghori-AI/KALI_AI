import pyttsx3


class TextToSpeech:

    def speak(self, text):

        print(f"[DEBUG] Text received by TTS: {repr(text)}")

        engine = pyttsx3.init()

        engine.setProperty("rate", 170)
        engine.setProperty("volume", 1.0)

        engine.say(str(text))

        engine.runAndWait()

        engine.stop()