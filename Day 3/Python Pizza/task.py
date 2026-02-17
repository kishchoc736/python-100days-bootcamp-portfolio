print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M or L: ")
pepperoni = input("Do you want pepperoni on your pizza? Y or N: ")
extra_cheese = input("Do you want extra cheese? Y or N: ")
total_cost = 0

if size == "S":
    total_cost += 15
elif size == "M":
    total_cost+= 20
elif size == "L":
    total_cost += 25

# todo: work out how much to add to their bill based on pepperoni choce
if pepperoni == "Y":
    if size == "S":
        total_cost += 2
    else:
        total_cost += 3


# todo: work out additional coast based on extra cheese selection
if extra_cheese == "Y":
    total_cost += 1

print(f"Your final bill is: ${total_cost}.")


