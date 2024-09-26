from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffeeMaker = CoffeeMaker()
money_machine = MoneyMachine()

machine_on = True


while machine_on:
    options = menu.get_items()
    choice = str(input(f"What would you like? ({options}): ").lower())
    if choice == "off":
        machine_on = False
    elif choice == "report":
        coffeeMaker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        if coffeeMaker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffeeMaker.make_coffee(drink)
    if coffeeMaker.is_resource_sufficient(menu.find_drink("espresso")) == False:
        print(
            "\nThe machine is out of resources of all of the drinks\nShutting down now")
        machine_on = False
