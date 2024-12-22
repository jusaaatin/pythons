title = " Pizzas ".center(24, "*")
pizzas = ["pepperoni", "cheese", "margherita", "hawaiian", "meat lovers"]
prices = [8.99, 7.99, 9.99, 12.99, 9.99]
pizzaTotal = pizzas + prices

def printMenu():
    print(title)
    for i in range(len(pizzas)):
        print("* " + pizzaTotal[i].ljust(14, ".") + str(pizzaTotal[i+len(pizzas)]).rjust(6) + " *")
    print("*" * 24)
def pizzaAsker():
    PizzaBuyingInput = str(input("""Enter the pizza you want to buy, request menu with "menu", or exit with "exit"\n"""))
    NilCounter = 0
    if len(PizzaBuyingInput) > 0:
        if PizzaBuyingInput == "menu":
            printMenu()
        elif PizzaBuyingInput == "exit":
            print("Goodbye!")
            exit()
        else:
            print("-" * 24)
            for i in range(len(pizzas)):
                if PizzaBuyingInput == pizzas[i]:
                    print("You have selected " + str(pizzas[i]))
                    print("Price: " + str(prices[i]))
                else: NilCounter += 1
            if NilCounter == 0:
                print("Invalid pizza selection")
    print("-" * 24)


printMenu()
while True:
    pizzaAsker()
        

