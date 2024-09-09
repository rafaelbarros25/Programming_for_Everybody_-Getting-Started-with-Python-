import urllib.request, urllib.parse, urllib.error
import json

url = input("Enter - ")
uh = urllib.request.urlopen(url).read().decode('utf-8')
print('Retrieving', url)
print('Retrived', len(url), 'characters')

js = json.loads(uh)
print(js)
count =0
sum=0
for item in js['comments']:
    x = int(item['count'])
    sum = sum+x

print ("Sum : ",sum)