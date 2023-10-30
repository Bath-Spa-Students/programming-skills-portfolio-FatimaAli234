
invitees=["Aisha","Sara","Humera","Eshal","Saba"]
guest_cant_make_it="Saba"
print(f"{guest_cant_make_it} cant make it to the dinner.\n")
replacement_guest="rida"
invitees[invitees.index(guest_cant_make_it)]=replacement_guest
for person in invitees:
    print(f"Dear{person},you are invited to dinner at my place.please join us on (20 may) at (7:30 pm).\n\n sincerely,(fatima)\n")
