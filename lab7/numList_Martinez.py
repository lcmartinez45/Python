# Name: Lillian Martinez
# Date:04-21-19
# Program Description: design a program that asks the user to enter a series of 5 numbers.
# The program should store the numbers in a list and then display the lowest, highest,
# the total, and average of the numbers entered.

def main():

    print('Please enter 5 numbers below')

    print()
    
    values = getValues()

    getTotals(values)

# This function gets the values from the user to store in a list
def getValues():
    # Initialize Variables
    values = []

    for nums in range(5):

        numbers = int(input('Enter number '+ str(nums+1)+': '))

        values.append(numbers)
        
    print('\nThe numbers you selected are: ', values)
    
    return values

# This function calculates the minimum, maximum, sum, and average
# of the numbers in the list
def getTotals(values):

    print('The lowest number is: ', str(min(values)))

    print('The highest number is: ', str(max(values)))

    print('The sum of the numbers is: ', str(sum(values)))

    print('The average of all the numbers is: ', sum(values) / len(values))
          
main()
