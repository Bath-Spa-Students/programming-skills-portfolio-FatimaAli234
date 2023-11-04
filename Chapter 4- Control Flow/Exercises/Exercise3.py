#Turn your if-else chain from Exercise 5-4 into an if-elifelse chain.
# •	 If the alien is green, print a message that the player earned 5 points.
# •	 If the alien is yellow, print a message that the player earned 10 points.
# •	 If the alien is red, print a message that the player earned 15 points.
# •	 Write three versions of this program, making sure each message is printed for the appropriate color alien.


Alien_color='green'
if Alien_color=='green':
    print("The player earned 5 points for shooting the green alien")
elif Alien_color=='yellow':
    print("The player earned 10 points for shooting the yellow alien")
else:
    print("The player earned 15 points for shooting the red alien")
    
#version 2
Alien_color='yellow'
if Alien_color=='green':
    print("The player earned 5 points for shooting the green alien")
elif Alien_color=='yellow':
    print("The player earned 10 points for shooting the yellow alien")
else:
    print("The player earned 15 points for shooting the red alien")
    
#version 3
Alien_color='Red'
if Alien_color=='green':
    print("The player has earned 5 points for shooting green alien")
elif Alien_color=='Yellow':
    print("The player earned for shooting the yellow alien")
else:
    print("The player earned 15 points for shooting red alien")