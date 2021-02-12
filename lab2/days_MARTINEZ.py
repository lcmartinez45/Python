#Lillian Martinez
#2/10/19

#Program Description: This program will determine a day of the week based on
#a cooresponding number for that day.

#Declare Constants

MONDAY    = 1
TUESDAY   = 2
WEDNESDAY = 3
THURSDAY  = 4
FRIDAY    = 5
SATURDAY  = 6
SUNDAY    = 7

#Declare Variables

number = 0.0

#Get Inputs

number = int(input("Please enter a number between the range 1 through 7: "))

#Determine the day of the week

if number == 1:

    print("Monday")

elif number == 2:
    
    print("Tuesday")

elif number == 3:

    print("Wednesday")

elif number == 4:

    print("Thurday")

elif number == 5:

    print("Friday")

elif number == 6:

    print("Saturday")

elif number == 7:

    print("Sunday") 

else:

    print("Error, invalid number outside of number range.")

