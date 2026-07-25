from datetime import datetime


class TimeSkill:

    def get_time(self):
        current_time = datetime.now().strftime("%I:%M %p")
        return f"The current time is {current_time}."