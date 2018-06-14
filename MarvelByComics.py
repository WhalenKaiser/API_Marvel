#!/usr/bin/evn python
#The attributionText is printed because I read the Marvel Developer rules and they require attribution.
#The data is returned into a new dictionary for caching and then sorted using a lambda function,
#for simplicity, and to limit run time.
#This API request returns the name and number of available comics for the first 100 characters.  It then
#sorts the characters by most comics.

import urllib.request
import urllib.parse
import json

PROXY_URL = "http://wwwcache--{}.lancs.ac.uk:8080"

url = 'http://gateway.marvel.com/v1/public/characters?ts=1&apikey=<api_key>&limit=100'
json_obj = urllib.request.urlopen(url)

data = json.load(json_obj)
new_dict = {}

print (data['attributionText'])

for people in data['data']['results']:
    char = (people ['name'])
    comic_count = (people ['comics']['available'])
    new_dict[char] = comic_count

#print (new_dict)

def sortByValue():
    sortedByVal = sorted(new_dict.items(), key = lambda t: t[1], reverse = True)
    print (sortedByVal[:10])

sortByValue()
