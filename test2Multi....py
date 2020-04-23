from bs4 import BeautifulSoup
import requests
import multiprocessing as mp
import time

def manage_urls(urls,bigurl):
    while (len(urls)<5000):    
        soup = BeautifulSoup(requests.get(urls.pop(0)).content, 'html.parser')
        for link in soup.find_all('a'):      
            try:                                              
                if('/wiki/' in link['href'])and('www'not in link['href'])and('wikimedia'not in link['href']and("//"not in link['href'])):             
                    url = f"https://en.wikipedia.org{link['href']}"                                 
                    if (len(urls) < 5000)and(url[:-3]not in bigurl)and(url not in urls)and("#"not in url)and("?"not in url)and("File:"not in url):                                                            
                        urls.append(url)       
                        open("./links.txt","a").write(url +'\n')                                                                       
                        bigurl.append(url[:-3])
                    else:
                        pass       
            except:
                pass                    

if __name__ == '__main__': 
    manager = mp.Manager()
    urls,bigurl = manager.list(),manager.list()
    urls.append("https://en.wikipedia.org/wiki/Mia_Khalifa")
    worker1 = mp.Process(target=manage_urls,args=(urls,bigurl))
    worker2 = mp.Process(target=manage_urls,args=(urls,bigurl))
    worker3 = mp.Process(target=manage_urls,args=(urls,bigurl))
    worker4 = mp.Process(target=manage_urls,args=(urls,bigurl))
    worker1.start()
    time.sleep(0.85)
    worker2.start()
    worker3.start()
    worker4.start()
    worker1.join()
    worker2.join()
    worker3.join()
    worker4.join()
   