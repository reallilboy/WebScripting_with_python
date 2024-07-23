import requests
import bs4
import urllib


def founder(name):
    try: 
        name = name.quote_plus(name)
        URL = 'your another url for search'
        filename = requests.get
        found = requests.get(URL+'search url'+name)
        soup = bs4.BeautifulSoup(filename.content)
        founfile = soup.findAll('Determine what you want for exmaple <a>')
        return name ,filename
    except BaseException:
        print('ERROR!!')


page = requests.get('YOUR URL')
soup = bs4.BeautifulSoup(page.content)
names = soup.findAll('Determine what you want for exmaple <a>')

for name in names:
    if name.string == None:
        continue
    else:
        print(founder(str((name.string))))
