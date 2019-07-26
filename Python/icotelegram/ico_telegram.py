import requests, time, csv
from bs4 import BeautifulSoup

BASE_URL = "https://bitcointalk.org/index.php?board=238."
pages = 289
tg_links = []

with open("bitcointalkICO.csv", mode="w") as ico_file:
    ico_writer = csv.writer(ico_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    ico_writer.writerow(['ICO Name', 'Telegram Link'])
    for page in range(0, pages*40, 40):
        try:
            url = BASE_URL + str(page)
            r = requests.get(url)
            list_soup = BeautifulSoup(r.text, features="html.parser")
            rows = list_soup.find_all("td", {"class": "windowbg"})
            links = []
            for row in rows:
                if str(type(row.find("a"))) != "<class 'NoneType'>": 
                    row = row.find("a")
                    links.append(row.get("href"))
            for link in links:
                time.sleep(5)
                #print("### -", link)
                r2 = requests.get(link)
                link_soup = BeautifulSoup(r2.text, features="html.parser")
                firstPostRow = link_soup.find_all("td", {"class": "td_headerandpost"})
                try:
                    telegram_link = firstPostRow[0].find_all("a")
                    for tg in telegram_link:
                        if str(type(tg.get('href'))) != "<class 'NoneType'>":
                            try:
                                if tg.get('href').startswith("https://t.me") or tg.get('href').startswith("http://t.me") or tg.get("href").startswith("https://telegram.me") or tg.get("href").startswith("http://telegram.me"):
                                    telegram_link = tg.get("href")
                                    if telegram_link.split("/")[-2] != "joinchat":
                                        if telegram_link not in tg_links:
                                            tg_links.append(telegram_link)
                                            #print(link_soup.title.text)
                                            name = telegram_link.split("/")[-1]
                                            #print(name + " - " + telegram_link)
                                            ico_writer.writerow([name, telegram_link])
                            except:
                                print('excepted')
                                pass
                except:
                    pass
            print(len(page, tg_links))
        except requests.exceptions.RequestException as e:
            input("Disconnecter, Click any button to proceed")
            pass