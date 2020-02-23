from bs4 import BeautifulSoup
import requests
import time
urls = ["https://el.wikipedia.org/wiki/Διεθνές_Πανεπιστήμιο_της_Ελλάδος"]
h1s = []

def manage_links(links):
    for link in links:
        try:
            url = f"https://el.wikipedia.org/{link['href']}" 
            urls.append(url)
            open("./links.txt","a", encoding='utf-8').write(url +'\n')
        except:
            print("Exception !")
            pass         

def manage_urls(urls):
    while True:    
        for i in urls:
            try:
                page = requests.get(i)
                soup = BeautifulSoup(page.content, 'html.parser')
                time.sleep(0.2)
                h1 = soup.find(id="firstHeading").text
                l = soup.find_all('a')
                manage_links(l)
                h1s.append(h1)
                print(h1)
                open("./names.txt","a",encoding='utf-8').write(h1 +'\n')
            except:
                pass
    
manage_urls(urls)