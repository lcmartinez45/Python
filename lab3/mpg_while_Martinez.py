#Lillian Martinez
#3/2/19

#Program Description: This program calculates your cars mileage per gallon
#as long as a valid beginning mileage is entered

#Declare Variables

beginMileage  = 0.0
endMileage    = 0.0
milesTraveled = 0.0
milesPerGal   = 0.0
gallonsUsed   = 0.0

# Get Inputs

beginMileage = float(input("Enter the amount of the beginning mileage: "))

#Loop to enter destinations

while beginMileage >= 1:

        endMileage = float(input("Enter the amount of the ending mileage: "))

        gallonsUsed = float(input("Enter the amount of gallons used for the trip: "))

        milesTraveled = endMileage - beginMileage #Begin Processing
    
        milesPerGal = milesTraveled / gallonsUsed

        print("The average miles per gallon is: ", format(milesPerGal, ".2f"))

        beginMileage = float(input("Enter the amount of the beginning mileage: "))

print("You have entered an invalid beginning mileage")
