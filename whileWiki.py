from bs4 import BeautifulSoup
import requests
import time
link = open("./links.txt","a",encoding='utf-8') 
name = open("./names.txt","a",encoding='utf-8') 

while True:
    try:
        url = f"https://el.wikipedia.org{link.readline}" 
        print(url)
        html_page = requests.get(url)
        time.sleep(0.2)
        soup = BeautifulSoup(html_page.content, 'html.parser')
        h1 = soup.find(id="firstHeading").text
        l = soup.find_all('a')
        name.write(h1 +'\n')
        link.write(l +'\n')
        #delete_file_cont("./links.txt")
        print(h1)      
    except:
        pass
        
def delete_file_cont(path):
    with open(path ,'w'):
        pass
