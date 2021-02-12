# Lillian Martinez
# 4/14/19
# Program Description: This program opens an output file and reads numbers
# from the file and calculates the average.

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

        try: 

            number = int(line)

            print(number)

            totalNum += number

            numCount += 1

        except IOError:

            print('An error occured trying to read the file. ')

        except ValueError:

            print('Non-numeric data found in the file. ')

        except:

            print('An error occured. ')

        line = outFile.readline()

    averageNum = totalNum / numCount

    outFile.close()

    print('\nThe average of the numbers in this file is: ', averageNum)
 
# Invoke main
main()
