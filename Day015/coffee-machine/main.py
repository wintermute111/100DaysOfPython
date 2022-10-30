from art import logo


def resources_sufficient(order_ingredients):
    """Returns True if the drink can be made, returns False if resources are insufficient"""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}. Please make another choice.")
            return False
    return True


def process_coins():
    """Returns the total of coins received from the customer"""
    print("Please insert coins.")
    total = int(input("how many quarters? ")) * 0.25
    total += int(input("how many dimes? ")) * 0.10
    total += int(input("how many nickels? ")) * 0.05
    total += int(input("how many pennies? ")) * 0.01
    return total


def transaction_successful(money_received, drink_cost):
    """Returns True if payment is accepted, returns False if funds are insufficient"""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change:.2f} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the coffee machine resources"""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0
machine_on = True

while machine_on:
    print(logo)
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        machine_on = False
        print("Coffee machine powering down. Please remove any perishable resources.")
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit:.2f}")
    else:
        try:
            drink = MENU[choice]
            if resources_sufficient(drink['ingredients']):
                print(f"Price: ${drink['cost']:.2f}")
                payment = process_coins()
                if transaction_successful(payment, drink['cost']):
                    make_coffee(choice, drink['ingredients'])
        except KeyError:
            print("Not a valid choice. Please try again.")
