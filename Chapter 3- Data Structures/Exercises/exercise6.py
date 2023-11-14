#ou just found out that your new dinner table won’t arrive in time for the dinner, and you have space for only two guests.
#•Start with your program from Execise 3-5. Add a new line that prints a message saying that you can invite only two people for dinner.
#•Use pop() to remove guests from your list one at a time until only two names remain in your list. 
#Each time you pop a name from your list, print a message to that person letting them know you’re sorry you can’t invite them to dinner.
#•Print a message to each of the two people still on your list, letting them know they’re still invited.
#•Use del to remove the last two names from your list, so you have an empty list. Print your list to make sure you actually have an empty list at the end of your program.


invitees=["Aisha","Sara","Humera","Eshal","rida"]
print("i can invite only 2 people for dinner.\n")
for person in invitees:
 #check if the number of invitees is more than one  
    if len(invitees) > 2:
        removed_guest=invitees.pop()
        print(f"sorry, {removed_guest}, but i cant invite you to dinner this time. ")
        for person in invitees:
            print(f"Dear {person}\nyou are still invited to the dinner at my place on(20 may) at (7:30 pm)\n")
 #remove the first to people from invitees         
            del invitees[:2]
#print the updated guest list    
            print("my guest list is now empty",invitees)
