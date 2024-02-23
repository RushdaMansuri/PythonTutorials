# Write a program to ask user enter number till he enters 0 and than sum all the numbers he entered


total = 0
while True:
    num = int(input("Please enter:"))

    if num == 0:
        break
    total += num
print(total)
