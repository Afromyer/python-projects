from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_off = False

while is_off == False:
    user_choice = input(f"What would you like? ({menu.get_items()}): ")
    if user_choice.lower() == "off":
        is_off = True
    elif user_choice.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        menu_item = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(menu_item) and money_machine.make_payment(menu_item.cost):
            coffee_maker.make_coffee(menu_item)


