
Sandwich_orders = ["chicken sandwich", "Egg sandwich", "Grilled cheese"]
finished_Sandwiches = []
while Sandwich_orders:
    current_order = Sandwich_orders.pop()
    print(f"I made your {current_order}")
    finished_Sandwiches.append(current_order)
print("\nFinished Sandwiches:")
for sandwich in finished_Sandwiches:
    print(sandwich.title())
