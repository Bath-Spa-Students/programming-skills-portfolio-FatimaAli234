#Make a list called sandwich_orders and fill it with the names of various sandwiches. Then make an empty list called finished_sandwiches.
#Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich. As each sandwich is made, 
#move it to the list of finished sandwiches. After all the sandwiches have been made, print a message listing each sandwich that was made.


Sandwich_orders = ["chicken sandwich", "Egg sandwich", "Grilled cheese"]
finished_Sandwiches = []
while Sandwich_orders:
    current_order = Sandwich_orders.pop()
    print(f"I made your {current_order}")
    finished_Sandwiches.append(current_order)
print("\nFinished Sandwiches:")
for sandwich in finished_Sandwiches:
    print(sandwich.title())
