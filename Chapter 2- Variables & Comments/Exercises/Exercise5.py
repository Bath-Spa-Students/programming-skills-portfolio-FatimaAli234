#A girl heads to a computer shop to buy some USB sticks. She loves USB sticks and wants as many as she can get for £50. They are £6 each.
#Write a programme that calculates how many USB sticks she can buy and how many pounds she will have left.
#You will to use the arithmetic operators to complete this exercise.


USB_stick_cost=6
money=50
num_USB_sticks=money // USB_stick_cost
money_left=money % USB_stick_cost
print("Number of USB sticks she can buy:", num_USB_sticks)
print("Pounds left:", money_left)