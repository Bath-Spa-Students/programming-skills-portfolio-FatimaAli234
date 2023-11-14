#Write a Python program that uses the elif statement to determine the season based on the month provided as input.


#Taking input from user
month = input("Enter the month here:")

if month in ["January", "February", "December"]:
    season = "Winter"
elif month in ["June", "July", "August"]:
    season = "Summer"
elif month in ["March", "April", "May"]:
    season = "Spring"
elif month in ["September", "October", "November"]:
    season = "Fall"
else:
    season = "Invalid month"

print(f"The {season} season is in {month}.")

    

