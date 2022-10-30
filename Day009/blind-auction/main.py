from replit import clear
# HINT: You can call clear() to clear the output in the console.
from art import logo

bids = {}
other_users = True
while other_users:
    clear()
    print(logo)
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))
    bids[name] = bid
    repeat = input("Are there more bidders? (yes/no) ").lower()
    if repeat == "no":
        other_users = False

high_bidder = ''
highest_bid = 0
for name in bids:
    if bids[name] > highest_bid:
        high_bidder = name
        highest_bid = bids[name]

print(f"{high_bidder} is the winner with a bid of ${highest_bid}")
