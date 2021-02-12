# Lillian Martinez
# 4/14/19
# Program Description: This program opens an output file and reads numbers
# from the file, prints them, gets a total, and average.

def main():
    # Initialize Variables
    totalNum = 0.0

    numCount = 0

    averageNum = 0.0

    # Open a file numbers.txt
    outFile = open('numbers.txt', 'r')

    # Read the first line of the file.
    line = outFile.readline()

    print('Here are the numbers in the file:\n')

    while line != '':

        number = int(line)

        print(number)

        totalNum += number

        numCount += 1

        line = outFile.readline()  

    averageNum = totalNum / numCount

    outFile.close()

    print()

    print('The total of the numbers is: ', totalNum)

    print('The number of values read is: ', numCount)

    print('The average of the numbers in this file is: ', averageNum)

   
# Invoke main
main()
