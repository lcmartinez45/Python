#Lillian Martinez
#2/2/19

#Program Description: This program calculates your cars mileage per gallon

#Declare Variables

beginMileage  = 0.0
endMileage    = 0.0
milesTraveled = 0.0
gallonsUsed   = 0.0
milesPerGal   = 0.0

#Get Inputs

beginMileage = float(input("Enter the amount of the beginning mileage: "))

endMileage = float(input("Enter the amount of the ending mileage: "))

gallonsUsed = float(input("Enter the amount of gallons used for the trip: "))

#Begin Processing

milesTraveled = endMileage - beginMileage

milesPerGal = milesTraveled / gallonsUsed

#Display Output

print("The average miles per gallon is: ", format(milesPerGal, ".2f") )
