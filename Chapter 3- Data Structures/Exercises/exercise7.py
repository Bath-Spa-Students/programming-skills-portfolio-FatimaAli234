#Think of at least five places in the world you’d like to visit.
#•	 Store the locations in a list. Make sure the list is not in alphabetical order.
#•	 Print your list in its original order. Don’t worry about printing the list neatly,just print it as a raw Python list.
#•	 Use sorted() to print your list in alphabetical order without modifying the actual list.
#•	 Show that your list is still in its original order by printing it.
#•	 Use sorted() to print your list in reverse alphabetical order without changing the order of the original list.
#•	 Show that your list is still in its original order by printing it again.
#•	 Use reverse() to change the order of your list. Print the list to show that its order has changed.
#•	 Use reverse() to change the order of your list again. Print the list to show it’s back to its original order.
#•	 Use sort() to change your list so it’s stored in alphabetical order. Print the list to show that its order has been changed.
#•	 Use sort() to change your list so it’s stored in reverse alphabetical order. Print the list to show that its order has changed.



#list of places to visit
places_to_visit=["Tokyo","Venice","paris","Iceland","KSA"]

print("original order:",places_to_visit)
print("Alpahbetical order:",sorted(places_to_visit))
print("original order:",places_to_visit)
print("Reverse Alphabetical order:",sorted(places_to_visit,reverse=True))
print("original order:",places_to_visit)
places_to_visit.reverse()
print("Reversed order:",places_to_visit)
places_to_visit.reverse()
print("original order:",places_to_visit)
places_to_visit.sort()
print("Alphabetical order:",places_to_visit)
places_to_visit.sort(reverse=True)
print("Reverse alphabetical order:", places_to_visit)
