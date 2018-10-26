import requests, re
from bs4 import BeautifulSoup

soup = BeautifulSoup(requests.get("https://coinmarketcap.com/exchanges/cryptopia/").text, "lxml")
mydivs = soup.findAll("a", {"target": "_blank"})

# a= []

# for i in mydivs:
#          if str(i).endswith("/BTC</a>"):
#                 for i in re.findall("[A-Z]{2,}", str(i)[-13:-8]):
#                 	a.append(i)
#                 	print(len(a))


text = open("coins.txt", "a")

liste = []

for i in mydivs:
    for j in re.findall("[A-Z0-9]{2,6}", str(i)):
            if str(j) != "BTC" and str(j) not in liste and len(str(j)) <= 5:
                    liste.append(str(j))
                    text.write(str(j) + "\n")
                    print(len(liste))

text.close()