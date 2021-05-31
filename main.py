from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

def coff_machine():
    machine = CoffeeMaker()
    choices = Menu()

    while True:
        user_input = input("What would you like? (espresso/latte/cappuccino): "):
        if user_input == "off":
            break
        elif