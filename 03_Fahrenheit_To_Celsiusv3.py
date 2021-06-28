""" Converting Fahrenheit to Celsius v3
Converting from degrees Fahrenheit to Celsius
Function takes in a value, does the conversion and puts answer into a list"""


def to_c(from_f):
    celsius = (from_f - 32) * 5/9
    # Method 1 of rounding numbers - checking if it has any decimals
    if celsius % 1 == 0:
        return int(celsius)
    else:
        return round(celsius, 1)


# Main Routine
temperatures = [0, 32, 100]
converted = []

for temp in temperatures:
    answer = to_c(temp)
    ans_statement = "{} degrees F is {} degrees C".format(temp, answer)
    converted.append(ans_statement)

print(converted)

