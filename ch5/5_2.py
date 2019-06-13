#Exercise 5.2 Write another program that prompts for a list of numbers as above
#and at the end prints out both the maximum and minimum of the numbers instead
#of the average.

maximum = None
minimum = None

while True:
    num = raw_input("Enter a number: ")
    try:
        if num == 'done':
            print "Max", maximum, "Min", minimum
            break
        num = float(num)
    except:
        print "Invalid input"
        continue
    if maximum is None:
        maximum = num
    if minimum is None:
        minimum = num
    if maximum < num:
        maximum = num
    if minimum > num:
        minimum = num
