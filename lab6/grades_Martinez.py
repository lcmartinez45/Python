# Lillian Martinez
# Date: 4/14/19

# Program Description:This function will calculate the average of all 5 test scores and
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
