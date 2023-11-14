#Make several dictionaries, where each dictionary represents a different pet. In each dictionary, include the kind of animal and the
# owner’s name. Store these dictionaries in a list called pets. Next, loop through your list and asyou do, print everything you know about 
# each pet

Pets=[
    {"kind":"Cat", "Owner":"Fatima"},
    {"kind":"snake","Owner":"Sara"},
    {"kind":"Fish","Owner":"Alisa"},
    {"kind":"Dog","Owner":"lana"},
]

for Animal in Pets:
    print(f"kind of Animal:{Animal['kind']}")
    print(f"Owners name:{Animal['Owner']}")