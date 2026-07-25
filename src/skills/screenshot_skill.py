import os
from datetime import datetime

import pyautogui


class ScreenshotSkill:

    def take_screenshot(self):

        try:
            project_root = os.path.abspath(
                os.path.join(os.path.dirname(__file__), "..", "..")
            )

            screenshot_folder = os.path.join(project_root, "screenshots")

            os.makedirs(screenshot_folder, exist_ok=True)

            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

            filename = f"screenshot_{timestamp}.png"

            filepath = os.path.join(screenshot_folder, filename)

            screenshot = pyautogui.screenshot()

            screenshot.save(filepath)

            return f"Screenshot saved successfully as {filename}."

        except Exception as e:
            return f"Unable to take screenshot. Error: {e}"