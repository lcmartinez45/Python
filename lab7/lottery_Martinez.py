# Name: Lillian Martinez
# Date:04-21-19
# Program Description: This program generates a five-digit lottery number each
# in the range 1 through 40 and assigns each number to a list element then 
# displays the list in the format of a lottery number

from random import *

def main():
    # Initialize Variables
    numbers = []
    lotteryNum = 0

    for number in range(5):

        lotteryNum = int(randint(1, 41))

        numbers.append(lotteryNum)

    print('Hello here are your individual lottery numbers:\n ')

    index = 0
    
    while index < len(numbers):

        print(numbers[index])

        index += 1

    print()

    print('Your list of lottery numbers: ', numbers)

main()
