import art

# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary

print(art.logo)

bidding = True
bids = {}

while bidding:
    name = input("What is your name?: ")
    bid = input("What's your bid?: ")
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")

    bids[name] = int(bid[1:])

    if more_bidders == "no":
        bidding = False

winner = [0, ""]
for name, bid in bids.items():
    if bid > winner[0]:
        winner[0] = bid
        winner[1] = name
print(f"Winner is: {winner[1]} with a bid of: ${winner[0]}")
