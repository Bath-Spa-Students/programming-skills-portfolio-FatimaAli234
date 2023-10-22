
invitees=["Aisha","Sara","Humera","Eshal","rida"]
print("i can invite only 2 people for dinner.\n")
for person in invitees:
    if len(invitees) > 2:
        removed_guest=invitees.pop()
        print(f"sorry, {removed_guest}, but i cant invite you to dinner this time. ")
        for person in invitees:
            print(f"Dear {person}\nyou are still invited to the dinner at my place on(20 may) at (7:30 pm)\n")
            del invitees[:2]
            print("my guest list is now empty",invitees)