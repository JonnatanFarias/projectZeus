import requests
from bs4 import BeautifulSoup

#INFORMAÇÕES SOBRE A COVID-19 NO BRASIL

paginaweb =requests.get("https://www.worldometers.info/coronavirus/country/brazil/")
soup =BeautifulSoup(paginaweb.text, 'html.parser')

lista = soup.findAll("div", {"class":"maincounter-number"})

casos = lista[0].text.strip()
mortes=lista[1].text.strip()
recuperados=lista[2].text.strip()

print()
brasil = ('Monitor da COVID-19 no Brasil\n'+
           '*'*30+"\n"+
           'Número de casos = ' + casos +"\n"+
           'Número de mortes = '+ mortes+"\n"+
           'Número de recuperados = '+ recuperados+"\n"+
           '*'*30+"\n"+
           'As informações mostradas são do inicio da pandemia.')
print(brasil)
print()

#INFORMAÇÕES SOBRE A COVID-19 NO MUNDO

paginaweb =requests.get("https://www.worldometers.info/coronavirus/")
soup =BeautifulSoup(paginaweb.text, 'html.parser')

lista = soup.findAll("div", {"class":"maincounter-number"})

casos = lista[0].text.strip()
mortes=lista[1].text.strip()
recuperados=lista[2].text.strip()

print()
mundo = ('Monitor da COVID-19 no Mundo\n'+
           '*'*30+"\n"+
           'Número de casos = ' + casos +"\n"+
           'Número de mortes = '+ mortes+"\n"+
           'Número de recuperados = '+ recuperados+"\n"+
           '*'*30+"\n"+
           'As informações mostradas são do inicio da pandemia.')
print(mundo)
print()