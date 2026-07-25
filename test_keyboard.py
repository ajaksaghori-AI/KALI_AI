from src.skills.keyboard_control_skill import KeyboardControlSkill
import time

keyboard = KeyboardControlSkill()

print("Switch to Notepad in 5 seconds...")

time.sleep(5)

print(keyboard.type_text("Hello from KALI AI"))

time.sleep(1)

print(keyboard.press_enter())

time.sleep(1)

print(keyboard.type_text("Keyboard Skill is working."))