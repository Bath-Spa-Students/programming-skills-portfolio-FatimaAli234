#You just heard that one of your guests can’t make the
#dinner, so you need to send out a new set of invitations. You’ll have to think of
#someone else to invite.
#•Start with your program from Exercise 3-4. Add a print() call at the end of your program stating the name of the guest who can’t make it.
#•Modify your list, replacing the name of the guest who can’t make it with the name of the new person you are inviting.
#•Print a second set of invitation messages, one for each person who is still in your list.


#list of invitees
invitees=["Aisha","Sara","Humera","Eshal","Saba"]
guest_cant_make_it="Saba"
print(f"{guest_cant_make_it} cant make it to the dinner.\n")
replacement_guest="rida"
invitees[invitees.index(guest_cant_make_it)]=replacement_guest
for person in invitees:
    print(f"Dear{person},you are invited to dinner at my place.please join us on (20 may) at (7:30 pm).\n\n sincerely,(fatima)\n")
