from bs4 import BeautifulSoup
import requests
import time
urls = []
h1s = []
urlM = "https://el.wikipedia.org/wiki/Διεθνές_Πανεπιστήμιο_της_Ελλάδος"
html_page = requests.get(urlM)
soup = BeautifulSoup(html_page.content, 'html.parser')
links = soup.find_all('a')

def manage_links(links):
    urls = []
    for link in links:
        try:
            url = f"https://el.wikipedia.org/{link['href']}" 
            urls.append(url)
            open("./links.txt","a", encoding='utf-8').write(url +'\n')
        except:
            pass       
    manage_urls(urls)          

def manage_urls(urls):
    links2 = []
    for i in urls:
        try:
            page = requests.get(i)
            soup = BeautifulSoup(page.content, 'html.parser')
            time.sleep(0.2)
            h1 = soup.find(id="firstHeading").text
            l = soup.find_all('a')
            links2.append(l)
            h1s.append(h1)
            print(h1)
            open("./names.txt","a",encoding='utf-8').write(h1 +'\n')
        except:
            pass
    manage_links(links2)

manage_links(links)