import requests
from bs4 import BeautifulSoup
import re
from csv import writer

base_url = 'https://en.wikipedia.org/wiki/Game_of_Thrones'

ogledi = 0
for x in range(1, 8):
    seasons_url = base_url + "_(season_" + str(x) + ")"
    
    url = requests.get(seasons_url)

    soup = BeautifulSoup(url.text, 'lxml')

    tabela = soup.find(attrs={'class': 'wikitable plainrowheaders wikiepisodetable'})
    tabela_1 = tabela.select('.vevent')

    # with open('got.csv', 'w') as csv_file:
    #     csv_writer = writer(csv_file)
    #     headers = ['Season', 'Viewers']
    #     csv_writer.writerow(headers)

    for epizoda in tabela_1:
        n = epizoda.findAll('td')[-1]
        m = re.search(r'\d{1,2}.\d{2}', n.text)

        m_novo = float(m.group())
#             # print(m_novo)
        ogledi += m_novo

print(ogledi)
        
        