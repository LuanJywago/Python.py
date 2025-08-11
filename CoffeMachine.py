# Ingredientes iniciais
ingredients = {
    "water": 1000,         # ml
    "milk": 500,           # ml
    "coffee_beans": 200    # g
}

# Menu de cafés e receitas
coffee_menu = {
    "espresso": {
        "water": 50,
        "milk": 0,
        "coffee_beans": 18,
        "price": 1.50
    },
    "latte": {
        "water": 200,
        "milk": 150,
        "coffee_beans": 24,
        "price": 2.50
    },
    "cappuccino": {
        "water": 250,
        "milk": 100,
        "coffee_beans": 18,
        "price": 3.00
    }
}

# Funções utilizadas no programa
def report():
    print("\n--- REPORT ---")
    for item, amount in ingredients.items():
        print(f"{item.capitalize()}: {amount}")
    print("--------------\n")

def process_coins():
    print("Please insert coins:")
    quarters = int(input("How many quarters? ($0.25): "))
    dimes = int(input("How many dimes? ($0.10): "))
    nickels = int(input("How many nickels? ($0.05): "))
    pennies = int(input("How many pennies? ($0.01): "))

    total = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01
    return total


def make_coffee(coffee_type):
    recipe = coffee_menu[coffee_type]


    for item in ["water", "milk", "coffee_beans"]:
        if ingredients[item] < recipe[item]:
            print(f"Not enough {item}. Please refill.")
            return


    payment = process_coins()
    if payment < recipe["price"]:
        print("Not enough money. Money refunded.")
        return
    else:
        change = round(payment - recipe["price"], 2)
        if change > 0:
            print(f"Here is ${change} in change.")


    for item in ["water", "milk", "coffee_beans"]:
        ingredients[item] -= recipe[item]

    print(f"☕ Making {coffee_type.capitalize()}... Enjoy!")


def refill_machine():
    print("\n--- REFILL INGREDIENTS ---")
    water_add = int(input("Add water (ml): "))
    milk_add = int(input("Add milk (ml): "))
    beans_add = int(input("Add coffee beans (g): "))

    ingredients["water"] += water_add
    ingredients["milk"] += milk_add
    ingredients["coffee_beans"] += beans_add

    print("✅ Ingredients refilled successfully!\n")

# Loop e visualização principal do Sistema de Café
print("Welcome to the Coffee Machine!")
while True:
    action = input("What would you like? (espresso/latte/cappuccino/report/refill/exit): ").lower()

    if action in coffee_menu:
        make_coffee(action)
    elif action == "report":
        report()
    elif action == "refill":
        refill_machine()
    elif action == "exit":
        break
    else:
        print("Invalid option.")
