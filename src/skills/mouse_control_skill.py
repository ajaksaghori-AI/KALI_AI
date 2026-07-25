import pyautogui


class MouseControlSkill:

    def move_mouse(self, position):

        try:

            screen_width, screen_height = pyautogui.size()

            positions = {

                "center": (
                    screen_width // 2,
                    screen_height // 2
                ),

                "top left": (
                    50,
                    50
                ),

                "top right": (
                    screen_width - 50,
                    50
                ),

                "bottom left": (
                    50,
                    screen_height - 50
                ),

                "bottom right": (
                    screen_width - 50,
                    screen_height - 50
                )
            }


            if position in positions:

                x, y = positions[position]

                pyautogui.moveTo(
                    x,
                    y,
                    duration=1
                )

                return f"Mouse moved to {position}."


            return "I don't know that mouse position."


        except Exception as e:

            return f"Unable to move mouse. Error: {e}"



    def click_mouse(self):

        try:

            pyautogui.click()

            return "Mouse click completed."


        except Exception as e:

            return f"Unable to click mouse. Error: {e}"



    def double_click_mouse(self):

        try:

            pyautogui.doubleClick()

            return "Double click completed."


        except Exception as e:

            return f"Unable to double click mouse. Error: {e}"



    def right_click_mouse(self):

        try:

            pyautogui.rightClick()

            return "Right click completed."


        except Exception as e:

            return f"Unable to right click mouse. Error: {e}"