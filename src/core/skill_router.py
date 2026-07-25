from src.skills.time_skill import TimeSkill
from src.skills.date_skill import DateSkill
from src.skills.calculator_skill import CalculatorSkill
from src.skills.weather_skill import get_weather
from src.skills.application_launcher import ApplicationLauncher
from src.skills.screenshot_skill import ScreenshotSkill
from src.skills.mouse_control_skill import MouseControlSkill
from src.skills.keyboard_control_skill import KeyboardControlSkill


class SkillRouter:

    def __init__(self):

        self.time_skill = TimeSkill()
        self.date_skill = DateSkill()
        self.calculator_skill = CalculatorSkill()

        self.application_launcher = ApplicationLauncher()

        self.screenshot_skill = ScreenshotSkill()

        self.mouse_skill = MouseControlSkill()

        self.keyboard_skill = KeyboardControlSkill()

    def execute(self, text):

        text = text.lower().strip()

        # ==================================================
        # Application Launcher
        # ==================================================

        if text.startswith("open"):

            response = self.application_launcher.open_application(text)

            if response:
                return response

        # ==================================================
        # Screenshot Skill
        # ==================================================

        if (
            "screenshot" in text
            or "screen shot" in text
            or "capture" in text
        ):

            return self.screenshot_skill.take_screenshot()

        # ==================================================
        # Mouse Skill
        # ==================================================

        if (
            "center" in text
            or "centre" in text
            or "middle" in text
        ):

            return self.mouse_skill.move_mouse("center")

        elif "top left" in text:

            return self.mouse_skill.move_mouse("top left")

        elif "top right" in text:

            return self.mouse_skill.move_mouse("top right")

        elif "bottom left" in text:

            return self.mouse_skill.move_mouse("bottom left")

        elif "bottom right" in text:

            return self.mouse_skill.move_mouse("bottom right")

        elif text == "click":

            return self.mouse_skill.click_mouse()

        elif (
            text == "double"
            or "double click" in text
            or "double tap" in text
        ):

            return self.mouse_skill.double_click_mouse()

        elif (
            text == "right"
            or "right click" in text
            or "right button" in text
        ):

            return self.mouse_skill.right_click_mouse()

        # ==================================================
        # Keyboard Skill
        # ==================================================

        elif text.startswith("type "):

            typing_text = text.replace("type ", "", 1)

            return self.keyboard_skill.type_text(typing_text)

        elif text == "enter":

            return self.keyboard_skill.press_enter()

        elif text == "tab":

            return self.keyboard_skill.press_tab()

        elif text == "escape":

            return self.keyboard_skill.press_escape()

        elif text == "backspace":

            return self.keyboard_skill.press_backspace()

        elif text == "delete":

            return self.keyboard_skill.press_delete()

        elif text == "copy":

            return self.keyboard_skill.copy()

        elif text == "paste":

            return self.keyboard_skill.paste()

        elif text == "cut":

            return self.keyboard_skill.cut()

        elif text == "select all":

            return self.keyboard_skill.select_all()

        elif text == "undo":

            return self.keyboard_skill.undo()

        elif text == "redo":

            return self.keyboard_skill.redo()

        elif text == "save":

            return self.keyboard_skill.save()

        # ==================================================
        # Weather Skill
        # ==================================================

        elif "weather" in text or "temperature" in text:

            city = "Bangalore"

            if " in " in text:
                city = text.split(" in ")[-1].strip().title()

            return get_weather(city)

        # ==================================================
        # Calculator Skill
        # ==================================================

        calculator_keywords = [
            "calculate",
            "plus",
            "add",
            "+",
            "minus",
            "subtract",
            "-",
            "times",
            "multiply",
            "multiplied",
            "*",
            "x",
            "divide",
            "divided",
            "/"
        ]

        if any(word in text for word in calculator_keywords):

            return self.calculator_skill.calculate(text)

        # ==================================================
        # Time Skill
        # ==================================================

        elif "time" in text:

            return self.time_skill.get_time()

        # ==================================================
        # Date Skill
        # ==================================================

        elif "date" in text:

            return self.date_skill.get_date()

        # ==================================================
        # Day Skill
        # ==================================================

        elif "day" in text:

            return self.date_skill.get_day()

        # ==================================================
        # No Skill Found
        # ==================================================

        return None