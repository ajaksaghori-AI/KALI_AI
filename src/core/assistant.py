from src.core.kali import Kali
from src.core.conversation import ConversationEngine
from src.voice.text_to_speech import TextToSpeech
from src.voice.speech_to_text import SpeechToText


class Assistant:

    def __init__(self):
        self.kali = Kali()
        self.brain = ConversationEngine()
        self.speaker = TextToSpeech()
        self.listener = SpeechToText()

    def start(self):

        # Greeting
        greeting = self.kali.greet()

        print(greeting)
        self.speaker.speak(greeting)

        # Continuous conversation
        while True:

            text = self.listener.listen()

            if not text:
                continue

            print(f"\nYou : {text}")

            # Exit commands
            exit_commands = [
                "bye",
                "exit",
                "quit",
                "stop",
                "terminate",
                "shutdown",
                "close kali",
                "stop kali",
                "exit kali",
                "terminate kali",
                "shutdown kali"
            ]

            if any(command in text.lower().strip() for command in exit_commands):

                farewell = "Goodbye Chaitanya. Shutting down KALI AI."

                print(f"KALI : {farewell}")

                self.speaker.speak(farewell)

                break

            response = self.brain.get_response(text)

            print(f"KALI : {response}")

            self.speaker.speak(response)

        print("\nKALI AI Stopped.")