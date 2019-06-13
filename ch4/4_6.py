#Exercise 4.6 Rewrite your pay computation with time-and-a-half for overtime
#and create a function called computepay which takes two parameters (hours and
#rate).
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

def computegrade(score):
    if score > 1.0:
        print 'Bad score'
        exit()
    if score >= 0.9:
        print 'A'
        exit()
    if score >= 0.8:
        print 'B'
        exit()
    if score >= 0.7:
        print 'C'
        exit()
    if score >= 0.6:
        print 'D'
        exit()
    if score < 0.6:
        print 'F'
        exit()


score = raw_input("Enter Score: ")
try: 
    score = float(score)
except:
    print 'Bad score'
    exit()
computegrade(score)
