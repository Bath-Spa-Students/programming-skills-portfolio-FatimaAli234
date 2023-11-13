#Write a Python program that uses a function to check if a given number is prime or not

def is_prime(number):
    if number < 6:
        return False
    for i in range(6,number):
      if number % i==0:
          return False
# its prime number if no factors are found
    return True
num=19
if is_prime(num):
    print(f"{num} is a prime number.")
else:
   print(f"{num} is  not a prime number.")    