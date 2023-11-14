#Write a Python program to merge two dictionaries into one

car1={"brand":"BMW","year":"2022"}
car2={"model":"x5","color":"Black"}
merge_car=car1.copy()
merge_car.update(car2)
print(" car:",merge_car)