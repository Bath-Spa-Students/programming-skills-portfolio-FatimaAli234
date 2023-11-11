
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

    
       
    