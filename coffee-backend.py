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
    cups = amount_disposable_cups // 1
    min_esp = min([beans_esp, water_esp, cups])
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
        print("Sorry, not enough beans!")
    elif cups <= 1:
        print("Sorry, not enough cups!")
    print("")

def calculation_Latte():
    global amount_water
    global amount_milk
    global amount_beans
    global amount_disposable_cups
    global amount_money
    water_latte = amount_water // 350
    milk_latte = amount_milk // 75
    beans_latte = amount_beans // 20
    cups_latte = amount_disposable_cups // 1
    min_latte = min([water_latte, milk_latte, beans_latte, cups_latte])
    if min_latte > 1:
        amount_water -= 350
        amount_milk -= 75
        amount_beans -= 20
        amount_disposable_cups -= 1
        amount_money += 7
        print("I have enough resources, making you a coffee!")
    elif water_latte < 1:
        print("Sorry, not enough water!")
    elif milk_latte < 1:
        print("Sorry, not enough milk!")
    elif beans_latte < 1:
        print("Sorry, not enough beans!")
    elif cups_latte < 1:
        print("Sorry, not enough cups!")

def calculation_cappuccino():
    global amount_water
    global amount_milk
    global amount_beans
    global amount_disposable_cups
    global amount_money
    water_capp = amount_water // 200
    milk_capp = amount_milk // 100
    beans_capp = amount_beans // 12
    cups_capp = amount_disposable_cups // 1
    min_capp = min([water_capp, milk_capp, beans_capp, cups_capp])
    if milk_capp >= 1:
        amount_water -= 200
        amount_milk -= 100
        amount_beans -= 12
        amount_disposable_cups -= 1
        amount_money += 6
        print("I have enough resources, making you a coffee!")
    elif water_capp < 1:
        print("Sorry, not enough water!")
    elif milk_capp < 1:
        print("Sorry, not enough milk!")
    elif beans_capp < 1:
        print("Sorry, not enough beans!")
    elif cups_capp < 1:
        print("Sorry, not enough cups!")





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
        calculation_Latte()

    if Coffee == "3":
        calculation_cappuccino()

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
