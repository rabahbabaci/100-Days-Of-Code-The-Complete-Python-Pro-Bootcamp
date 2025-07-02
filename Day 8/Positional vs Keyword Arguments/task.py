# Functions with input

def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

def greet_with(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

greet_with_name("Jack Bauer")
#Calling using keyword arguments
greet_with(location="San Francisco", name="Rab")
