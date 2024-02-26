# A student will not be allowed to sit in exam if his/her attendance is less than 75%
# Take following input from user
# -> Number of classes held
# -> Number of classes attended.
# 1. Print percentage of class attended
# 2. Print Is student is allowed to sit in exam or not.

noOfClassesHeld = int(input("Enter the number of classes held: "))
noOfClassesAttended = int(input("Enter the number of classes attended: "))

classAttended = (noOfClassesAttended / noOfClassesHeld) * 100

if classAttended < 75:
    print("Student is not allowed to sit in exam as his attendance is", classAttended)
else:
    print("Student is allowed to sit in exam as his attendance is", classAttended)
