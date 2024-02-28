# 1 3 6 8 11 13 16 18 21 23 .. upto N numbers


def pattern2(n):
    num = 1
    i = 1
    while i <= n:
        print(num)
        if i % 2 == 0:
            num += 3
        else:
            num += 2
        i += 1


pattern2(10)
