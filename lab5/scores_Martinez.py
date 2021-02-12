# Lillian Martinez
# Date: 4/7/19

# Program Description: This program will calculate a user's average grade based
# off of 5 scores entered. The program will display a letter grade,
# numeric grade, and average exam score and letter grade.

def main():

    # Variables

    score1 = 0.0
    score2 = 0.0
    score3 = 0.0
    score4 = 0.0
    score5 = 0.0
    
    print('Hello user, please enter 5 test scores below.\n')

    score1 = float(input('What is the score of your first exam? '))

    score2 = float(input('What is the score of your second exam? '))

    score3 = float(input('What is the score of your third exam? '))

    score4 = float(input('What is the score of your fourth exam? '))

    score5 = float(input('What is the score of your fifth exam? '))
    
    average = calc_average(score1, score2, score3, score4, score5)
    
    print('\nScore\tNumeric Grade\tLetter Grade \n')
    
    print('Score 1', '\t', format(score1, '.0f'), '\t\t', get_letter_grade(score1))

    print('Score 2', '\t', format(score2, '.0f'), '\t\t', get_letter_grade(score2))

    print('Score 3', '\t', format(score3, '.0f'), '\t\t', get_letter_grade(score3))

    print('Score 4', '\t', format(score4, '.0f'), '\t\t', get_letter_grade(score4))

    print('Score 5', '\t', format(score5, '.0f'), '\t\t', get_letter_grade(score5))

    print('\nAverage Score', '\t', format(average, '.1f'), '\t\t', get_letter_grade(average))

# This function will calculate the average of all 5 test scores and
# return the average.
def calc_average(score1, score2, score3, score4, score5):

    # Declare Variables
    average = 0.0
    
    average = (score1 + score2 + score3 + score4 + score5) / 5

    return average

# This function will take the argument grades and the average and determine
# what letter grade they are.
def get_letter_grade(score):

    if score >= 90 and score <= 100:

        score = 'A'

    elif score >= 80 and score <= 89.9:

        score = 'B'

    elif score >= 70 and score <= 79.9:

        score = 'C'

    elif score >= 60 and score <= 69.9:

        score = 'D'

    else:

        score = 'F'

    return score

# Invoke main function

main()

    

    
    

    

    
