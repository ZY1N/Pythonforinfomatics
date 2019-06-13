#Exercise 13.1 Change the program that retrieves twitter data (twitter2.py) to
#also print out the location for each of the friends indented under the name by two
#spaces as follows:

import urllib
import twurl
import json

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

while True:
    print ''
    acct = raw_input('Enter Twitter Account:')
    if ( len(acct) < 1 ) : break
    url = twurl.augment(TWITTER_URL,
        {'screen_name': acct, 'count': '5'} )
    print 'Retrieving', url
    connection = urllib.urlopen(url)
    data = connection.read()
    headers = connection.info().dict
    print 'Remaining', headers['x-rate-limit-remaining']
    js = json.loads(data)
    print json.dumps(js, indent=4)

    
        
    for u in js['users'] :
        print u['screen_name']
        print u['location']
        s = u['status']['text']
        print '  ',s[:50]
