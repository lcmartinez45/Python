# Lillian Martinez
# Date: 4/7/19

# Program Description:This program will calculate the time in seconds a vehicle
# would require to reach final velocity. 

def main():

    # Declare Variables
    time = 0.0

    initVelocity = get_initial_velocity()

    finVelocity = get_final_velocity()

    acceleration = get_acceleration()

    time = (finVelocity - initVelocity) / acceleration

    print('\nThe vehicle requires', time, 'seconds to reach final velocity.')

def get_initial_velocity():
    # This function gets the initial velocity from the user and returns the value
    
    # Declare Variables
    initVelocity = 0.0

    initVelocity = float(input('\nWhat is the initial velocity? '))

    return initVelocity

def get_final_velocity():
    # This function gets the final velocity from the user and returns the value
    
    # Declare Variables
    finVelocity = 0.0

    finVelocity = float(input('What is the final velocity? '))

    return finVelocity    

def get_acceleration():
    # This function gets the acceleration from the use and returns the value

    # Declare Variables
    acceleration = 0.0
    
    acceleration = float(input('What is the acceleration? '))

    return acceleration

# Invoke main function
main()
    
