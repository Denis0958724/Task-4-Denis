import random


class Encryptor:
    def __init__(self, *numbers):

        self.__numbers = list(numbers)

        self.__result = None

    def __perform_operation(self):

        if len(self.__numbers) < 2:
            raise ValueError("Потрібно щонайменше два числа.")

        operation = random.choice(["add", "subtract", "multiply", "divide"])
        a, b = self.__numbers[0], self.__numbers[1]

        if operation == "add":
            self.__result = a + b
        elif operation == "subtract":
            self.__result = a - b
        elif operation == "multiply":
            self.__result = a * b
        elif operation == "divide":

            self.__result = a / b if b != 0 else "undefined"

        return operation

    def __str__(self):

        operation = self.__perform_operation()
        return f"Operation: {operation}, Result: {self.__result}"

    def add_number(self, number):

        self.__numbers.append(number)

    def get_numbers(self):

        return self.__numbers



encryptor = Encryptor(10, 5)
print(encryptor)
encryptor.add_number(20)
print("Stored numbers:", encryptor.get_numbers())