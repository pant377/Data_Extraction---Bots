import requests
from bs4 import BeautifulSoup
import smtplib
import time
URL = 'https://coinmarketcap.com/currencies/litecoin/'
URL2 = 'https://coinmarketcap.com/currencies/bitcoin/'
headers = {"User-Agent": 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:69.0) Gecko/20100101 Firefox/69.0'}


def check_price():

    page = requests.get(URL, headers=headers)
    page2 = requests.get(URL2, headers=headers)
    soup1 = BeautifulSoup(page.content, 'html.parser')
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")
    soup3 = BeautifulSoup(page2.content, 'html.parser')
    soup4 = BeautifulSoup(soup3.prettify(), 'html.parser')
    price = soup2.find(id="quote_price").text
    price2 = soup4.find(id="quote_price").text

    pricef1 = float(price[:18])*0.903763
    pricef2 = float(price2[:19])*0.903763

    print("Litecoin : ", pricef1, " Euro")
    print("\nBitcoin : ", pricef2, " Euro")

    if(pricef1 > 75 and pricef2 > 10000):
        send_mail()
    elif(pricef1 > 76):
        send_mail()
    elif(pricef2 > 10000):
        send_mail()


def send_mail():

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login('pantpap15@gmail.com', '')
    server.sendmail(from_addr='pantpap15@gmail.com', to_addrs='thisispant@protonmail.com', msg="Anevikan Ta coins des : https://coinmarketcap.com/currencies")
    print("\nMail Sended !!")
    server.quit()


while(True):
    check_price()
    time.sleep(60*10)
