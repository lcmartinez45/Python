#Lillian Martinez
#2/2/19

#Program Description: This program calculates the subtotal sale amount, the
#sales tax amount, and the total sale amount given the sales tax rate

#Declare Variables

firstItem  = 0.0
secondItem = 0.0
thirdItem  = 0.0
fourthItem = 0.0
fifthItem  = 0.0
salesTax   = 0.0
subtotal   = 0.0
totalSale  = 0.0

#Get Inputs

firstItem = float(input("Enter the amount of the first item: "))

secondItem = float(input("Enter the amount of the second item: "))

thirdItem = float(input("Enter the amount of the third item: "))

fourthItem = float(input("Enter the amount of the fourth item: "))

fifthItem = float(input("Enter the amount of the fifth item: "))

#Begin Processing

subtotal = firstItem + secondItem + thirdItem + fourthItem + fifthItem

salesTax = subtotal * .0825

totalSale = subtotal + salesTax

#Display Output

print("The subtotal sale amount is: ", format(subtotal, ".2f"))

print("The sales tax amount is: ", format(salesTax, ".2f"))

print("The total sale amount is: ", format(totalSale, ".2f"))
