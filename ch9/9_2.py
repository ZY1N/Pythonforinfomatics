#Exercise 9.2 Dictionaries have a method called get that takes a key and a default
#value. If the key appears in the dictionary, get returns the corresponding value;
#otherwise it returns the default value. For example:

def histogram(s):
    d = dict()
    for c in s:
        d[c] = d.get(c, 0) + 1
    return d

h = histogram('brontosaurus')
print h
