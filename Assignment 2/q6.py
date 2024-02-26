# Ask 4 numbers from user. Make sure all the numbers entered by user
# are different. Print which number is the smallest.

num1 = int(input("Enter num1: "))
num2 = int(input("Enter num2: "))
num3 = int(input("Enter num3: "))
num4 = int(input("Enter num4: "))

smallest = num1

if num2 < smallest:
    smallest = num2
if num3 < smallest:
    smallest = num3
if num4 < smallest:
    smallest = num4

print(f"The smallest number = {smallest}")
