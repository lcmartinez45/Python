# Lillian Martinez
# 3/2/19

# Program Description: This program will display the number of calories burned
# after 10, 15, 20, 25, and 30 minutes in a table format.

# Declare Constant:

calories = 4.2

# Declare Variables:

caloriesBurned = 0

minutes = 10

print("I will display a table of the number of calories burned after \
10, 15, 20, 25, and 30 minutes")


# Print the table headings

print()

print("Minutes\tCalories")

print("------------------")


# Begin loop and print the number of minutes running and the amount of
# calories burned.

while minutes <= 30: # Condition we are testing

    caloriesBurned = calories * minutes

    print(minutes, '\t', format(caloriesBurned, '.0f'))

    minutes = minutes + 5 # Stopping Code 

