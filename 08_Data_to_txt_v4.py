# Source: https://www.quru99.com/reading-and-writing-files-in-python.html
# includes RegEx to check filename is valid (A-Z a-z 0-9 and underscores)
# checks if something is valid

import re

has_error = "yes"
while has_error == "yes":
    print()
    # Get filename, can't be blank / invalid
    filename = input("Enter a Filename: ")
    has_error = "no"

    valid_char = "[A-Za-z0-9_]"
    for letter in filename:
        if re.match(valid_char, letter):
            continue

        elif letter == " ":
            problem = "(no spaces allowed)"
        else:
            problem = ("(no {}'s allowed)".format(letter))
        has_error = "yes"

    if filename == "":
        problem = "can't be blank"
        has_error = "yes"

    if has_error == "yes":
        print("Invalid filename - {}".format(problem))
    else:
        print("You entered a valid filename")
