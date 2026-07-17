from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
machine_running = True

while machine_running:
    choice = input(f"What would you like to have? {menu.get_items()}: ").lower()

    if choice == "off":
        machine_running = False

    elif choice == "report":
        money_machine.report()
        print("\n")
        coffee_maker.report()

    else:
        order = menu.find_drink(choice)
        if order:
            if coffee_maker.is_resource_sufficient(order):
                if money_machine.make_payment(order.cost):
                    coffee_maker.make_coffee(order)
        else:
            print("Please enter a valid choice.")




