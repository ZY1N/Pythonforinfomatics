fname = raw_input('Enter file name: ')
try:
	fhandle = open(fname)
except:
	print 'File cannot be opened:', fname
	exit()
emails = dict()
for line in fhandle:
	if line.startswith('From '):
		line = line.split()
		email = line[1]
		email = email.split('@')
		domain = email[1]
		emails[domain] = emails.get(domain,0) + 1
print emails
