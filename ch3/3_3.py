#Exercise 3.3 Write a program to prompt for a score between 0.0 and 1.0. If the
#score is out of range print an error. If the score is between 0.0 and 1.0, print a
#grade using the following table:
#Score Grade
#>= 0.9 A
#>= 0.8 B
#>= 0.7 C
#>= 0.6 D
#< 0.6 F
#Enter score: 0.95
#A
#Enter score: perfect
#Bad score
#Enter score: 10.0
#Bad score
#Enter score: 0.75
#C
#Enter score: 0.5
#F

grade = raw_input("Enter score: ")

try:
    grade = float(grade)
except:
    print "Bad score"
    exit()
if (grade >= 0 and grade <= 1):
    if grade >= 0.9:
       print "A"
       exit()
    if grade >= 0.8:
        print "B"
        exit()
    if grade >= 0.7:
        print "C"
        exit()
    if grade >= 0.6:
        print "D"
        exit()
    if grade < 0.6:
        print "F"
        exit()
else:
    print "Bad score"
