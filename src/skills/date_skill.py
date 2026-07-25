from datetime import datetime


class DateSkill:

    def get_date(self):
        current_date = datetime.now().strftime("%d %B %Y")
        return f"Today's date is {current_date}."

    def get_day(self):
        current_day = datetime.now().strftime("%A")
        return f"Today is {current_day}."
