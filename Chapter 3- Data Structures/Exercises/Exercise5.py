# List of people i chose to invite
guests = ["J.Cole", "Drake", "Justin Bieber"]

# Printing a message to each person to invite them to dinner
for guest in guests:
    print(f"Dear {guest}, I would be honored if you could join me for dinner.")

# Printing a message with the name of the guest who won't be able make it
print("Unfortunately, one of our guests can’t make it to dinner.")

# Replacing the name of the guest who won't be able to make it with the name of the new person I'm inviting
guests[0] = "Bas"

# Printing a second set of invitation messages, one for each person who is still in my list
for guest in guests:
    print(f"Dear {guest}, I would be honored if you could join me for dinner.")
