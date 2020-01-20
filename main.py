
import decimal
import re

dec = decimal.Decimal

running = True
print("\nWelcome to the Change Calculator!\n")


def change_calculator():
    hundreds = 0
    fifties = 0
    twenties = 0
    tens = 0
    fives = 0
    singles = 0
    quarters = 0
    dimes = 0
    nickels = 0
    pennies = 0

    price = input("\nPlease enter the price of the item: ")
    payment = input("Please enter payment received: ")

    price = re.sub(r'[^\d.]+', '', price)
    payment = re.sub(r'[^\d.]+', '', payment)

    if payment == "" or price == "":
        return

    price = dec(price)
    payment = dec(payment)

    if price > payment:
        print("That's not enough money to pay...")
        return
    elif price == payment:
        print("No change.")
        return

    change = payment - price

    print("Change due: $" + str(change.quantize(dec('0.00'))))

    while change >= 100:
        change -= 100
        hundreds += 1

    while change >= 50:
        change -= 50
        fifties += 1

    while change >= 20:
        change -= 20
        twenties += 1

    while change >= 10:
        change -= 10
        tens += 1

    while change >= 5:
        change -= 5
        fives += 1

    while change >= 1:
        change -= 1
        singles += 1

    while change >= dec(.25):
        change -= dec(.25)
        quarters += dec(1)

    while change >= dec(.10):
        change -= dec(.10)
        dimes += dec(1)

    while change >= dec(.05):
        change -= dec(.05)
        nickels += 1

    while change > dec(.0):
        change -= dec(.01)
        pennies += dec(1)

    print("\n$100 bills: -", hundreds, "\n$50 bills: --", fifties, "\n$20 bills: --", twenties,
          "\n$10 bills: --", tens, "\n$5 bills: ---", fives, "\n$1 bills: ---", singles, "\nQuarters: ---",
          quarters, "\nDimes: ------", dimes, "\nNickels: ----", nickels, "\nPennies: ----", pennies)


while running:
    change_calculator()
