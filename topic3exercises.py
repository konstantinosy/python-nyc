# EXERCISE 3
#
# Takes user input for three different temperatures and stores them into their respective variables.
# The float() function is used to convert the input into a floating-point number.
firstTemp = float(input("Enter first obtained tempereture: "))
secondTemp = float(input("Enter second obtained tempereture: "))
thirdTemp = float(input("Enter third obtained tempereture: "))

# It calculates the average temperature by adding the previous three variables and dividing the sum by 3.
# The result then is stored in the variable named "avgTemp".
avgTemp = (firstTemp + secondTemp + thirdTemp) / 3

# This line of code prints the average temperature calculated in the previous line of code.
print("Average temperature is: ", firstTemp + secondTemp + thirdTemp / 3, "°C")

# This is a conditional statement that checks if the average temperature is greater than 35. If the 
# condition is true, it will execute the code block inside the if statement which prints the string "Heat".
if avgTemp > 35:
    print("Heat")

#################################################################################################################
# EXERCISE 4
#
# Aks the user to enter a value for the sound level and stores that value in the variable "soundLevel". We use
# the input() function to get input from the user and the int() function to convert to an integer data type.
soundLevel = int(input("Enter the sound level in dB: "))

# The code uses conditional statements to determine the sound source based on the value of the variable.
if soundLevel == 130:
    print("Jackhammer")

elif soundLevel == 106:
    print("Gas lawnmower")

elif soundLevel == 70:
    print("Alarm Clock")

elif soundLevel == 40:
    print("Quite Room")