# The uuid library will stand later useful as we will need a way to generate unique ID's for each customer.
# The csv library will stand later useful as we will need it to be able to export infomation using the csv format.
import uuid
import csv


def menu():  # A "menu()" function is defined that will serve the purpose of choosing what action the employee will take when the credentials entered at the log-in page are correct.
    # An indefinite loop is created to loop the following eleven (11) options the employee has. The employee can quit by simply pressing the number eleven (11) on the keyboard. "\n" is added throughout the program at various segments to achieve readability.
    while True:
        print("""\nChoose what action you want to execute by entering the appropriate number.\n
                1): Place order.
                2): Display number of orders placed by a specific customer.
                3): Display numbers of orders in one specific day.
                4): Display total amount of all orders delivered.
                5): Display total amount of the orders placed by a specific customer.
                6): Total amount of the orders placed by a specific day.
                7): Export all the customer's name that ordered - txt format.
                8): Export orders entered per user - txt format.
                9): Export all data - csv format.
                10): Export total amount of orders per day - csv format.
                11): Exit menu dialog.
                """)  # We print the series of options the user can choose.
        programSelect = input("Enter number 1 through 11: ") # The user inputs a number from 1 through 11.

        match programSelect: # We use the match statement to match the input entered by the user.
            case "1":
                placeOrder()
            case "2":
                numOrdersSpecificCustomer()
            case "3":
                totalOrdersSpecificDate()
            case "4":
                totalAmountOrders()
            case "5":
                totalAmountSpecificCustomer()
            case "6":
                totalAmountSpecificDay()
            case "7":
                exportNames()
            case "8":
                exportOrdersEnteredUser()
            case "9":
                exportAll()
            case "10":
                exportTotalAmount()
            case "11":
                break # If the user enters 11 the loop is broken and the program is exited.
            case _:
                print("Wrong input! Please enter a number and make sure it is an integer 1 through 11.") # If the user enters anything else than 1 through 11 an error message is displayed.


# A function named "customerIdGenerator" is created to assign unique ID's to each customer.
def customerIdGenerator():
    # Generates a unique customer ID using the "uuid" library.
    customerId = int(uuid.uuid4().int)
    return customerId  # Returns the "customerId" variable above.


# (1) The function below takes the role of placing an order. In essence it runs when one of the three employees chooses to take an order from a customer.
# It takes exactly four variables that the user inputs. The name, address, date, and total amount of the order. Then it creates a list with the four variables.
# Lastly, it appends the list created in a list that contains all the customers.
def placeOrder():
    try:  # We include the user input into a try block so we can raise errors.
        # The function asks for the user to enter the name of the customer.
        customerName = input("\nEnter the name of the customer: ")
        if not customerName:  # If the customer's name field is empty an error is raised.
            raise ValueError("The customers name field cannot be empty!")
        # Then the adress is entered.
        customerAddress = input("Enter the address of the customer: ")
        if not customerAddress:  # If the customer's address field is empty an error is raised.
            raise ValueError("The customers address field cannot be empty!")
        # Afterwards the date is entered in the manner of DD-MM-YY.
        customerDate = input("Enter the date in 'DDMMYY' format: ")
        # Some conditions need to be met for the raise not to kick in. First it checks if the input is 6 numbers long using len(). Then it checks if it is digits using the .isdigit() method and lastly it checks if the field is empty.
        if len(customerDate) != 6 or not customerDate.isdigit() or not customerDate:
            raise ValueError(
                "The customers date field should be in DDMMYY format. Please try again!")
        # Lastly the total amount is entered that the customer spent on the order.
        customerTotalAmount = float(
            input("Enter the total amount of the order: "))
        # Here the program makes sure that the input entered is greater than 0.
        if customerTotalAmount <= 0:
            raise ValueError(
                "Minimum amount must be greater than 0. Please try again!")
        # We define a variable and call the customer ID generation function that was previously defined.
        customerUniqueIdentifier = customerIdGenerator()
        # We define a list of the previous variables from the four inputs and the ID generator function.
        customerInfo = [customerName, customerAddress, customerDate,
                        customerTotalAmount, customerUniqueIdentifier]
        # Lastly we append the previous list ("customerInfo") into a list that includes lists of all the customers outside this function.
        customersList.append(customerInfo)
        print("Order was placed!")
    except ValueError as e:  # Lastly any other exceptions are handled here.
        print(f"Error: {e}")

