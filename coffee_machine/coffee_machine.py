def machine_state(water, milk, coffee_beans, disposable_cups, money):
    print(f"\nThe coffee machine has:",
          f"{water} of water",
          f"{milk} of milk",
          f"{coffee_beans} of coffee_beans",
          f"{disposable_cups} of disposable cups",
          f"{money} of money", sep="\n", end="\n\n")


def espresso(water, milk, coffee_beans, disposable_cups, money):
    water -= 250
    coffee_beans -= 16
    disposable_cups -= 1
    money += 4
    return water, milk, coffee_beans, disposable_cups, money


def latte(water, milk, coffee_beans, disposable_cups, money):
    water -= 350
    milk -= 75
    coffee_beans -= 20
    disposable_cups -= 1
    money += 7
    return water, milk, coffee_beans, disposable_cups, money


def cappuccino(water, milk, coffee_beans, disposable_cups, money):
    water -= 200
    milk -= 100
    coffee_beans -= 12
    disposable_cups -= 1
    money += 6
    return water, milk, coffee_beans, disposable_cups, money


def buy(water, milk, coffee_beans, disposable_cups, money):
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    type_of_coffee = int(input())
    if type_of_coffee == 1:
        return espresso(water, milk, coffee_beans, disposable_cups, money)
    elif type_of_coffee == 2:
        return latte(water, milk, coffee_beans, disposable_cups, money)
    elif type_of_coffee == 3:
        return cappuccino(water, milk, coffee_beans, disposable_cups, money)


def fill(water, milk, coffee_beans, disposable_cups, money):
    water += int(input("Write how many ml of water do you want to add:\n"))
    milk += int(input("Write how many ml of milk do you want to add:\n"))
    coffee_beans += int(input("Write how many grams of coffee beans do you want to add:\n"))
    disposable_cups += int(input("Write how many disposable cups of coffee do you want to add:\n"))
    return water, milk, coffee_beans, disposable_cups, money


def take(water, milk, coffee_beans, disposable_cups, money):
    print(f'I gave you ${money}')
    money = 0
    return water, milk, coffee_beans, disposable_cups, money


def get_action(water, milk, coffee_beans, disposable_cups, money):
    action = input("Write action (buy, fill, take):\n")
    if action == "buy":
        return buy(water, milk, coffee_beans, disposable_cups, money)
    elif action == "fill":
        return fill(water, milk, coffee_beans, disposable_cups, money)
    elif action == "take":
        return take(water, milk, coffee_beans, disposable_cups, money)


def coffee_machine(water, milk, coffee_beans, disposable_cups, money):
    machine_state(water, milk, coffee_beans, disposable_cups, money)
    water, milk, coffee_beans, disposable_cups, money = get_action(water, milk, coffee_beans, disposable_cups, money)
    machine_state(water, milk, coffee_beans, disposable_cups, money)


if __name__ == "__main__":

    coffee_machine(water=400, milk=540, coffee_beans=120, disposable_cups=9, money=550)
