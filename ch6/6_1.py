#Exercise 6.1 Write a while loop that starts at the last character in the string and
#works its way backwards to the first character in the string, printing each letter on
#a separate line, except backwards.



i = 0

string = raw_input("Enter a string: ")
length = len(string) - 1

while length >= 0:
    print string[length]
    length = length - 1
