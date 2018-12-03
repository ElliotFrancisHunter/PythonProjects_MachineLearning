# TODO here is a comment all caps todo places comment in todo section for easy reference
input_1 = input("Enter a number")  # Entered as strings
input_2 = input("Enter another number")

try:                         # try and catch statement, allows you to detect errors without crashing
    number_1 = int(input_1)  # Converts to type int
    number_2 = int(input_2)

    result = number_1 + number_2

    print("Result: ", result)  # comma is concatenation operator

except ValueError:
    print("One of the inputs NanN")


