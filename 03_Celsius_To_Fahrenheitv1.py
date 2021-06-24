""" Converting Celsius to Fahrenheit v1
Converting from degrees Celsius to Fahrenheit
Function takes in a value, does the conversion and puts answer into a list"""


def to_f(from_c):
    fahrenheit = from_c * 9/5 + 32
    return fahrenheit


# Main Routine
temperatures = [0, 40, 100]
converted = []

for temp in temperatures:
    answer = to_f(temp)
    ans_statement = "{:.1f} degrees C is {:.1f} degrees F".format(temp, answer)
    converted.append(ans_statement)

print(converted)
