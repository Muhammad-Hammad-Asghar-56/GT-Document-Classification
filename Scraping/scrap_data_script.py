import requests as req
import threading
from bs4 import BeautifulSoup



fileName = "marcuslemonis.txt"
threads=[]
global links
links=[]

def scrap_data(url):
    data = req.get(url)
    content = data.content

    soup = BeautifulSoup(content, 'html.parser')  # Specify the parser

    with open(fileName,'a', encoding='utf-8') as file:
        data=soup.text.replace('\n',' ')
        file.write(data)
    urls = soup.find_all('a')  # Find all <a> tags
    link=[]

    for x in urls:
        clean_url = x.get('href')
        if "//" in clean_url:
            link.append(clean_url)

    for x in link:
        if(x not in link):
            th = threading.Thread(target=scrap_data, args=(x,))
            threads.append(th)
            th.start()
        


url = 'https://marcuslemonis.com/business/starting-a-business'
scrap_data(url)
for x in threads:
    x.join()