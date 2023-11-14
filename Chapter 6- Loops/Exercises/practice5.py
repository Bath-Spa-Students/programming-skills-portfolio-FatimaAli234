#Write a Python program that uses a while loop to find the largest number among a series of 
#user-input values until they enter '0' to exit the loop.


largest_num = None

while True:
    user_input = input("Enter a number here (or type '0' to stop): ")
    if user_input == '0':
        break
    number = int(user_input)

    if largest_num is None or number > largest_num:
        largest_num = number

if largest_num is not None:
    print(f"The largest number entered is: {largest_num}")
else:
    print("No valid numbers are entered.")
