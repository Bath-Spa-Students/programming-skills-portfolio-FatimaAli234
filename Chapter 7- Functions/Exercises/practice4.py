#Write a Python program that defines a function to calculate the area of a circle, and then calls that function with a given radius

import math
def circle_radius(radius):
    area=math.pi * radius **2
    return area
radius=33
#result
area_result=circle_radius(radius)
print(f"The area of a circle with radius {radius} is {area_result}")
    