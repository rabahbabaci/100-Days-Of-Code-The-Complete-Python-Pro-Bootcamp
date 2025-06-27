print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want?\n"
            "Small pizza Enter(S) $15\n"
             "Medium pizza Enter(M) $20\n"
             "Large pizza Enter(L) $25\n"
             "===> ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N +$2: ")
extra_cheese = input("Do you want extra cheese? Y or N +$3: ")

bill = 0
if size == "S":
    bill = 15
elif size == "M":
    bill = 20
elif size == "L":
    bill = 25

if pepperoni == "Y":
    bill += 2
if extra_cheese == "Y":
    bill += 3

print(f"Your final bill is: ${bill}")

