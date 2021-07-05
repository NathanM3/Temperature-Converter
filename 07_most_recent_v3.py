# Get data from user and store it in a list, then
# display the most recent three entries nicely
# Trial #3 - prints list in reverse order
# (no need for extra code or importing extra libraries)

# set up empty list
all_calculations = []

# Get five items of Data
for item in range(0, 5):
    get_item = input("Enter an item: ")

    # add item to start of 'list'
    all_calculations.append(get_item)

# Show that everything made it in to the list...
print()
print("*** The Full List ***")
print(all_calculations)

print()

print("*** Most Recent 3 ***")
for item in range(0, 3):
    print(all_calculations[len(all_calculations) - item - 1])
