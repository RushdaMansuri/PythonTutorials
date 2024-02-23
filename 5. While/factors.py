# Write a program to find factor of number


def find_factor(n1: int) -> None:
    num = 1
    while num <= n1:
        if n1 % num == 0:
            print(num)
        num += 1


find_factor(10)


# Prime Number
def isPrime(n1: int) -> bool:
    return find_factor(n1) == 2


number = 5
if isPrime(number):
    print("It's prime number!!")
else:
    print("It's not prime number")
