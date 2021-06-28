""" 04_Number_Checker_v1
Writing a number checker that I will apply to F - C and C - F
This number checker should only allow numbers that are above or equal to the
absolute zero value depending on the low value given to the function
"""


def temp_check(low):
    valid = False
    while not valid:
        try:
            response = float(input("Enter a number: "))
            if response < low:
                print("Too cold!")
            else:
                return response

        except ValueError:
            print("Please enter a number: ")


# Main Routine
# Set up to run this code twice (for two valid responses in test plan)
number = temp_check(-273)
print("You entered {}".format(number))

number = temp_check(-459)
print("You entered {}".format(number))
