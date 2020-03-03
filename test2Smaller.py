from bs4 import BeautifulSoup
import requests
urls = ["https://en.wikipedia.org/wiki/Mia_Khalifa"]     
bigurl = []       
while len(urls) < 200:    
    page = requests.get(urls.pop(0))
    soup = BeautifulSoup(page.content, 'html.parser')
    a = soup.find_all('a')
    for link in a:                                                    
        try:
            if('http'not in link['href'])and('www'not in link['href'])and('wikimedia'not in link['href']and("//"not in link['href'])): 
                url = f"https://en.wikipedia.org{link['href']}"                                                                        
                if (len(urls) <= 200)and(url[:-3]not in bigurl)and("#"not in url)and("index.php?"not in url):                           
                    open("./links.txt","a", encoding='utf-8').write(url +'\n')                                    
                    urls.append(url)                                                                                 
                    bigurl.append(url[:-3])     
                else:
                    pass     
        except:
            pass   
