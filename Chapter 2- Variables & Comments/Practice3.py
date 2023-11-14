#Write a python program that takes an input 5 from user and then type cast those values to string, int 
#and float in the separate variables. Print all the variables.


User_input = input("Enter your Value here:")
#convert the user input into string
String = str(User_input)
#convert the user input into integer
integer = int(User_input)
#convert the user input into float
Float = float(User_input)

#print the user input as original ,string,float and integer
print("Original input:", User_input)
print("String Variable:", String)
print("Integer Variable:", integer)
print("Float Variable:", Float)
