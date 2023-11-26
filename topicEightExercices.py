#####################################################################################################################
# EXERCISE 1
#
# Create the file object. We use the open funtion to create a file named "outfile" and then we use the W parameter.
fileObject = open("outfile", "w")

# We create a loop to prompt the user to enter ten numbers.
for x in range(0, 10):
    userInput = input("Enter number: ")  # Get input from the user.
    # Write to the file "outfile" the numbers the user was prompted to enter in a manner of "Data: X".
    fileObject.write("Data: " + userInput + "\n")

# Write an additional line at the end when the loop finishes.
fileObject.write("This is the end of the data.")

# Close the file.
fileObject.close()

# An example of what the program will write to the file "outfile" if you run the program:
# Data: 2
# Data: 4
# Data: 8
# Data: 16
# Data: 32
# Data: 64
# Data: 128
# Data: 256
# Data: 512
# Data: 1024
# This is the end of the data.

#####################################################################################################################
# EXERCISE 2 and 3 together.
#
# Import the random integer function from the random module for later usage.
from random import randint

# A function that opens, reads as in prints to the console the contents and closes the practise3 file.
def filePrinter():
    fileObject = open("practise3", "r")  # Opens the file with the R parameter.
    print(fileObject.read())  # Prints the contents.
    fileObject.close()  # Closes it.


randomIntegers = []  # Define empty list called "randomIntegers".

for x in range(0, 5):  # Create a loop to run five times.
    # Append to the previously defined list five non-negative numbers ranging from 1 to 100 using the randint function.
    randomIntegers.append(randint(1, 100))

# Create the file object. We use the open function to create a file named "practise3" and then we use the W parameter.
fileObject = open("practise3", "w")

for number in randomIntegers:  # Iterate the list that now has five numbers in it.
    # Write to the file "practise3" the numbers the randint function generated in a manner of "Data: X".
    fileObject.write("Data: " + str(number) + "\n")
# Write an additional line at the end when the loop finishes.
fileObject.write("Finished.")
# Close the file.
fileObject.close()

# Call the "filePrinter()" function to read and print the contents of the "practise3" file.
filePrinter()

# An example of what the program will write to the file "practise3" if you run the program:
#
# Data: 40
# Data: 91
# Data: 76
# Data: 2
# Data: 25
# Finished.
