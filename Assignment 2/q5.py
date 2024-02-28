# Write a program to calculate bill. Ask the final amount from the user.
# You have to give discount and print the final bill after discount.
# 50000 above - 30% discount
# 40000 - 49999 - 25% discount
# 30000 - 39999 - 20% discount
# 10000 - 29999 - 10% discount
# 1 - 9999 - No discount
# Print the discount and the final amount to be paid.

amount = int(input("Enter the final amount: "))

discount = 0
if amount >= 50000:
    discount = 0.3 * amount
elif amount >= 40000 and amount <= 49999:
    discount = 0.25 * amount
elif amount >= 30000 and amount <= 39999:
    discount = 0.2 * amount
elif amount >= 10000 and amount <= 29999:
    discount = 0.1 * amount
else:
    discount = 0

finalAmount = amount - discount
print(
    "On",
    amount,
    "you got discount of",
    discount,
    "which makes your final amount",
    round(finalAmount, 2),
)
