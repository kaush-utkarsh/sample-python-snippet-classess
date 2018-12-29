from bs4 import BeautifulSoup
with open("test.html","r") as htmlfile: 
	html_doc = htmlfile.read()
# print(html_doc)
soup = BeautifulSoup(html_doc, 'html.parser')
# print(soup.title)
print(soup.title.text.strip())
# print(soup.a)
# for link in soup.find_all('a'):
#     print(link.get('href'))
for para in soup.find_all('p'):
    print(para.text)
# print(soup.find(id="colophon"))
print(soup.find(id="colophon").text)