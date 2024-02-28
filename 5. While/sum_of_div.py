# Write a program to return total of sum that is divisible by n2.
# n1 = 63, n2 = 3;
# use while loop from 1 to n1, than find numbers that are divisble by n2 and sum all those numbers together


def sum_of_div(n1: int, n2: int) -> int:
    total: int = 0
    i: int = 1
    while i <= n1:
        if i % n2 == 0:
            total += i
        i += 1
    return total


sum = sum_of_div(100, 8)
print(f"sum is {sum}")
