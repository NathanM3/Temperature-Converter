""" Converting Celsius to Fahrenheit v2
Converting from degrees Celsius to Fahrenheit
Function takes in a value, does the conversion and puts answer into a list
Addition of rounding values in case I there are numbers with lots of decimals
"""


def to_f(from_c):
    fahrenheit = from_c * 9/5 + 32
    if fahrenheit % 1 == 0:
        return int(fahrenheit)
    else:
        return round(fahrenheit, 1)


# Main Routine
temperatures = [0, 40, 100]
converted = []

for temp in temperatures:
    answer = to_f(temp)
    ans_statement = "{} degrees C is {} degrees F".format(temp, answer)
    converted.append(ans_statement)

print(converted)
