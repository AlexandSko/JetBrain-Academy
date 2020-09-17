def machine_state():
    global water, milk, coffee_beans, disposable_cups, money
    print(f"\nThe coffee machine has:",
          f"{water} of water",
          f"{milk} of milk",
          f"{coffee_beans} of coffee_beans",
          f"{disposable_cups} of disposable cups",
          f"{money} of money", sep="\n", end="\n\n")


def espresso():
    global water, milk, coffee_beans, disposable_cups, money
    water -= 250
    coffee_beans -= 16
    disposable_cups -= 1
    money += 4


def latte():
    global water, milk, coffee_beans, disposable_cups, money
    water -= 350
    milk -= 75
    coffee_beans -= 20
    disposable_cups -= 1
    money += 7


def cappuccino():
    global water, milk, coffee_beans, disposable_cups, money
    water -= 200
    milk -= 100
    coffee_beans -= 12
    disposable_cups -= 1
    money += 6


def buy():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    type_of_coffee = int(input())
    if type_of_coffee == 1:
        espresso()
    elif type_of_coffee == 2:
        latte()
    elif type_of_coffee == 3:
        cappuccino()
    else:
        ...


def fill():
    global water, milk, coffee_beans, disposable_cups
    water += int(input("Write how many ml of water do you want to add:\n"))
    milk += int(input("Write how many ml of milk do you want to add:\n"))
    coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
    disposable_cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))


def take():
    global money
    print(f'I gave you ${money}')
    money = 0


def get_action():
    action = input("Write action (buy, fill, take):\n")
    if action == "buy":
        buy()
    elif action == "fill":
        fill()
    elif action == "take":
        take()
    else:
        ...


def coffee_machine():
    machine_state()
    get_action()
    machine_state()


if __name__ == "__main__":

    water = 400
    milk = 540
    coffee_beans = 120
    disposable_cups = 9
    money = 550

    coffee_machine()
