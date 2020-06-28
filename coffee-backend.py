amount_water = 400

amount_milk = 540

amount_beans = 120

amount_disposable_cups = 9

amount_money = 550

espresso_water = 250


print('The coffee machine has:')
print(amount_water, 'of water')
print(amount_milk, 'of milk')
print(amount_beans, 'of coffee beans')
print(amount_disposable_cups, 'of disposable cups')
print(amount_money, 'of money')
print('')
print('')


def global_amounts_coffee():
    global amount_water
    global amount_milk
    global amount_beans
    global amount_disposable_cups
    global amount_money
    amount_water -= 250
    amount_milk -= 0
    amount_beans -= 16
    amount_disposable_cups -= 1
    amount_money += 4
    print('The coffee machine has:')
    print(amount_water, 'of water')
    print(amount_milk, 'of milk')
    print(amount_beans, 'of coffee beans')
    print(amount_disposable_cups, 'of disposable cups')
    print(amount_money, 'of money')
    print('')
    print('')


def latte():
    global amount_water
    global amount_milk
    global amount_beans
    global amount_disposable_cups
    global amount_money
    amount_water -= 350
    amount_milk -= 75
    amount_beans -= 20
    amount_disposable_cups -= 1
    amount_money += 7
    print('The coffee machine has:')
    print(amount_water, 'of water')
    print(amount_milk, 'of milk')
    print(amount_beans, 'of coffee beans')
    print(amount_disposable_cups, 'of disposable cups')
    print(amount_money, 'of money')
    print('')
    print('')


def cappuccino():
    global amount_water
    global amount_milk
    global amount_beans
    global amount_disposable_cups
    global amount_money
    amount_water -= 200
    amount_milk -= 100
    amount_beans -= 12
    amount_disposable_cups -= 1
    amount_money += 6
    print('The coffee machine has:')
    print(amount_water, 'of water')
    print(amount_milk, 'of milk')
    print(amount_beans, 'of coffee beans')
    print(amount_disposable_cups, 'of disposable cups')
    print(amount_money, 'of money')
    print('')
    print('')


def fill_amounts_of_machine():
    global amount_water
    global amount_milk
    global amount_beans
    global amount_disposable_cups
    global amount_money
    amount_water += add_water
    amount_milk += add_milk
    amount_beans += add_beans
    amount_disposable_cups += add_disposable_cups
    print('The coffee machine has:')
    print(amount_water, 'of water')
    print(amount_milk, 'of milk')
    print(amount_beans, 'of coffee beans')
    print(amount_disposable_cups, 'of disposable cups')
    print(amount_money, 'of money')
    print('')


def take_money_from_machine():
    global amount_money
    global amount_milk
    global amount_beans
    global amount_disposable_cups
    global amount_money
    amount_money -= amount_money
    print('The coffee machine has:')
    print(amount_water, 'of water')
    print(amount_milk, 'of milk')
    print(amount_beans, 'of coffee beans')
    print(amount_disposable_cups, 'disposable cups')
    print(amount_money, 'of money')


print('Write action (buy, fill, take)')
user_choice = input()

if user_choice == 'buy':
    print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino')
    user_choice = int(input())
    if user_choice == 1:
        global_amounts_espresso()
    elif user_choice == 2:
        latte()
    elif user_choice == 3:
        cappuccino()
sada
if user_choice == 'fill':
    print('Write how many ml of water do you want to add.')
    add_water = int(input())
    print('Write how many ml of milk do you want to add:')
    add_milk = int(input())
    print('Write how many grams of coffee beans do you want to add:')
    add_beans = int(input())
    print('Write how many disposable cups of coffee do you want to add:')
    add_disposable_cups = int(input())
    fill_amounts_of_machine()

if user_choice == 'take':
    money_counter = 0
    while money_counter < amount_money:
        money_counter += 1
    print('I gave you $', money_counter)
    print()
    print()
    take_money_from_machine()
