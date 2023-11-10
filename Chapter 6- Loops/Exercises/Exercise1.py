
pizza=True
while pizza:
    Topping=input("Enter a pizza topping(or 'quit' to finish):")
    if Topping.lower()=='quit':
        print("Quitting.your pizza is ready!")
        pizza=False
    else:
     print(f"Adding {Topping} to your pizza")
    