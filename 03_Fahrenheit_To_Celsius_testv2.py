""" Converting Fahrenheit to Celsius v2
Converting from degrees Fahrenheit to Celsius
Function takes in a value, does the conversion and puts answer into a list
Testing different ways of rounding that I can apply to both parts of comp 3
"""


def to_c(from_f):
    celsius = (from_f - 32) * 5/9
    # Method 1 of rounding numbers - checking if it has any decimals
    if celsius % 1 == 0:
        return int(celsius)
    else:
        return round(celsius, 1)


def to_c_round_v2(from_f):
    celsius = (from_f - 32) * 5/9
    # Method 2 of rounding numbers - sending them into a formatted string
    if celsius % 1 == 0:
        return "{:.0f}".format(celsius)
    else:
        return "{:.1f}".format(celsius)


# Main Routine
temperatures = [0, 32, 100]
converted = []
converted2= []

for temp in temperatures:
    answer = to_c(temp)
    answer2 = to_c_round_v2(temp)
    ans_statement = "{} degrees F is {} degrees C".format(temp, answer)
    ans_statement2 = "{} degrees F is {} degrees C".format(temp, answer2)
    converted.append(ans_statement)
    converted2.append(ans_statement2)

print(converted)
print(converted2)
