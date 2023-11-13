#Write a Python program that defines a function to check whether a given number is prime

def prime_num(number):
    if number < 5:
        return False
    for i in range(5,number):
        if number % i==0:
            return False
    return True
user_number=int(input("Enter a number here:"))
if prime_num(user_number):
    print(f"{user_number} is a prime number")
else:
    print(f"{user_number} is not a prime number")
    
