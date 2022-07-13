from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
m1 = Menu()
c1 = CoffeeMaker()
coins = MoneyMachine()
is_continue = True
while is_continue:
    choice = input("what would you like? Espresso/ latte / cappuccino")
    if choice == "off":
        is_continue = False
    elif choice == "report":
        reports = c1.report()
        print(reports)
    else:
        drinks = m1.find_drink(choice)
        print(drinks)
        resource = c1.is_resource_sufficient(drinks)
        print(resource)
        if resource and coins.make_payment(drinks.cost):
            c1.make_coffee(drinks)









