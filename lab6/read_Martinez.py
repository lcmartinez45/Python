# Lillian Martinez
# 4/14/19
# Program Description: This program opens an output file, reads your name,
# address, and phone number from the file, then displays them to the screen.

def main():

    # Open a file names info.txt
    inFile = open('info.txt', 'r')

    # Read the three lines from the file.
    contents1 = inFile.readline()  
    contents2 = inFile.readline()
    contents3 = inFile.readline() 

    # Strip the \n from each string.
    contents1 = contents1.rstrip('\n')  
    contents2 = contents2.rstrip('\n')
    contents3 = contents3.rstrip('\n')

    # Close the file.
    inFile.close() 

    # Print the data that was read into memory.
    print(contents1)
    print(contents2)
    print(contents3)

#invoke main
main()
