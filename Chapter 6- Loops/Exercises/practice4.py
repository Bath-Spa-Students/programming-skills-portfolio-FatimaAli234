#Write a Python program that uses the break statement to exit a for loop when a specific condition is met.

for numbers in range(1,15):
    print(numbers)
    if numbers==7:
        print("breaking the loop at number 7.")
        break