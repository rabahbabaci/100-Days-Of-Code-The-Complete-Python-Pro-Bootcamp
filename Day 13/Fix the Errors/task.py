try:
    age = int(input("How old are you? "))
except ValueError:
    print("User typed an invalid number")
    age = int(input("How old are you? "))

if age > 18:
    print("You can drive at age {age}.")
