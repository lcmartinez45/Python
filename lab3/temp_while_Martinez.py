# Lillian Martinez
# 3/2/19

# Program Description: This program uses a loop to convert Celsius temperatures
# to Fahrenheit temperatures in a range from 0 to 20 and will display
# output in a form of a table.

#Declare Variables

fahrenheit  = 0
celsius     = 0


print("I will display a table of tempertaures in Fahrenheit and Celsius \
in a range from 0 to 20")


# Print the table headings

print()

print("Celsius\tFahrenheit")

print("------------------")


# Begin loop and print the Celsius range 0 to 20 and coverted Fahrenheit

while celsius < 21: # Condition we are testing

    fahrenheit = (celsius * 9 / 5) + 32

    print(celsius, '\t', format(fahrenheit, '.0f'))

    celsius = celsius + 1 # Stopping Code 


    



