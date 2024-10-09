import bs4
import requests

windex = 0

info = requests.get('https://finance.yahoo.com/topic/stock-market-news')
# print(info.text)

soup = bs4.BeautifulSoup(info.text, 'html.parser')
print(soup.title)

headlines = soup.find_all('p')
# print(headlines[3])

for i in headlines:
    if "Most Read from Bloomberg" in str(i):
        splitted = str(i).split("Most Read from Bloomberg")
        # print("Splitted: \n", splitted[0])
        if "--" in splitted[0]:
            splittedier = splitted[0].split(" -- ")
            print("Headline: \n", splittedier[-1])
        # print(splitted[0])
        else:
            continue
    else:
        continue

prg = soup.select('p')
# print(prg)