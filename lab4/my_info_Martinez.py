# Name: Lillian Martinez

# Date: 3-30-19

# Program description: This program will gather and print information from
# a user.


def main():

    # Declare Variables
    first = ''
    last = ''
    address = ''
    major = ''
    
    # Get the users information below
    print('Hello user we are going to gather some information \
from you, please answer the questions below.')

    print()

    first = input('What is your first name? ')

    last = input('What is your last name? ')

    address = input('What is your address? ')

    major = input('Lastly, what is your major? ')

    print()
    
    # Invoke the print_name function
    print_name(first, last)
    
    # Invoke the print_address function
    print_address(address)

    # Invoke the print_major function
    print_major(major)

    print()
    
    print('Thank you for your time your information is complete, have a good day!')

def print_name(first, last):

    print('Your name is: ', first, last)


def print_address(address):

    print('Your address is: ', address)


def print_major(major):

    print('Your major is: ', major)


main()

    

    
