from config import IG_CLIENT_ID, IG_CLIENT_SECRET
import json,urllib2

tag = 'nofilter'
url = 'https://api.instagram.com/v1/tags/%s/media/recent?client_id=%s' % (tag, IG_CLIENT_ID)
response = urllib2.urlopen(url)
html = response.read()
json_response = json.loads(html)

for item in json_response['data']:
    print item['type'],  item['images']['standard_resolution']['url']

