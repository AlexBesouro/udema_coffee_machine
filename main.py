from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Step 1. Generate objects
new_machine = CoffeeMaker() # Generate new object - new coffee machine
money_machine = MoneyMachine()  # Generate new object - new money machine
menu = Menu()   # Generate new object - menu with 3 coffee drinks


# Step 2. Create a while loop
is_on = True
while is_on:
    options = menu.get_items()  # get_items() methode returns list of drinks available
    choice = input(f"What would you like to drink? ({options}): \n")    # Put user's choice into a variable
    if choice == "off": # If 'off' command is entered, our machine is turned off
        is_on = False
    elif choice == "report":    # If 'report' command is entered, all resources available are printed out
        # Step 3. Print out reports
        new_machine.report()  # Call report() methode to show up available resources in the machine
        money_machine.report()  # Call report() methode to show up earned money in the machine
    else:
        drink = menu.find_drink(choice) # Assign user's choice to a drink variable preliminary checked if it is in a menu
        if new_machine.is_resource_sufficient(drink):   # Verify the coffee machine has enough resources
            if money_machine.make_payment(drink.cost):  # Make payment, preliminary checked if there was enough coin inserted
                new_machine.make_coffee(drink)  # Make a drink




