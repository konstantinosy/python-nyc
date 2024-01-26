# EXERCISE 1:
#
# The code is prompting the user to enter the grades for four quizzes. The grades are then stored in
# the variables quizGrade1, quizGrade2, quizGrade3 and quizGrade4.
quizGrade1 = int(input("Enter 1st Quiz Grade: "))
quizGrade2 = int(input("Enter 2nd Quiz Grade: "))
quizGrade3 = int(input("Enter 3rd Quiz Grade: "))
quizGrade4 = int(input("Enter 4th Quiz Grade: "))

# It calculates the average grade of the four quiz grades by adding up the grades stored
# in the variables and then dividing the sum by 4. The result is then printed to the console.
print("The average grade is:", (quizGrade1 + quizGrade2 + quizGrade3 + quizGrade4) / 4) 

#########################################################################################################
# EXERCISE 4:
#
# Prints a message to the console. Informs about the purpose of the program, which is to calculate 
# the result of the expression (x+y) * (x+y) using two numbers.
print("The program will run the expression (x+y) * (x+y) from the two numbers you will input.")

# Prompts the user to enter a value for X.
# Similar for Y.
x = int(input("Enter the value of X: ")) 
y = int(input("Enter the value of Y: ")) 

# Calculates the result of the expression (x + y) * (x + y).
print((x + y) * (x + y)) 

#########################################################################################################
# EXERCISE 6:
#
# Prompts the user to enter the length and width of a rectangle. The input() function is used
# to get user input and the int() function is used to convert to an integer data type. The entered values
# then are stored into their respective variables.
rectangleLength = int(input("Enter the length of the rectangle: ")) 
rectangleWidth = int(input("Enter the width of the rectangle: ")) 

# The two following lines of code calculate the perimeter and area of the rectangle using the previous
# input the user was prompted to enter.
perimeter = 2 * (rectangleLength + rectangleWidth) 
area = rectangleLength * rectangleWidth 

# Finally the program prints out the perimeter and the area of the rectangle.
print("The Perimeter is:", str(perimeter) + " and the Area is:", str(area))
