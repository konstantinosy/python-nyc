# EXERCISE 1
#
# The code prompts the user to enter the number of years the company is in operation and
# the number of workers in the company. It converts the input to integers and asssigns them
# to their respective variables.
# Then it determines the allowance for the employer based on how many years the company exists and how many
# workers are employed.
for x in range(0, 3):
    yearsOfOperation = int(input("Enter the years of operation: "))
    numOfEmployees = int(input("Enter how many workers are in the company: "))
    if yearsOfOperation >= 1 and yearsOfOperation <= 9:
        if numOfEmployees == 1:
            print("The allowanced to the employer will be 50 euros!")
        elif numOfEmployees == 2 or numOfEmployees == 3:
            print("The allowance to the employer will be 70 euros!")
        elif numOfEmployees >= 3:
            print("The allowance to the employer will be 100 euros!")
        
    elif yearsOfOperation >= 10:
        if numOfEmployees == 1:
            print("The allowance to the employer will be 60 euros!")
            
        elif numOfEmployees == 2 or numOfEmployees == 3:
            print("The allowance to the employer will be 80 euros!")
            
        elif numOfEmployees >= 3:
            print("The allowance to the employer will be 120 euros!")

#######################################################################################################################
# EXERCISE 2
#
# Import the mean function for later usage.
from statistics import mean

# Define empty list name "gradesList".
gradesList = []

# This code is creating a loop that will continue indefinitely until a specific condition is met.
# If the first input is a 0 it will display you an error message promting you again to input a valid number/grade.
# On the other hand if the list is not empty the program will print you the mean value while exiting.
while True:
    gradeInput = int(input("Enter grade: "))
    if gradeInput == 0 and gradesList == []:
        print("First value cannot be 0 / zero.")
        continue
    
    gradesList.append(gradeInput)
    if gradeInput == 0 and gradesList != []:
        print("The average is:", mean(gradesList))
        break   

#######################################################################################################################
# EXERCISE 3
#
# Import the mean function for later usage.
from statistics import mean 

gradesList = [] # Define an empty list called gradesList.

# We create a loop of 10 iterations. It prompts the user to enter a grade while checking the validity to be between 0 and 10.
for x in range(0, 10):
    gradeInput = float(input("Enter grade: "))
    if gradeInput >= 0 and gradeInput <=10:
        gradesList.append(gradeInput)
    else:
        print("Invalid input. Input must be 0 to 10.")
        break

# Prints the max, min and mean values of the list.
print("Highest grade was: ", max(gradesList))
print("Lowest grade was: ", min(gradesList))
print("The average is:", mean(gradesList))

# Iterates the list to grab the student(s) who achieved at lest 8.5 grade score.
for x in gradesList:
    if x >= 8.5:
        print("The following student(s) got excellent grade(s): ", x, ".")

#######################################################################################################################
# EXERCISE 4
#        
# A function is defined called "costOfWater" that takes a single parameter and returns the cost depending on how many liters
# of water the customer consumed.
def costofWater(water): 
    if water >= 1 and water <= 15:
        return 10 + 20
    elif water >= 16 and water <= 50:
        return 25 + 20
    elif water >= 51 and water <= 100:
        return 40 + 20
    elif water >= 101:
        return 50 + 20
    
customers = {} # Define an empty dictionary called "customers".

# An infinite loop is created to prompt the user to enter Customer Names and their Consumption.
# If the word "END" is entered the loop breaks and the program continues.
# The customer cost is calculated by calling the previously defined function and is stored to it's respective variable.
# Lastly we append both the Customer Names and the Costs(Keys and Values) into the Dictionary.
while True:
    customerName = input("Enter customer Name: ") # Promts the user for the name of the customer.
    if customerName == "END":
        break
    customerConsumption = int(input("Enter the consumption of the Customer in Liters: ")) # Prompts the user for the consumption.
    customerCost = costofWater(customerConsumption) # We call the previously defined function to figure out the cost.
    customers.update({customerName : customerCost}) # We append the names and the costs of each customer into a dictionary.


# We find the key(customer name) in the customers dictionary which corresponds to the maximum value.
highestBillName = max(customers, key = customers.get) # We apply the get method with the key parameter to find it.
print("Highest bill was", max(customers.values()), "Euros which was payed by", highestBillName, ".") 

# Prints the total revenue of the company by using the sum function on the values of the customers dictionary.
print("The total revenue of the company is:", sum(customers.values()),"Euros.")

# Iterates the keys and values in the customers dictionary and shows us each customer how much he payed.
for customers, cost in customers.items():
    print(customers, "payed a total of", cost, "Euros.")
