from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'http://services.runescape.com/m=itemdb_rs/top100'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

#grabs the content
content = page_soup.tbody.findAll("tr")
#grabs the first item
item = content[0]

filename = "top100.csv"
f = open(filename, "w")

headers = "name,total\n"

f.write(headers)
for item in content:
    name = item.td.a.img["title"]
    info = item.findAll("td")
    minvol = info[2].text
    medvol = info[3].text
    maxvol = info[4].text
    total = info[5].text
    print("name: " + name)
    print("total: " + total)

    f.write(name + "," + total + "\n")

f.close()

#grabs title of item
# name = item.td.a.img["title"]
# #grabs volumes
# info = item.findAll("td")
# minvol = info[2].text
# medvol = info[3].text
# maxvol = info[4].text
# total = info[5].text
