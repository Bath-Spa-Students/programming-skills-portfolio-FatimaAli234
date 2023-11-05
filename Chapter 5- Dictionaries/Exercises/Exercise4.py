
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