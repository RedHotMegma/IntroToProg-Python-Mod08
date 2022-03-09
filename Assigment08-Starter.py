
# ------------------------------------------------------------------------ #
# Title: Assignment 08
# Description: Working with classes

# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 8
# MSumnicht,2.6.2022,Modified code to complete assignment 8
# ------------------------------------------------------------------------ #

# Data -------------------------------------------------------------------- #
strFileName = 'products.txt'
lstOfProductObjects = []

class Product:
    """Stores data about a product:

    properties:
        product_name: (string) with the products's  name
        product_price: (float) with the products's standard price
    methods:
    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MSumnicht,3.6.2022,Modified code to complete assignment 8
    """
    # TODO: Add Code to the Product class
    # -- Fields --
    # -- Constructor --
    def __init__(self, product_name, product_price):
        #     -- Attributes --
        self.__product_name = product_name
        self.__product_price = product_price
    # -- Properties --
    @property
    def product_name(self):
        return str(self.__product_name).title()

    @product_name.setter
    def product_name(self, value):
        if str(value).isnumeric() == False:
            self.__product_name = value
        else:
            raise Exception("Names cannot be numbers")

    @property
    def product_price(self):
        return float(self.__product_price)

    @product_price.setter
    def product_price(self, value):
        if float(value).isnumeric == True:
            self.__product_price = value
        else:
            raise Exception("Price must be numeric")
    # -- Methods --


# Data -------------------------------------------------------------------- #

# Processing  ------------------------------------------------------------- #
class FileProcessor:
    """Processes data to and from a file and a list of product objects:

    methods:
        save_data_to_file(file_name, list_of_product_objects):

        read_data_from_file(file_name): -> (a list of product objects)

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MSumnicht,3.6.2022,Modified code to complete assignment 8
    """
    def read_data_from_file(file_name, lstOfProductObjects):
        try:
            file = open(file_name, "r")
            for row in file:
                for item in row:
                    row.append(item)
                lstOfProductObjects.append[row]
        except:
            file = open(file_name, "w")
            lstOfProductObjects = []
        file.close()
        return lstOfProductObjects

    def save_data_to_file(file_name, list_of_product_objects):
        file = open(file_name, "w")
        for row in list_of_product_objects:
            file.write(row[0] + "," + str(row[1]) + "\n")
        file.close()


# Processing  ------------------------------------------------------------- #

# Presentation (Input/Output)  -------------------------------------------- #
class IO:
    # TODO: Add docstring
    """Creates functions which display text to the user and retrieve user inputs:

    methods:
        print_menu(self):
        get_user_choice(self):
        show_current_data(self, list_of_product_objects):
        get_product_data(self):

    changelog: (When,Who,What)
        RRoot,1.1.2030,Created Class
        MSumnicht,3.6.2022,Modified code to complete assignment 8
    """

    # TODO: Add code to show menu to user
    def print_menu(self):
        print("Menu of Options\n"
              "\t1) See current data\n"
              "\t2) Add a new product\n"
              "\t3) Save and exit\n")
    # TODO: Add code to get user's choice
    def get_user_choice(self):
        user_choice = input("Please select a menu option: ")
        return user_choice
    # TODO: Add code to show the current data from the file to user
    def show_current_data(self, list_of_product_objects):
        for row in list_of_product_objects:
            print(row)
    # TODO: Add code to get product data from user
    def get_product_data(self):
        newProduct = Product(input("Please enter the product's name: "), input("Please enter the product's price: "))
        return newProduct

# Presentation (Input/Output)  -------------------------------------------- #

# Main Body of Script  ---------------------------------------------------- #
Present = IO()
# FileProcessor = FileProcessor()
# Load data from file into a list of product objects when script starts
FileProcessor.read_data_from_file(strFileName)

# Show user a menu of options
while True:
    Present.print_menu()

    # Get user's menu option choice
    # Show user current data in the list of product objects
    # Let user add data to the list of product objects
    # let user save current data to file and exit program
    userChoice = Present.get_user_choice()

    if userChoice == "1":
        Present.show_current_data(lstOfProductObjects)
    elif userChoice == "2":
        product_data = Present.get_product_data()
        row = [product_data.product_name, product_data.product_price]
        lstOfProductObjects.append(row)
    elif userChoice == "3":
        FileProcessor.save_data_to_file(strFileName, lstOfProductObjects)
        break
    else:
        print("Please select option from the menu.\n")



# Main Body of Script  ---------------------------------------------------- #