from src.core.skill_router import SkillRouter


class ConversationEngine:

    def __init__(self):
        self.router = SkillRouter()

    def get_response(self, text):

        # First, let the Skill Router try
        skill_response = self.router.execute(text)

        if skill_response:
            return skill_response

        text = text.lower().strip()

        if "hello" in text or "hi" in text:
            return "Hello Chaitanya! How can I help you today?"

        elif "your name" in text:
            return "I am KALI AI, your personal AI assistant."

        elif "how are you" in text:
            return "I am doing great. Thank you for asking."

        elif "thank you" in text or "thanks" in text:
            return "You're welcome."

        elif text in ["bye", "exit", "quit", "stop"]:
            return "Goodbye. Have a wonderful day."

        return "Sorry, I don't know how to answer that yet."
