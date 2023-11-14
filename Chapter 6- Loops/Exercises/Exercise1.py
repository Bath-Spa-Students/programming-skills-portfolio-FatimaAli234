#Write a loop that prompts the user to enter a series of pizza toppings until they enter a 'quit' value. As they enter each topping,
# print a message saying you’ll add that topping to their pizza.

pizza=True
while pizza:
    Topping=input("Enter a pizza topping(or 'quit' to finish):")
    if Topping.lower()=='quit':
        print("Quitting.your pizza is ready!")
        pizza=False
    else:
     print(f"Adding {Topping} to your pizza")
    