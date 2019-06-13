#Exercise 2.3 Write a program to prompt the user for hours and rate per hour to
#compute gross pay.
#Enter Hours: 35
#Enter Rate: 2.75
#Pay: 96.25

hours = raw_input('Enter Hours:')
rate = raw_input('Enter Rate:')
hours = float (hours)
rate = float(rate)
print 'Pay:', hours * rate
