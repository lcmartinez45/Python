# Name: Lillian Martinez
# Date:04-21-19
#Program Description: This program creates a two-dimensional list with 3 rows
# and 3 columns and displays each element in the list and their sums.

ROWS = 3

COLS = 3

def main():
    # Initialize Variables
    row0 = []
    row1 = []
    row2 = []
    col0 = []
    col1 = []
    col2 = []
    
    values = [[0,0,0],
              [0,0,0],
              [0,0,0]]
    print('Please enter nine numbers for the table:')
    
    for numberRow in range(ROWS):

        for numberCol in range(COLS):
            
            values[numberRow][numberCol] = int(input('Number: '))
    
    print('Your list of numbers are: ', values)

    add_rows(values)

    add_cols(values)
    
# This function gets the sum of rows
def add_rows(values):
    # Initialize Variables
    rowSum = 0
    
    for row in values:

        for elem in row:

            rowSum += elem

    print('Sum for rows is: ', rowSum)

# This function gets the sum of columns
def add_cols(values):
    # Initialize Variables
    colSum = 0
    
    for col in values:

        for elem in col:

            colSum += elem

    print('Sum for the columns is: ', colSum)

main()
