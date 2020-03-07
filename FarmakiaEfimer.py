from bs4 import BeautifulSoup as Bs
import requests as ureq
n = 1
url = 'https://www.vrisko.gr/efimeries-farmakeion/thessaloniki/'
page = ureq.get(url)
details = Bs(page.content,'html.parser' )
therialdve = details.find_all(class_="DutiesResult")
for trx in therialdve:
    dive = trx.find_all(class_="ResultLeft")
    times = trx.find_all(class_="ResultRight")
    for j in times:
        try:
            firsttime = j.find(class_="DutyTimes").text
            duty = j.find(class_="DutyActive").text
        except:
            None 
    for i in dive:
        details2 = i.find(style="padding-bottom:6px;").get_text()
        details3 = i.find(class_="ResultAddr").next.next.next
        details4 = i.find(class_="spPhone").get_text()

    print(":",details2,"\n    ",details3,"\n      ",details4,firsttime,"\n\n")
        