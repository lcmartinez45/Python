# Lillian Martinez
# Date: 4/7/19

# Program Description:This program determines the distance an object falls
# within a time period.

# Declare Constant
GRAVITY = 9.8

def main():
    
    # Declare Variables
    time = 0
    
    falling_distance(time)
    
    for time in range(5, 15):

        print('The object fell', format(falling_distance(time), '.01f'), 'meters in', time, 'sec(s)')

def falling_distance(time):
    # This function calculates the distance using the formula
    # d = 1/2 (gravity * time**2) using time as an argument and returning distance
    
    # Declare Variables
    distance = 0.0

    # Begin Processing
    distance = .5 * (GRAVITY * time**2)

    return distance

# Invoke main function
main()
