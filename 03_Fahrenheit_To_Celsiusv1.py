""" Converting Fahrenheit to Celsius v1
Converting from degrees Fahrenheit to Celsius
Function takes in a value, does the conversion and puts answer into a list"""


def to_c(from_f):
    celsius = (from_f - 32) * 5/9
    if celsius
    return celsius


# Main Routine
temperatures = [0, 32, 100]
converted = []

for temp in temperatures:
    answer = to_c(temp)
    ans_statement = "{} degrees F is {} degrees C".format(temp, answer)
    converted.append(ans_statement)

print(converted)
