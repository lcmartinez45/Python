# Lillian Martinez
# 4/14/19
# Program Description: This program opens an output file, writes your name,
# address, and phone number to the file, then closes the file.

def main():
    print('Are you ready to write? Please answer the questions below. ')

    # Open a file named info.txt
    outFile = open('info.txt', 'w')

    #Get the information.
    userName = input('What is your name?: ')
    
    userAddress = input('What is your address?: ')
    
    userNumber = input('What is your telephone number?: ')
    
    #Write the information to the file.
    outFile.write(userName + '\n')

    outFile.write(userAddress + '\n')

    outFile.write(userNumber + '\n')

    # Close the file.
    outFile.close()

    print('We are all done thank you.')

# Invoke main function.
main()