# (2) Number of orders placed by one specific customer.


def numOrdersSpecificCustomer():
    # Iterates the customer name in the "customersList" for the user to see.
    for customer in customersList:
        print(customer[0])
    # Then the user inputs the name.
    inputName = input(
        "\nThe following customers have placed orders. Enter the name you want to look up: ")
    # Generator expression to see the number of times where the name in the "customersList" matches the input entered by the user.
    occurrences = sum(
        1 for customer in customersList if customer[0] == inputName)
    print(f"The customer {inputName} has ordered {occurrences} time(s).")


# (3) Total number of orders in one specific day.
def totalOrdersSpecificDate():
    # Iterates the date in the "customersList" for the user to see.
    for date in customersList:
        print(date[2])
    # Asks for date input.
    inputDate = input(
        "\nIn the following dates there were orders placed. Enter a specific date to see how many total orders were placed: ")
    # Generator expression to see the number of times where the date in the "customersList" matches the input entered by the user.
    occurences = sum(1 for date in customersList if date[2] == inputDate)
    print(f"In the date: {inputDate} there were {occurences} orders.")


# (4) Total amount of all orders delivered.
def totalAmountOrders():
    # We use the sum function to add each every third index in each list in the "customersList".
    totalMoneySpent = sum(customer[3] for customer in customersList)
    print("\nThe total amount of all orders delivered is: " +
          str(totalMoneySpent) + ".")


# (5) Total amount of the orders placed by a specific customer.
def totalAmountSpecificCustomer():
    # Iterates the "customersList" and prints each customer's name for the user to be able to choose.
    for customer in customersList:
        print(customer[0])
    inputName = input(
        # Input is made.
        "\nThe following customers have placed orders. Enter the name you want to look up to see the total amount of a specific customer: ")
    # An initial variable "totalMoney" is defined with a value of zero "0".
    totalMoney = 0
    for customer in customersList:  # A loop is created to iterate the "customersList".
        # A conditional statement is defined to figure out if the input made before matches the first index which is the name of the customer in the list.
        if inputName in customer[0]:
            # If it is true then it is added to the "totalMoney" variable by extracting it from the fourth index from the list.
            totalMoney += int(customer[3])
    # Output is displayed.
    print(f"The total money spent by {inputName} is: {totalMoney}.")


# (6) Total amount of the orders placed by a specific day.
def totalAmountSpecificDay():
    for date in customersList:  # Iterates the dates in the "customersList".
        print(date[2])
    inputDate = input(
        # Input is entered from the user.
        "\nThe following dates there were orders placed. Write a date to see the total amount of orders placed that day: ")
    # An initial variable called "totalMoney" is defined with a value of zero "0".
    totalMoney = 0
    for date in customersList:  # A loop is created to iterate the "customersList".
        # A conditional statement is defined to figure out if the input made before matches the third index which is the date of the customer in the list who made an order.
        if inputDate in date[2]:
            # If it is true then it is added to the totalMoney variable by extracting it from the fourth index from the list.
            totalMoney += int(date[3])
    print(f"The total money spent in the date {inputDate} is: {totalMoney}.")


# (7) Export names of customers in .txt format.
def exportNames():
    # Creates a "fileObject" with the name of "namesExport" and the attribute "w" to write.
    fileObject = open("namesExport", "w")
    for customer in customersList:  # Iterates the "customersList".
        # Writes each customer using the [0] index.
        fileObject.write("Name: " + customer[0] + "." + "\n")
    # Informs the user the export was made.
    print("The customers who ordered were exported to a text file named 'namesExport.txt'")
    fileObject.close()  # Closes the "fileObject".


# (8) Export orders entered per user in .txt format.
def exportOrdersEnteredUser():
    ordersPerUser = {}  # An empty dictionary "ordersPerUser" is defined.
    for customer in customersList:  # Iterates the "customersList".
        # A variable is defined with the index [0] from the "customersList".
        name = customer[0]
        # Sets a default value of "0" for the key "name" in the dictionary.
        ordersPerUser.setdefault(name, 0)
        ordersPerUser[name] += 1  # Increments the value when the user orders.
    # Creates a "fileObject" with the name of "ordersPerUser" and the attribute "w" to write.
    fileObject = open("ordersPerUser", "w")
    fileObject.write(str(ordersPerUser))  # Writes the dictionary to the file.
    # Informs the user the export was made.
    print("The orders entered per user were exported to the text file named 'ordersPerUser.txt'")
    fileObject.close()  # Closes the "fileObject".


