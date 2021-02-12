#Lillian Martinez
#2/10/19

#Program Description: This program will determine a color based off of
#two primary colors.


#Declare Variables

primaryColor1 = " "

primaryColor2 = " "

#Get Inputs

primaryColor1 = input("Please enter the first primary color \
(Red, Blue, or Yellow) : ")

primaryColor2 = input("Please enter the second primary color \
(Red, Blue, or Yellow) : ")

#Determine the color

if (primaryColor1 == "Blue" and primaryColor2 == "Yellow") or \
   (primaryColor1 == "Yellow" and primaryColor2 == "Blue"):

    print("These two colors combined make PURPLE!")

elif (primaryColor1 == "Blue" and primaryColor2 == "Yellow") or \
   (primaryColor1 == "Yellow" and primaryColor2 == "Blue"):

    print("These two colors combined make GREEN!")

elif (primaryColor1 == "Red" and primaryColor2 == "Yellow") or \
   (primaryColor1 == "Yellow" and primaryColor2 == "Red"):

    print("These two colors combined make ORANGE!")

else:

    print("Invalid, at least one colored entered is not a primary color.")
