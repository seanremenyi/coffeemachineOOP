from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

machine = CoffeeMaker()
choices = Menu()
money_counter = MoneyMachine()

is_on = True

while is_on:
    options = choices.get_items()
    user_input = input("What would you like? (espresso/latte/cappuccino): ")
    if user_input == "off":
        is_on = False
    elif user_input == "report":
        machine.report()
        money_counter.report()
    else:
        item = choices.find_drink(user_input)
        resources = machine.is_resource_sufficient(item)
        payment = money_counter.make_payment(item.cost)
        if payment and resources:
            machine.make_coffee(item)