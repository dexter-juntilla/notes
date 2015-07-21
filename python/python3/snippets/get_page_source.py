import urllib.parse
import requests


headers = {}

headers['User-Agent'] = r"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36"

url = 'http://whatsmyuseragent.com/'

response = requests.get(url, headers = headers)
the_page = response.text

with open('ua.html', 'w') as file:
	file.write(the_page)



#POST request
import urllib.parse
import urllib.request
headers = {}

headers['User-Agent'] = r"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.132 Safari/537.36"

url = 'http://127.0.0.1/urllib.php'

values = {'name' : 'Michael Foord',
          'location' : 'Northampton',
          'language' : 'Python' }

data = urllib.parse.urlencode(values).encode('utf-8')
request = urllib.request.Request( url, data, headers=headers )
response = urllib.request.urlopen(request)
the_page = response.read()
print(the_page)
