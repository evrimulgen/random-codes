# hakan icin telegram isi 2
import csv

from bs4 import BeautifulSoup
import requests
import time

BASE_URL = 'https://coinmarketcap.com' # +'coin sayfasi'
BASE_URL2 = 'https://telegramcryptogroups.com/' # 83 sayfa # https://telegramcryptogroups.com/telegram_groups/332
URL = 'https://coinmarketcap.com/all/views/all/'
pages = 83

with open("ico.csv", mode="w") as ico_file:
  ico_writer = csv.writer(ico_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  ico_writer.writerow(['ICO Name', 'Telegram Link'])
  r = requests.get(URL)
  list_soup = BeautifulSoup(r.text, "lxml")
  rows = list_soup.find_all("a", {"class": ["currency-name-container", "link-secondary"]})
  links = []
  coin_links = []
  for row in rows:
    time.sleep(5)
    row = row.get('href')
    if row in links:
      pass
    else:
      links.append(row)
    get_coin = requests.get(BASE_URL + row)
    coin = BeautifulSoup(get_coin.text, 'lxml')
    a_search = coin.find_all("a")
    name = row.split('/')[-2]
    FOUND = False

    for a in a_search:
      if a.get('href') != None:
        if a.get('href').startswith("https://t.me") or a.get('href').startswith("http://t.me"):
          if a.get('href') != "https://t.me/CoinMarketCap":
            if name in coin_links:
              pass
            else:
              FOUND = True
              coin_links.append(name)
              print(name + " - " + a.get('href'))
              ico_writer.writerow([name, a.get('href')])

    if name not in coin_links:
      coin_links.append(name)
      if FOUND == False:
        print(name, "NOT FOUND")
        try:
          ico_writer.writerow([name, 'NOT FOUND'])
        except:
          pass