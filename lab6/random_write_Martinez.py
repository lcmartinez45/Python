# Lillian Martinez
# Date: 4/14/19

# Program Description: This program writes a series of numbers to a file while
# letting the user pick how many lines to enter in that file.

import random

def main():

    # Open a file to write to.
    outFile = open('numbers.txt', 'w')
    
    for count in range(int(input('How many random numbers in the file? '))):

        line = str(random.randint(1,20))

        outFile.write(line + '\n')

    outFile.close()

    print('The information was written into numbers.txt')

# Invoke the main function
main()

