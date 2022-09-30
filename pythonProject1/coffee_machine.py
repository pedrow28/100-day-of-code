
# COFFEE MACHINE

# Receitas

"""

espresso = 50 ml water / 18g coffee - 15 cents
latte = 200ml water / 24g coffee / 150ml milk - 50 cents
cappuccino = 250 ml water / 24g coffee / 100 ml milk - 75 cents

"""

# Moedas

"""
penny = 0.01
nickel = 0.05
dime = 0.10
quarter = 0.25

"""
# Initial resources

water = 300
milk = 200
coffee = 100
money_machine = 50  # troco?

# Improvement: make functions to serve itens and get code shorter

machine_on = True


while machine_on:

    # Order
    order = input("What do you want? (espresso/latte/cappuccino) ")

    if order == "report":
        print(f"Water: {water}.\nMilk: {milk}.\nCoffee: {coffee}.\nMoney: ${money_machine}.")

    elif order == "off":
        machine_on = False
    else:
        # Ask for the money
        print("Please insert coins.")
        pennies = int(input("How many pennies? "))
        nickles = int(input("How many nickles? ")) * 5
        dimes = int(input("How many dimes? ")) * 10
        quarters = int(input("How many quarters? ")) * 25
        # Total money
        money = (pennies + nickles + dimes + quarters) / 100  # Must discover later what about this bug

        # Adjust the function to the machine checks if there are enough resources
        if order == "espresso":  # Espresso
            if money >= 0.15:  # Get better, when money = price, new if statement with no change
                if water < 50 or coffee < 18:
                    print("Sorry, we are out of materials! Money reimbursed.")  # Verify the resources before the order
                else:
                    water -= 50
                    coffee -= 18

                    money_machine += money
                    change = money - 0.15
                    money_machine -= change
                    print(f"Here's ${change} in change.\n Here's your espresso.")
            else:
                print("Please insert more coins.") # Think in how turn to add more money
        elif order == "latte":  # Serving latte
            if money >= 0.5:
                water -= 200
                coffee -= 24
                milk -= 150

                money_machine += money
                change = money - 0.5
                money_machine -= change
                print(f"Here's ${change} in change.\n Here's your latte.")
        elif order == "cappuccino":  # Serving latte
            if money >= 0.75:
                water -= 250
                coffee -= 24
                milk -= 100

                money_machine += money
                change = money - 0.75
                money_machine -= change
                print(f"Here's ${change} in change.\n Here's your cappuccino.")
            else:
                print("Please insert more coins.")  # Think in how turn to add more money
