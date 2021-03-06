class CoffeeMachine:

    def __init__(self):
        self.water = 400
        self.milk = 540
        self.coffee = 120
        self.cup = 9
        self.money = 550

    def enough_resources(self):
        if self.water < 0:
            print('Sorry, not enough water!')
            return False
        elif self.milk < 0:
            print("Sorry, not enough milk!")
            return False
        elif self.coffee < 0:
            print("Sorry, not enough coffee bean!")
            return False
        elif self.cup < 0:
            print("Sorry, not enough cup!")
            return False
        else:
            return True

    def espresso(self):
        self.water -= 250
        self.coffee -= 16
        self.money -= 4
        self.cup -= 1
        if self.enough_resources():
            print('I have enough resources, making you a coffee!')
        else:
            self.water += 250
            self.coffee += 16
            self.money += 4
            self.cup += 1

    def latte(self):
        self.water -= 350
        self.coffee -= 20
        self.milk -= 75
        self.money += 7
        self.cup -= 1

        if self.enough_resources():
            print("I have enough resources, making you a coffee!")
        else:
            self.water += 350
            self.coffee += 20
            self.milk += 75
            self.money -= 7
            self.cup += 1

    def cappuccino(self):
        self.water -= 200
        self.coffee -= 12
        self.milk -= 100
        self.money += 6
        self.cup -= 1

        if self.enough_resources():
            print("I have enough resources, making you a coffee!\n")
        else:
            self.water += 200
            self.coffee += 12
            self.milk += 100
            self.money -= 6
            self.cup += 1

    def remaining(self):
        print(f"""\nThe coffee machine has:
{self.water} of water
{self.milk} of milk
{self.coffee} of coffee beans
{self.cup} of disposable cups
${self.money} of money\n""")

    def take(self):
        take_money = self.money
        print(f'I gave you ${take_money}')
        self.money = 0
        return take_money

    def fill(self):
        add_water = int(input("Write how many ml of water do you want to add:\n"))
        add_milk = int(input("Write how many ml of milk do you want to add:\n"))
        add_coffee = int(input("Write how many grams of coffee beans do you want to add:\n"))
        add_cup = int(input("Write how many disposable cups of coffee do you want to add:\n"))
        self.water += add_water
        self.milk += add_milk
        self.coffee += add_coffee
        self.cup += add_cup

    def buy(self):
        coffee_type = input("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:\n")
        if coffee_type == "1":
            self.espresso()
        elif coffee_type == "2":
            self.latte()
        elif coffee_type == "3":
            self.cappuccino()
        elif coffee_type == "back":
            pass
        else:
            pass

    def interact(self, _action):
        if _action == 'take':
            self.take()
            return True
        elif _action == 'buy':
            self.buy()
            return True
        elif _action == 'fill':
            self.fill()
            return True
        elif _action == 'remaining':
            self.remaining()
            return True
        elif _action == 'exit':
            return False
        else:
            return True


continuation = True
coffee_machine = CoffeeMachine()

while continuation:
    action = input('\nWrite action (buy, fill, take, remaining, exit):\n')
    continuation = coffee_machine.interact(action)
