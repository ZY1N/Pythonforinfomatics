#Exercise 6.3 Encapsulate this code in a function named count, and generalize it
#so that it accepts the string and the letter as arguments.

def lettercount (string, let):
    count = 0
    for letter in string:
            if letter == let:
                count = count + 1
    print count

string = raw_input("Enter string: ")
let = raw_input("Enter letter: ")

lettercount(string, let)
