# Source: https://www.quru99.com/reading-and-writing-files-in-python.html

# Data to be outputted
data = ['first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh']

# Get filename, can't be blank / invalid
# assume valid data for now.
filename = input("Enter a Filename: ")

# create file to hold data

f = open(filename, "W+")

for item in data:
    f.write(item)

# close file
f.close()
