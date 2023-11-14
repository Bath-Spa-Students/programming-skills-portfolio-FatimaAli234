#Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. Add code
#near the beginning of your program to print a message saying the deli has run out of pastrami, and then use a while loop to remove all 
#occurrences of 'pastrami' from sandwich_orders. Make sure no pastrami sandwiches end up in finished_sandwiches.

Sandwich_orders = ["chicken sandwich", "pastrami", "Egg sandwich", "pastrami", "Grilled cheese", "pastrami"]
finished_sandwiches = []
print("Sorry, The Deli has run out of pastrami sandwiches.")
while "pastrami" in Sandwich_orders:
    Sandwich_orders.remove("pastrami")
while Sandwich_orders:
    current_order = Sandwich_orders.pop(0)
    print(f"I made your {current_order}.")
    finished_sandwiches.append(current_order)
print("\nFinished sandwiches:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
