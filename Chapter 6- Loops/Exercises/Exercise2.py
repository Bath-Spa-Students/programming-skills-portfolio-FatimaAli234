#A movie theater charges different ticket prices depending on a person’s age. If a person is under the age of 3, the ticket is free; if
# they are between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is $15. Write a loop in which you ask users their 
# age, and then tell them the cost of their movie ticket


while True:
    Age = input("Enter your age (or 'quit' to finish):")

    if Age.lower() == 'quit':
        print('Quitting. Thank you for using the Ticket services')
        break

    Ticket = int(Age)

    if Ticket < 3:
        ticket_price = 0
    elif 3 <= Ticket <= 12:
        ticket_price = 10
    else:
        ticket_price = 15
        print(f"The cost of the movie ticket is ${ticket_price}")

    
       
    