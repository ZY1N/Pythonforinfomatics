#Exercise 12.2 Change your socket program so that it counts the number of characters it has received and stops displaying any text after it has shown 3000 characters. The program should retrieve the entire document and count the total number
#of characters and display the count of the number of characters at the end of the
#document.



import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

website = raw_input("Enter URL: ")

url = website.split('/')

try:
    main = url[2]
    mysock.connect((main, 80))
    mysock.send('GET website HTTP/1.0\n\n')
except:
    print "Error bad address"
    exit()

total = 0
string = str()
while total < 3000:
    data = mysock.recv(1)
    string = string + data
    if (len(data) < 1):
        break
    total = total + len(data)

print string
    
print total
mysock.close()
