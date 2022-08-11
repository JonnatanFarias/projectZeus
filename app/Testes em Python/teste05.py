from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import pandas as pd
import time
import urllib

contatos = pd.read_excel(r"F:\projectZeus\app\Usuarios.xlsx")
print(contatos)


navegador = webdriver.Chrome()
navegador.get("https://web.whatsapp.com/")


while len(navegador.find_elements_by_id("side")) < 1:
    time.sleep(1)


for i, mensagem in enumerate(contatos['Mensagem']):
    pessoa = contatos.loc[i, "Pessoa"]
    numero = contatos.loc[i, "Número"]
    texto = urllib.parse.quote(f"Oi {pessoa}! {mensagem}")
    link = f"https://web.whatsapp.com/send?phone={numero}&text={texto}"
    navegador.get(link)
    while len(navegador.find_elements_by_id("side")) < 1:
        time.sleep(1)
    navegador.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div/div/div[2]/div[1]/div/div[2]').send_keys(Keys.ENTER)
    time.sleep(10)   