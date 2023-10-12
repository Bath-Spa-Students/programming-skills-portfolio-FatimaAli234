#Write a Python program which accepts the radius of a circle from the user and compute the area.
import math

if __name__ == "__main__":
    try:
        radius = float(input("Enter the radius of the circle: "))

        if radius < 0:
            print("Radius cannot be negative. Please enter a non-negative value.")
        else:
            area = math.pi * (radius ** 2)
            print("The area of the circle is:", area)
    except ValueError:
        print("Invalid input. Please enter a valid numeric value for the radius.")

