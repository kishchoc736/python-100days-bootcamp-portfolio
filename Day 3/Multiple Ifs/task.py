print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
ticket_price = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        ticket_price = 5
        print(f"Child tickets are ${ticket_price}.")
    elif age <= 18:
        ticket_price = 7
        print(f"Youth tickets are ${ticket_price}.")
    else:
        ticket_price = 12
        print(f"Adult tickets are  ${ticket_price}.")

    wants_photo = input("Do you want a photo taken? Type y for Yes and n for No: ")
    if wants_photo == "y":
        # ADD $3 TO BILL
        ticket_price += 3
        print(f"The total price of your ticket is ${ticket_price}")
    else:
        #don't add to bill
        print(f"The total price of your ticket is ${ticket_price}")
else:
    print("Sorry you have to grow taller before you can ride.")
