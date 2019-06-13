#Exercise 8.6 Rewrite the program that prompts the user for a list of numbers and
#prints out the maximum and minimum of the numbers at the end when the user
#enters done. Write the program to store the numbers the user enters in a list
#and use the max() and min() fuctions to compute the maximum and minimum
#numbers after the loop completes.

lis = []

while True:
    try:
        num = raw_input("Enter a number : ")
        if num == 'done':
            break
        num = float(num)
    except:
        print "Not a valid number"
        continue
    lis.append(num)

print "Max:", max(lis)
print "Min:", min(lis)
