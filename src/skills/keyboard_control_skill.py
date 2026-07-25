import pyautogui


class KeyboardControlSkill:

    def type_text(self, text):

        try:
            pyautogui.write(text, interval=0.05)
            return f"Typed: {text}"

        except Exception as e:
            return f"Unable to type text. Error: {e}"

    def press_enter(self):

        try:
            pyautogui.press("enter")
            return "Enter key pressed."

        except Exception as e:
            return f"Unable to press Enter. Error: {e}"

    def press_tab(self):

        try:
            pyautogui.press("tab")
            return "Tab key pressed."

        except Exception as e:
            return f"Unable to press Tab. Error: {e}"

    def press_escape(self):

        try:
            pyautogui.press("esc")
            return "Escape key pressed."

        except Exception as e:
            return f"Unable to press Escape. Error: {e}"

    def press_backspace(self):

        try:
            pyautogui.press("backspace")
            return "Backspace key pressed."

        except Exception as e:
            return f"Unable to press Backspace. Error: {e}"

    def press_delete(self):

        try:
            pyautogui.press("delete")
            return "Delete key pressed."

        except Exception as e:
            return f"Unable to press Delete. Error: {e}"

    def copy(self):

        try:
            pyautogui.hotkey("ctrl", "c")
            return "Copied."

        except Exception as e:
            return f"Unable to copy. Error: {e}"

    def paste(self):

        try:
            pyautogui.hotkey("ctrl", "v")
            return "Pasted."

        except Exception as e:
            return f"Unable to paste. Error: {e}"

    def cut(self):

        try:
            pyautogui.hotkey("ctrl", "x")
            return "Cut completed."

        except Exception as e:
            return f"Unable to cut. Error: {e}"

    def select_all(self):

        try:
            pyautogui.hotkey("ctrl", "a")
            return "Selected all."

        except Exception as e:
            return f"Unable to select all. Error: {e}"

    def undo(self):

        try:
            pyautogui.hotkey("ctrl", "z")
            return "Undo completed."

        except Exception as e:
            return f"Unable to undo. Error: {e}"

    def redo(self):

        try:
            pyautogui.hotkey("ctrl", "y")
            return "Redo completed."

        except Exception as e:
            return f"Unable to redo. Error: {e}"

    def save(self):

        try:
            pyautogui.hotkey("ctrl", "s")
            return "Saved."

        except Exception as e:
            return f"Unable to save. Error: {e}"