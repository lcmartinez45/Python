#Lillian Martinez
#2/2/19

#Program Description: This program converts Celsius temperatures to Fahrenheit
#temperatures.

#Declare Variables

fahrenheit = 0.0
celsius    = 0.0

#Get Inputs

celsius = float(input("Enter a temperature in Celsius: "))

#Begin Processing

fahrenheit = (celsius * 9 / 5) + 32

#Display Output

print("The temperature in Fahrenheit is: ", format(fahrenheit, ".2f") )
