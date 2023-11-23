###############################################################################################################################
#
# TOPIC 5 - EXERCISE 1.
# 
# We define two lists
firstList = ["Ten", "Twenty", "Thirty"]
secondList = [10, 20, 30]

# We create a dictionary using the built-in dict() function and then we use the zip() function to pair the first list with the
# second one to get the appropriate keys and values.
print(dict(zip(firstList, secondList)))
###############################################################################################################################
#
# TOPIC 5 - EXERCISE 2.
#
# We define two lists.
firstList = [3, 6, 9, 12, 15, 18, 21]
secondList = [4, 8, 12, 16, 20, 24, 28]


# Start at index [1] and skips every other one to get the odd-indexed.
oddIndexedFirstList = firstList[1::2]
# Starts at index [0] and skips every other one to get the even-indexed.
oddIndexedSecondList = secondList[0::2]
# Combine the two lists together.
finalList = oddIndexedFirstList + oddIndexedSecondList

print("Elements with odd-index from first list are:", oddIndexedFirstList)
print("Elements with odd-index from second list are:", oddIndexedSecondList)
print("Third list is: ", finalList)
###############################################################################################################################
#
# TOPIC 5 - EXERCISE 3.
#
# Define a list with nine numbers.
sample_list = [11, 45, 8, 12, 15, 18, 7, 4, 15]

# Print each equally sliced list.
print("First list is:", sample_list[0:3])
print("Second list is:", sample_list[3:6])
print("Third list is:", sample_list[6:9])
###############################################################################################################################
#
# TOPIC 5 - EXERCISE 4.
#
# Almost the same as the first exercise. The only things that change are that we use the tuple function instead of the
# dict one and we add a list function in the beggining to include the tuples in a list.
# Define two lists.
firstList = [2, 3, 4, 5, 6, 7, 8]
secondList = [4, 9, 16, 25, 36, 49, 64]

# Prints a list of zipped tuples using the zip() function to combine the values from the two previously defined lists.
print(list(tuple(zip(firstList, secondList))))
###############################################################################################################################
#
# TOPIC 5 - EXERCISE 8.
#
# We define a sample list with eight values.
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]

# We use the max and min functions to find the appropriate values.
print("Max value is:", (max(sample_list)))
print("Min value is:", (min(sample_list)))
###############################################################################################################################
#
# TOPIC 6 EXERCISE.
#
from statistics import mean  # import mean function from statistics module.

# We define a function that takes two parameters. Weight and Height.
# The function runs the formula to figure out the BMI(Body mass index).
# Then it appends that value to a list.
# It also returns a string of characters depending on the BMI that was previously calculated.


def bmiCalculator(weight, height):
    bmi = weight / height**2
    averageList.append(bmi)
    if bmi >= 0 and bmi <= 18.5:
        print("You are underweight.")
    elif bmi >= 18.5 and bmi <= 25:
        print("You are normal.")
    elif bmi >= 25 and bmi <= 30:
        print("You are overweight.")
    else:
        print("You are obese.")


averageList = []  # Define empty list called 'averageList'.
print("To quit press 00 at the height prompt.")

while True:  # Define an endless loop.
    # Prompts the user to enter the height. The input is in str so if the user enters '00' as input the program will stop. Later it gets converted into a floating type so we can check if the numbers the user is inputting are valid.
    heightUserInput = (input("Enter your height in meters: "))
    # If the user enters the string of text "00" the loop breaks and the program ends.
    if heightUserInput == '00':
        break
    # The 'heightUserInput' is converted into a float.
    heightUserInput = float(heightUserInput)
    # Prompts the user to enter the weight.
    weightUserInput = float(input("Enter your weight in kilograms: "))
    # If one of the two variables contain a 0 or a negative number the program asks you to re enter the numbers.
    if heightUserInput <= 0 or weightUserInput <= 0:
        print("Enter some valid numbers please...")
        continue
    else:
        # We call the 'bmiCalculator' function with the previously defined variables as arguments to inform the user about the BMI result.
        bmiCalculator(weight=weightUserInput, height=heightUserInput)
        # Lastly we call the mean function to calculate the average we have so far.
        print("The average of all the BMI's combined is:", mean(averageList))
