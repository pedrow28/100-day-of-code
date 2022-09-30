from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Turning the machine on
machine_on = True

while machine_on:

    # Creating objects
    menu = Menu()
    coffee_machine = CoffeeMaker()
    money_machine = MoneyMachine()

    # Getting the order/command

    order = input(f"What is your order? ({menu.get_items()}) ")

    # Calling report secret command

    if order == "report":

        coffee_machine.report()
        money_machine.report()

    # Calling off secret command

    elif order == "off":

        machine_on = False  # Turning off the machine

    # Getting orders

    else:

        order_item = menu.find_drink(order)  # Find drink to be modeled

        if coffee_machine.is_resource_sufficient(order_item) and money_machine.make_payment(order_item.cost):
            coffee_machine.make_coffee(order_item)




