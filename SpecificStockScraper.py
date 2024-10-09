import bs4
import requests

url='https://finance.yahoo.com/quote/AAPL/'

soup = bs4.BeautifulSoup(requests.get(url).text)

# print(soup)

anchor = soup.find_all('a', attrs={'class':'subtle-link fin-size-small thumb yf-1e4diqp'})

for atrb in anchor:
    print('Title: ', atrb['title'])
    print('URL: ', atrb['href'])
    print('-------------------')


# print(anchor)