#Assume the lists numbers1 has 100 elements and numbers2 is an empty list. Write code that copies the values in numbers to numbers2.

number1 = list(range(1, 101))
number2 = number1[:]
print(number2)
