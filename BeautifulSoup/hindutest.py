import requests, random
from bs4 import BeautifulSoup
# fetch feeds
result = requests.get("https://www.thehindu.com/news/international/feeder/default.rss")
result.encoding = result.apparent_encoding
feed = result.text
# parse xml rss feed
feedsoup = BeautifulSoup(feed,"xml")
articles = []
for item in feedsoup.find_all('item'):
	articles.append(item.find('link').text)
# fetch random article link
link = articles[random.randint(0,len(articles))]
#Fetch Article Page
result = requests.get(link)
result.encoding = result.apparent_encoding
artbod = result.text
# parse html page
soup = BeautifulSoup(artbod, 'html.parser')
print(soup.title.text.strip())
art = soup.find("div",{'class':'articlepage'})
for p in art.find_all("p"):
	print(p.text.strip())