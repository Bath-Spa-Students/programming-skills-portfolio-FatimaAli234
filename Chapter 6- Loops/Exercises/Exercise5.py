
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
