#Write a Python program to iterate through both the keys and values of a dictionary and printthem 

cars={
    "brand":"BMW",
    "model":"x5",
    "color":"Black"
}
for key,value in  cars.items():
    print( f"{key}:{value}")