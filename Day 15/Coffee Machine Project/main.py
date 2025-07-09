MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

profit = 0  # 🆕 global tracker for money in the machine

def format_list_naturally(items):
    if len(items) == 0:
        return ""
    elif len(items) == 1:
        return items[0]
    elif len(items) == 2:
        return f"{items[0]} and {items[1]}"
    else:
        return f"{', '.join(items[:-1])} and {items[-1]}"

def report():
    print()
    for res, amount in resources.items():
        unit = "g" if res == "coffee" else "ml"
        print(f"{res.capitalize()}: {amount}{unit}")
    print(f"Money: ${profit:.2f}\n")

def check_resources(drink):
    missing_ing = []
    for ing, quantity in drink["ingredients"].items():
        if quantity > resources.get(ing, 0):
            missing_ing.append(ing)
    return missing_ing

def process_coins():
    print("Please insert coins.")
    quarters = int(input("How many quarters?: ")) * 0.25
    dimes = int(input("How many dimes?: ")) * 0.10
    nickles = int(input("How many nickles?: ")) * 0.05
    pennies = int(input("How many pennies?: ")) * 0.01
    return round(quarters + dimes + nickles + pennies, 2)

def check_transaction(balance, drink_cost):
    return balance >= drink_cost

def get_change(balance, drink_cost):
    return round(balance - drink_cost, 2)

def update_resources(drink):
    for ing, quantity in drink["ingredients"].items():
        resources[ing] -= quantity

def open_cafe():
    global profit
    cafe_closed = False

    while not cafe_closed:
        order = input("What would you like? (espresso/latte/cappuccino): ").lower()

        if order == "off":
            print("\nShutting down for maintenance. ☕ See you soon!\n")
            cafe_closed = True
        elif order == "report":
            report()
        elif order in MENU:
            drink = MENU[order]
            missing_ing = check_resources(drink)

            if missing_ing:
                print(f"\nSorry, there is not enough {format_list_naturally(missing_ing)}.\n")
            else:
                balance = process_coins()

                if check_transaction(balance, drink["cost"]):
                    change = get_change(balance, drink["cost"])
                    profit += drink["cost"]  # 🆕 add profit
                    update_resources(drink)
                    print(f"\nHere is ${change:.2f} in change.")
                    print(f"Here is your {order} ☕️. Enjoy!\n")
                else:
                    print("\nSorry, that's not enough money. Money refunded.\n")
        else:
            print("❌ Invalid input. Please choose from espresso, latte, cappuccino, report, or off.\n")

# Start the coffee machine
open_cafe()
