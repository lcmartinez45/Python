# Lillian Martinez
# 3-30-19

# Program Description:

# Declare Global Constants

LEVEL_ONE_COST   = 75

LEVEL_TWO_COST   = 65

LEVEL_THREE_COST = 55

LEVEL_FOUR_COST  = 35

LEVEL_FIVE_COST  = 15

LEVEL_SIX_COST   = 10.50

def main():

    # Declare Variables
    level_one   = 0
    level_two   = 0
    level_three = 0
    level_four  = 0
    level_five  = 0
    level_six   = 0
    
    t1 = 0
    t2 = 0
    t3 = 0
    t4 = 0
    t5 = 0
    t6 = 0
    
    total_tickets = 0
    
    # Get Inputs
    level_one = int(input('How many Level 1 tickets were purchased?: '))

    while level_one < 0:

                    level_one = int(input('Please enter a valid number of \
Level 1 tickets purchased.: '))

    t1 = LEVEL_ONE_COST * level_one
    
    
    level_two = int(input('How many Level 2 tickets were purchased?: '))

    while level_two < 0:

                    level_two = int(input('Please enter a valid number of \
Level 2 tickets purchased.: '))

    t2 = LEVEL_TWO_COST * level_two

    
    level_three = int(input('How many Level 3 tickets were purchased?: '))

    while level_three < 0:

                    level_three = int(input('Please enter a valid number of \
Level 3 tickets purchased.: '))

    t3 = LEVEL_THREE_COST * level_three
    
    
    level_four = int(input('How many Level 4 tickets were purchased?: '))

    while level_four < 0:

                    level_four = int(input('Please enter a valid number of \
Level 4 tickets purchased.: '))

    t4 = LEVEL_FOUR_COST * level_four


    level_five = int(input('How many Level 5 tickets were purchased?: '))

    while level_five < 0:

                    level_five = int(input('Please enter a valid number of \
Level 5 tickets purchased.: '))

    t5 = LEVEL_FIVE_COST * level_five

    
    level_six = int(input('How many Level 6 tickets were purchased?: '))

    while level_six < 0:

                    level_six = int(input('Please enter a valid number of \
Level 6 tickets purchased.: '))

    t6 = LEVEL_SIX_COST * level_six

    # Invoke display_income function
    display_income(t1, t2, t3, t4, t5, t6)

# Display the amount of income from ticket sales for each level, calculate, 
# and display the total ticket sales for all levels combined

def display_income(t1, t2, t3, t4, t5, t6):

    # Declare Variables
    total_tickets = 0.0
    print()
    
    print('Level 1 income from sales is $' , format(t1, ".2f"))

    print('Level 2 income from sales is $' , format(t2, ".2f"))

    print('Level 3 income from sales is $' , format(t3, ".2f"))

    print('Level 4 income from sales is $' , format(t4, ".2f"))

    print('Level 5 income from sales is $' , format(t5, ".2f"))

    print('Level 6 income from sales is $' , format(t6, ".2f"))

    total_tickets = t1 + t2 + t3 + t4 + t5 + t6

    print()

    print('The total number of ticket sales is $', format(total_tickets, ".2f"))

# Invoke the main function

main()
