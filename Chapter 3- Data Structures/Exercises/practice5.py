#You have given a Python list. Write a program to find value 20 in the list, and if it is present, 
# replace it with 200. Only update the first occurrence of an item.Work with the given list:
# list1 = [5, 10, 15, 20, 25, 50, 20]

list= [5, 10, 15, 20, 25, 50, 20]
list[list.index(20)]=200
print(list)