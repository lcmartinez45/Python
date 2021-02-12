# Lillian Martinez
# Date: 4/14/19

# Program Description: This program will calculate a user's average grade based
# off of 5 scores entered. The program will display a letter grade,
# numeric grade, and average exam score and letter grade.

from grades_Martinez import *

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


# Invoke main function

main()

    
