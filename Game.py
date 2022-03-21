import random


class ValueTooSmallError(Exception):
    def __init__(self):
        message = "Value is too small"
        super().__init__(message)


class ValueTooLargeError(Exception):
    def __init__(self):
        message = "value is too large"
        super().__init__(message)


my_lucky_value = random.randrange(100)
while True:
    try:
        number = int(input(f"Insert a number: "))
        if number > my_lucky_value:
            raise ValueTooLargeError()
        elif number < my_lucky_value:
            raise ValueTooSmallError()
        break
    except ValueTooLargeError as e:
        print(e)
    except ValueTooSmallError as e:
        print(e)
    except ValueError:
        print("Please insert an integer!")

print(f"Great! You guessed it, {my_lucky_value} is the correct number!")
