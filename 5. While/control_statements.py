# break (breaking the loop) and continue (skips the loop)

# Break
i = 1
while i <= 10:
    print(i, end=" ")
    if i == 5:
        break
    i += 1

# Continue
while i <= 10:
    i += 1
    if i == 5:
        continue
    print(i, end=" ")
    print("Done", end="")
