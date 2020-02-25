from bs4 import BeautifulSoup
import requests
urls = [" https://en.wikipedia.org/wiki/Mia_Khalifa"]
h1s = []
bigurl = []

def manage_links(links):
    for link in links:
        try:
            url = f"https://en.wikipedia.org{link['href']}" 
            if (len(urls) <= 200) and (url[:-3] not in bigurl):
                open("./links.txt","a", encoding='utf-8').write(url +'\n')
                urls.append(url)  
                bigurl.append(url[:-3])     
            else:
                pass     
        except:
            print("Not Valid Link..")
            pass         

def manage_urls(urls):
    for url in urls:
        try:
            page = requests.get(url)
            soup = BeautifulSoup(page.content, 'html.parser')
            h1 = soup.find(("h1", {"id":"firstHeading"})).text
            a = soup.find_all('a')
            manage_links(a)
            h1s.append(h1)
            print(h1)
            open("./names.txt","a",encoding='utf-8').write(h1 +'\n')
        except:
            pass
    
manage_urls(urls)