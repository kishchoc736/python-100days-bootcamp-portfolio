# TODO-1: Ask the user for input

# first_bidder_name = input("What is your name?: ")

any_more_bidders = True
auction_dictionary = {}

while any_more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $ "))
    auction_dictionary[name] = bid

    extra_bidders = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
    if extra_bidders == "no":
        any_more_bidders = False
    elif extra_bidders == "yes":
        print("\n" * 20)

print(auction_dictionary)

# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary
highest_bid = 0
winner = ""
for key in auction_dictionary:
    if auction_dictionary[key]>=highest_bid:
        highest_bid = auction_dictionary[key]
        winner = key
print(f"The winner is {winner} with a bid of ${highest_bid}")


