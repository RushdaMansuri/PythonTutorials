# Write a program to sum the digits of entered number

number = int(input("Enter a number: "))
total = 0
while number > 0:
    dig = number % 10
    total = total + dig
    number = number // 10

print(total)
