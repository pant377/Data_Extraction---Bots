from bs4 import BeautifulSoup
import requests

html_page = requests.get("https://el.wikipedia.org/wiki/Διεθνές_Πανεπιστήμιο_της_Ελλάδος")
soup = BeautifulSoup(html_page.content, 'html.parser')
links = soup.find_all('a')
for link in links:
    try:
        print(link['href'])
        url = f"https://wikipedia.org/{link['href']}"
        page2 = reguests.get(url)
        print(page2)
    except:
        pass

