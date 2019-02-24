import requests
from bs4 import BeautifulSoup
from random import randint

base_url = 'https://quotes.yourdictionary.com/theme/marriage/'

page = requests.get(base_url)

soup = BeautifulSoup(page.text, 'lxml')

pregovori_firstPage = []
pregovori_otherPages = []
pregovori_skupno = []

for x in range(2, 5):
    nov_url = base_url + str(x) + "/"
    
    stran = requests.get(nov_url)
    stran_soup = BeautifulSoup(stran.text,'lxml')

    quotes_1 = soup.find_all(class_='quoteContent')

    for quote in quotes_1:
        pregovori_firstPage.append(quote.text)

    quotes = stran_soup.find_all(class_='quoteContent')

    for quote in quotes:
        pregovori_otherPages.append(quote.text)

    pregovori_skupno = pregovori_firstPage + pregovori_otherPages

# print(len(pregovori_skupno)) # Da zvem kok je vseh elementov v listi---> za naključno število


# 5 naključnih števil
x = [randint(0, 170) for p in range(0, 5)]

# Zapis v txt datoteko: 
with open("Output.txt", "w") as text_file:
    for number in x:
        print(pregovori_skupno[number], file=text_file)

