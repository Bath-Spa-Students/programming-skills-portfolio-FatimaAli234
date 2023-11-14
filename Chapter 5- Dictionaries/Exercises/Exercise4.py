#Make a dictionary containing three major rivers and the country each river runs through. One key-value pair might be 'nile': 'egypt'.
#* Use a loop to print a sentence about each river, such as The Nile runs through Egypt.
#* Use a loop to print the name of each river included in the dictionary.
#* Use a loop to print the name of each country included in the dictionary.

Rivers= {
    "Nile":"Egypt",
    "Amazon":"Brazil",
    "yangtze":"China",
}

for River, country in Rivers.items():
    print(f"The {River} flows through {country}.")
    
print("\nRiver:\n")
for River in Rivers.keys():
    print(River)
    
    
print("\nCountry:\n")
for country in Rivers.values():
    print(country)