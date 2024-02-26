# Write a Python program that takes a student's score as input and
# prints the corresponding grade. Use the following grading scale:
# A: 90-100
# B: 80-89
# C: 70-79
# D: 60-69
# F: Below 60

score = int(input("Enter your score: "))

if score >= 90 and score <= 100:
    print("A grade")
elif score >= 80 and score <= 89:
    print("B grade")
elif score >= 70 and score <= 79:
    print("C grade")
elif score >= 60 and score <= 69:
    print("D grade")
else:
    print("F grade")
