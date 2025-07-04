from art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n2 * n1

def divide(n1, n2):
    return n1 / n2

methods = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(logo)
    calculating = True
    result = None

    while calculating:
        if result is None:
            try:
                num1 = int(input("Enter first number: "))
            except ValueError:
                print("❌ Invalid input. Please enter a number.")
                continue
        else:
            num1 = result
            print(f"\nContinuing with result: {result}")

        print("Available operations:", " ".join(methods.keys()))
        operation = input("Pick an operation: ")

        if operation not in methods:
            print("❌ Invalid operation. Try again.")
            continue

        try:
            num2 = float(input("Enter next number: "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.")
            continue

        result = methods[operation](num1, num2)

        print(f"\n🧮 {num1} {operation} {num2} = {result}")

        next_action = input("\nType 'y' to continue with result, 'ac' to clear, or 'n' to exit: ").lower()

        if next_action == 'n':
            calculating = False
            print("👋 Goodbye!")
        elif next_action == 'ac':
            result = None  # reset
        elif next_action != 'y':
            print("❓ Unrecognized input. Exiting.")
            break

calculator()