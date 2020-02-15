from bs4 import BeautifulSoup
import requests
import re
html_page = requests.get("https://el.wikipedia.org/wiki/Διεθνές_Πανεπιστήμιο_της_Ελλάδος")
soup = BeautifulSoup(html_page.content, 'html.parser')

for link in soup.findAll('a'):
    pages = link.get('href')
    for j in pages:
        page2 = reguests.get(j)
        print(page2)




