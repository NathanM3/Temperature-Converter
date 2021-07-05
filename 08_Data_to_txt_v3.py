# Source: https://www.quru99.com/reading-and-writing-files-in-python.html

import re

# Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, can't be blank / invalid
# assume valid data for now.
filename = input("Enter a Filename: ")

valid_file = "[A-Zaz]"
if re.match(valid_file, filename):
    # add .txt suffix!
    filename = filename + ".txt"

    # create file to hold data

    f = open(filename, "w+")

    for item in data:
        f.write(item + "\n")

    # close file
    f.close()

else:
    print("oops!")