# (9) Export all data entered in .csv format.
def exportAll():
    # We create a list of the titles so we can write them later down the road.
    titles = ['Name', 'Address', 'Date', 'Amount', 'ID']
    # We set a variable called 'rows' that pinpoints to the "customersList".
    rows = customersList
    # We create the variable and assign it to the following name.
    filename = "coffeeshopData.csv"
    with open(filename, 'w') as csvfile:
        # We create the csv writer object.
        csvwriter = csv.writer(csvfile)
        # We write the titles.
        csvwriter.writerow(titles)
        # And lastly we write rows to the file.
        csvwriter.writerows(rows)
    # Informs the user about the export.
    print(f"Export was completed to {filename}.")


# (10) Export total amount of orders per day in .csv format.
def exportTotalAmount():
    # We create a list of the titles so we can write it to the file later.
    titles = ['Date', 'Total Amount']
    totalPerDay = {}  # Define empty list called "totalPerDay".
    for customer in customersList:  # Iterates the "customersList".
        # Variable named "date" which points to the date index of the list.
        date = customer[2]
        # Variable named "value" which points to the value index of the list.
        value = int(customer[3])
        # If a date is already present we add the value to the existing value of the specific date otherwise if it does not exist we add a new pair to the dictionary.
        if date in totalPerDay:
            totalPerDay[date] += value
        else:
            totalPerDay[date] = value
    # We create the variable and assign it to the following name.
    filename = 'amountOfOrdersPerday.csv'
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)  # We create the csv writer object.
        # We write the titles defined in the beginning.
        csvwriter.writerow(titles)
        # Iterates the dictionary and writes the key/value to the csv file using the writerow().
        for date, spend in totalPerDay.items():
            csvwriter.writerow([date, spend])
    # Informs the user about the export.
    print(f"Export was completed to {filename}.")


# The coffeeshop has 3 employees that have a user account and a password to login. Each user has two corresponding variables for their username and password.
username1 = ("Jenny")
password1 = ("Mickeymouse")
username2 = ("Adam")
password2 = ("Donald")
username3 = ("Lucy")
password3 = ("Goofy")

# A list is defined that will contain a list for each customer with their respective information that are passed through the "order()"" function previously defined.
customersList = []

# Welcome message.
print("Welcome to the User Log-In page of the Coffee Shop! To quit the log-in page simply type '0' either on the Username or Password field.\n")


# An infinite loop is defined to loop the log-in page. If the correct credentials are entered then the "menu()" function is called.
while True:
    try:  # We include the conditionals in a a try block of code to include the exception in the end.
        # The program asks for the employee to input the username.
        usernameInput = input("\nPlease enter your Username: ")
        # This if statement and the next one below break the loop and exit the program if the user enters zero (0).
        if usernameInput == "0":
            print("\nProgram was terminated.")
            break
        if not usernameInput:  # This conditional raises an error if the username field is empty.
            raise ValueError("Username field cannot be empty.")
            continue
        # The programs asks for the employee to input the password.
        passwordInput = input("Please enter your Password: ")
        if passwordInput == "0":
            print("\nProgram was terminated.")
            break
        if not passwordInput:  # This conditional raises an error if the password field is empty.
            raise ValueError("Password field cannot be empty.")
        # Then a set of conditionals is made to figure out if the username and password is correct.
        # The if statement checks for the first user.
        if usernameInput == username1 and passwordInput == password1:
            menu()  # If the credentials are correct then the "menu()" function is called for the employee to further take orders, extrapolate information and export.
        # The elif statement checks for the second user.
        elif usernameInput == username1 and passwordInput == password1:
            menu()  # Same as above.
        # The second elif statement checks for the third user.
        elif usernameInput == username1 and passwordInput == password1:
            menu()  # Same as above.
        else:
            # Lastly the else statement informs the user that the credentials entered were wrong.
            print("\nWrong username and/or password please re-enter your credentials.")
    except Exception as e:  # Any misc. error's are handled though this except block.
        print(f"\nError: {e}")
