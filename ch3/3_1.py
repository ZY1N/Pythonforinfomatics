#Exercise 3.1 Rewrite your pay computation to give the employee 1.5 times the
#hourly rate for hours worked above 40 hours.
#Enter Hours: 45
#Enter Rate: 10
#Pay: 475.0

hour = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")

hour = float(hour)
rate = float(rate)
if hour > 40:
    over = hour - 40
    print "Pay :", (rate * 40) + (1.5 * rate * over)
else:
    print "Pay :", rate * hour
