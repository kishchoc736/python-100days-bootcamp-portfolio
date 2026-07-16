from operator import truediv

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
    "money": 0
}

"""
penny: 0.01
Nickel: 0.05
Dime: 0.10
Quarter: 0.25
"""

"""
Print report
"""
def print_report():
    print(f"Water: {resources['water']}\n"
          f"Milk: {resources['milk']}\n"
          f"Coffee: {resources['coffee']}\n"
          f"Money: ${resources['money']:.2f}\n")

"""
Check if resources are available
"""
def check_resources(order):
    """
    for each order
    check if the corresponding resources are available
    :param order:
    :return:
    """
    for ingredient, amount_needed in order["ingredients"].items():
        if amount_needed > resources[ingredient]:
            print(f"There is not enough {ingredient}")
            return False
    return True

def process_payment(order)-> bool:
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickels = int(input("How many nickels?: "))
    pennies = int(input("How many pennies?: "))

    total_payment = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

    if total_payment < order["cost"]:
        print("Sorry, you don't have enough money")
        return False

    change = total_payment - order["cost"]
    print(f"Here is ${change:.2f} in change")
    return True

def make_coffee(order):
    for ingredient, amount_needed in order["ingredients"].items():
        resources[ingredient] -= amount_needed
    resources["money"] += order["cost"]

def run_coffee_machine():
    machine_running = True
    while machine_running:
        order_input = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if order_input == "off":
            machine_running = False
        elif order_input == "report":
            print_report()
        elif order_input in MENU:
            order = MENU[order_input]
            if check_resources(order):
                if process_payment(order):
                    make_coffee(order)
                    print(f"Here is your {order_input}")


run_coffee_machine()



