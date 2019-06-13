#Exercise 5.1 Write a program which repeatedly reads numbers until the user enters “done”. Once “done” is entered, print out the total, count, and average of
#the numbers. If the user enters anything other than a number, detect their mistake
#using try and except and print an error message and skip to the next number

count = 0
total = 0
average = 0

while True:
    num = raw_input("Enter a number: ")
    try:
        if num == 'done':
            print total, count, average
            break
        num = float(num)
    except:
        print "Invalid input"
        continue
    total = total + num
    count = count + 1
    average = total / count
