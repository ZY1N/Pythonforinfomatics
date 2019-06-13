#Exercise 3.2 Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the
#program. The following shows two executions of the program:
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input

try:
    hour = raw_input("Enter Hours: ")
    hour = float(hour)
except:
    print "Error, please enter numeric input"
    exit()

try:
    rate = raw_input("Enter Rate: ")
    rate = float(rate)
except:
    print "Error, please enter numeric input"
    exit()

if hour > 40:
    over = hour - 40
    print "Pay :", (rate * 40) + (1.5 * rate * over)
else:
    print "Pay :", rate * hour
