from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup
notification="https://ktu.edu.in/eu/core/announcements.htm"
uclient=uReq(notification)
content_html=uclient.read()
uclient.close()
#html parsing3
page_soup=soup(content_html,"html.parser")
item_class=page_soup.find_all("div",{"class":"c-details"})
#grab each

for container in item_class:
    a=container.findAll("td",{"class":"align-center"})
    b=container.findAll("td")
    c=container.findAll("a")

    for j in range(0,len(b)):
        content = b[j].text.strip()
        if(content==b[j-1].text.strip()):
            print ("")
        else:
            print(content)
    for k in range(0, len(c)):
        link = c[k].get('href')
        if(link[0:3]=="/eu"):
            print("https://ktu.edu.in"+link)
        else:
             print(link)


