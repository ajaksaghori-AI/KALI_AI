import re


class CalculatorSkill:

    WORD_TO_NUMBER = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10,
        "eleven": 11,
        "twelve": 12,
        "thirteen": 13,
        "fourteen": 14,
        "fifteen": 15,
        "sixteen": 16,
        "seventeen": 17,
        "eighteen": 18,
        "nineteen": 19,
        "twenty": 20,
        "thirty": 30,
        "forty": 40,
        "fifty": 50,
        "sixty": 60,
        "seventy": 70,
        "eighty": 80,
        "ninety": 90,
        "hundred": 100
    }

    def words_to_numbers(self, text):
        words = text.lower().split()
        numbers = []

        i = 0
        while i < len(words):

            # Numeric digits
            if words[i].isdigit():
                numbers.append(float(words[i]))
                i += 1
                continue

            # Spoken numbers
            if words[i] in self.WORD_TO_NUMBER:

                value = self.WORD_TO_NUMBER[words[i]]

                # Example: twenty five
                if value >= 20 and value < 100:
                    if i + 1 < len(words) and words[i + 1] in self.WORD_TO_NUMBER:
                        next_value = self.WORD_TO_NUMBER[words[i + 1]]

                        if next_value < 10:
                            value += next_value
                            i += 1

                # Example: one hundred
                elif value < 10:
                    if i + 1 < len(words) and words[i + 1] == "hundred":
                        value *= 100
                        i += 1

                numbers.append(float(value))

            i += 1

        return numbers

    def calculate(self, text):

        text = text.lower()

        print(f"Calculator received: {text}")

        # Detect operator

        if "+" in text or "plus" in text or "add" in text:
           operator = "+"

        elif "-" in text or "minus" in text or "subtract" in text:
           operator = "-"

        elif "*" in text or "x" in text or "times" in text or "multiplied by" in text or "multiply" in text:
           operator = "*"

        elif "/" in text or "÷" in text or "divided by" in text or "divide" in text:
           operator = "/"

        else:
           return "I could not find a mathematical operation."


        # First look for digits
        digit_numbers = re.findall(r"\d+\.?\d*", text)

        if digit_numbers:
            numbers = list(map(float, digit_numbers))
        else:
            numbers = self.words_to_numbers(text)

        print(f"Numbers found: {numbers}")

        if len(numbers) != 2:
            return "I could not understand the calculation."

        num1, num2 = numbers

        if operator == "+":
            result = num1 + num2

        elif operator == "-":
            result = num1 - num2

        elif operator == "*":
            result = num1 * num2

        elif operator == "/":

            if num2 == 0:
                return "Division by zero is not allowed."

            result = num1 / num2

        if result.is_integer():
            result = int(result)

        return f"The answer is {result}."
