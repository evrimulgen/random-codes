'''import requests

my_url = "http://siirleri.org/en_iyiler.html"

response = requests.get(my_url, steam=True)
#print(dir(response.request))
#print(requests.post(my_url).text) #alayini printliyor
r = requests.post(my_url)

#for i in range(3):
#print("".join(r.text.split("<li>")[1:10]).split("title"))
print(response.raw)

# payload = {'key1': 'value1', 'key2': 'value2'}
# r = requests.get('http://httpbin.org/get', params=payload)
# print(r.url)'''

# import libraries
import urllib.request as urllib
from bs4 import BeautifulSoup

url = "http://docs.python-requests.org/en/master/user/quickstart/#make-a-request"

page = urllib.urlopen(url)
soup = BeautifulSoup(page, 'html.parser')
name_box = soup.find('li')			#, attrs={'class':'styled'})
name = name_box.text.strip()		# strip() is used to remove starting and trailing
#print(soup.find_all('a')[0:10])
for i in soup.find_all('a'):			#, attrs={'class':'headerlink'}):		# A'larin icindeki tum titlelari buluyor
	try:
		print(i["title"])
	except:
		pass
#print(soup.find("title")) 			#butun tittle'lari buluyor