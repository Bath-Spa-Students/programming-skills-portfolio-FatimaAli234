#Write a Python function that calculates the factorial of a given positive integer using recursion

def factorial(x):
    if x==0 or x==1:
        return 1
#multiply
    else:
        return x * factorial(x-1)
#set the value for factorial
number=19
result=factorial(number)
#print the result
print(f"The factorial of {number} is {result}")