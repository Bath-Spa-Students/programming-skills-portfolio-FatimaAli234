
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

    

