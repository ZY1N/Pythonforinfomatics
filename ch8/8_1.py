#Exercise 8.1 Write a function called chop that takes a list and modifies it, removing the first and last elements, and returns None.

def chop(t):
    length = len(t)
    del t[0]
    del t[length - 2]
    return None

list1 = [1, 2, 3, 4, 5]
print list1
chop(list1)
print list1


#Then write a function called middle that takes a list and returns a new list that
#contains all but the first and last elements.

def middle(t):
    length = len(t) - 1
    return t[1:length]

letters = ['a','b','c']
print letters
mid = middle(letters)
print mid


