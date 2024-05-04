budget = 50
price_per_usb = 6

# Calculate how many USB sticks she can buy with £50
number_of_usbs = budget // price_per_usb

# Calculate how many pounds she will have left
remaining_money = budget % price_per_usb

# Print the result

print(f"She can buy {number_of_usbs} USB sticks and She'll have £{remaining_money} left.")