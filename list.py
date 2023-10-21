AGE=["12","14","35","20","19"]
print(AGE)
Food=["pizza","fries","burger"]
print(Food)
Colors=["red","grey","purple"]
print(Colors)

#Hetrogenous list
names=("Fatima","45")
print(names)

#repitition operator * to repeat data
Colors=["grey","orange","blue"]
new_colors=Colors * 4
print(new_colors)

#positive indexing
numbers=[4,5,6,7,8,9]
print(numbers[2])

#negative indexing
numbers=[7,4,3,9,2]
print(numbers[-3])

#lens function
Names=["fatima","Ali","Abrar"]
print("number of elements in a list:",len(Names))

#mutability(changeable)
numbers=[7,9,8,7,6,5]
numbers[0]=3
numbers[1]=6
print(numbers)

#concatenation
list_1=[6,4,5,8]
list_2=[3,4,2,1]
list_3=[0,9,8,7]
list_4=[6,7,8,1]

list_5=list_1+list_2+list_3+list_4
print(list_5)

#list slicing
new_list=[1,4,5,6,7,8,9]
result=new_list[1:4]
print(result)

#find elements in list
list=[3,5,6,7,8,9]
if 6 in list:
    print("found")
else:
    print("not found")
    
names=["shahida","salwa"]
if "fatima" in names:
    print("yes")
else:
    print("no")