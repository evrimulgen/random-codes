# hakan icin telegram isi 2
import csv

from bs4 import BeautifulSoup
import requests
import time

BASE_URL = 'https://telegramcryptogroups.com' # 83 sayfa # https://telegramcryptogroups.com/telegram_groups/332
pages = 83
#mb-1 mt-1 mr-1 btn btn-info



with open("telecrypto.csv", mode="w") as ico_file:
  ico_writer = csv.writer(ico_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
  ico_writer.writerow(['ICO Name', 'Telegram Link'])

  for page in range(1, pages):
    url = BASE_URL + "/?page=" + str(page)
    r = requests.get(url)
    list_soup = BeautifulSoup(r.text, "lxml")
    rows = list_soup.find_all("a", {"class": ["mb-1", "mt-1", "mr-1", "btn", "btn-info"]})
    links = []
    coin_links = []

    for row in rows:
      time.sleep(5)
      row = row.get('href')
      if row != None:
        if row.startswith('/telegram'):
          if row in links:
            pass
          else:
            links.append(row)
          r2 = requests.get(BASE_URL + row)
          coin = BeautifulSoup(r2.text, 'lxml')
          telegram_link = coin.find_all("a", {"class": ["mb-1", "mt-1", "mr-1", "btn", "btn-info"]})
          name = coin.find_all('h3')[0].text
          FOUND = False

          for a in telegram_link:
            if a.get('href') != None:
              if a.get('href').startswith("https://t.me") or a.get('href').startswith("http://t.me"):
                coin_name = a.find_all("h3")#, {"class": ["name", "font-weight-semibold"]})
                # if a.get('href') != "https://t.me/CoinMarketCap":
                if name in coin_links:
                  pass
                else:
                  FOUND = True
                  coin_links.append(name)
                  print(name + " - " + a.get('href'))
                  try:
                    ico_writer.writerow([name, a.get('href')])
                  except:
                    ico_writer.writerow([a.get('href').split('/')[-1], a.get('href')])

          if name not in coin_links:
            coin_links.append(name)
            if FOUND == False:
              print(name, "NOT FOUND")
              try:
                ico_writer.writerow([name, 'NOT FOUND'])
              except:
                pass