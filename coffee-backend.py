amount_water = 400
amount_milk = 540
amount_beans = 120
amount_disposable_cups = 9
amount_money = 550
espresso_water = 250

def calculation_espresso():
    global amount_water
    global amount_milk
    global amount_beans
    global amount_disposable_cups
    global amount_money
    water_esp = amount_water // 200
    beans_esp = amount_beans // 16
    min_esp = min([beans_esp, water_esp])
    if min_esp >= 1:
        amount_water -= 250
        amount_milk -= 0
        amount_beans -= 16
        amount_disposable_cups -= 1
        amount_money += 4
        print("I have enough resources, making you a coffee!")
    elif water_esp <= 1:
        print("Sorry, not enough water!")
    elif beans_esp <= 1:
        print("Sorry, not enough beans")
    print("")





def remaining():
    print('The coffee machine has:')
    print(amount_water, 'of water')
    print(amount_milk, 'of milk')
    print(amount_beans, 'of coffee beans')
    print(amount_disposable_cups, 'of disposable cups')
    print(amount_money, 'of money')
    print('')
    print('')


def buy():
    global amount_water
    global amount_milk
    global amount_beans
    global amount_disposable_cups
    global amount_money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
    Coffee = input()

    if Coffee == "1":
        calculation_espresso()


    if Coffee == "2":
        amount_water -= 350
        amount_milk -= 75
        amount_beans -= 20
        amount_disposable_cups -= 1
        amount_money += 7
    if Coffee == "3":
        amount_water -= 200
        amount_milk -= 100
        amount_beans -= 12
        amount_disposable_cups -= 1
        amount_money += 6
    if Coffee == "back":
        menu()


def menu():
    print("Write action (buy, fill, take, remaining, exit):")
    action = input()
    if action == "buy":
        buy()
    if action == "fill":
        fill()
    if action == "take":
        take()
    if action == "remaining":
        remaining()
    if action == "exit":
        breakpoint()
    menu()


def fill():
    global amount_water
    global amount_milk
    global amount_beans
    global amount_disposable_cups
    global amount_money
    print('Write how many ml of water do you want to add.')
    amount_water += int(input())
    print('Write how many ml of milk do you want to add:')
    amount_milk += int(input())
    print('Write how many grams of coffee beans do you want to add:')
    amount_beans += int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    amount_disposable_cups += int(input())
    menu()


def take():
    global amount_money
    print("I gave you $", amount_money)
    amount_money = 0
    menu()


menu()
