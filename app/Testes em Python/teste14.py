import pyautogui
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys


#Entra pesquisa a página
navegador = webdriver.Chrome()
navegador.get('http://painel.nuvvel.com.br/cliente/login')
#Fazer login
time.sleep(0.5)
navegador.find_element_by_xpath('/html/body/div[2]/form[1]/div[1]/input').send_keys("jonnatan@atacadaofarias.com.br")
time.sleep(0.5)
navegador.find_element_by_xpath('/html/body/div[2]/form[1]/div[2]/input').send_keys("farias2021@@!!")
time.sleep(1)
#Abre o cadastramento de endereço
navegador.find_element_by_xpath('/html/body/div[2]/form[1]/div[3]/button').click()
time.sleep(1.5)
navegador.find_element_by_xpath('/html/body/div/div[3]/div[1]/div/ul/li[3]/a/i').click()
time.sleep(1.5)
navegador.find_element_by_xpath('/html/body/div/div[3]/div[1]/div/ul/li[3]/ul/li[4]/a/span').click()
time.sleep(1.5)
navegador.find_element_by_xpath('/html/body/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[2]/a[1]').click()
time.sleep(1.5)
#Laço de repetição >>> conforme quantidade informada no range
for i in range(50):
 navegador.find_element_by_xpath('//*[@id="pac-input"]').click()
 time.sleep(1)
 pyautogui.click(x=3508,y=271)
 pyautogui.hotkey('ctrl','c')
 time.sleep(0.5)
 pyautogui.click(x=181,y=345)
 pyautogui.hotkey('ctrl','v')
 pyautogui.press('return')
 time.sleep(0.5)
 pyautogui.click(x=3294 ,y=35)
 time.sleep(0.5)
 pyautogui.press(['left'])
 time.sleep(0.5)
 pyautogui.hotkey('ctrl','c')
 time.sleep(0.5)
 navegador.find_element_by_xpath('//*[@id="tab_cerca"]/div[1]/input').click()
 time.sleep(0.5)
 pyautogui.click(x= 1483, y = 432)
 pyautogui.hotkey('ctrl','v')
 pyautogui.click(x=3294 ,y=35)
 time.sleep(0.5)
 pyautogui.press(['right'])
 time.sleep(0.5)
 pyautogui.press(['down'])
 time.sleep(0.5)
 navegador.find_element_by_xpath('//*[@id="tab_cerca"]/div[3]/span/span[6]').click()
 time.sleep(0.5)
 pyautogui.click(x = 1298 , y =599)
 time.sleep(0.5)
 navegador.find_element_by_xpath('//*[@id="portlet-cerca"]/div[2]/div/div[1]/div/ul/li[2]/a').click()
 time.sleep(0.5)
 navegador.find_element_by_xpath('//*[@id="tab_veiculos"]/div[1]/div[2]/div/div/span[3]').click()
 time.sleep(0.5)
 navegador.find_element_by_xpath('//*[@id="tab_veiculos"]/div[2]/div/div/div/span[3]').click()
 time.sleep(0.5)
 navegador.find_element_by_xpath('//*[@id="local-salvar"]').click()
 time.sleep(2)
 pyautogui.click(x= 918 , y = 642)
 time.sleep(1)
 pyautogui.click(x= 918 , y = 642)
 time.sleep(0.5)
 navegador.find_element_by_xpath('/html/body/div/div[3]/div[1]/div/ul/li[3]/a/i').click()
 time.sleep(1.5)
 navegador.find_element_by_xpath('/html/body/div/div[3]/div[1]/div/ul/li[3]/ul/li[4]/a/span').click()
 time.sleep(1.5)
 navegador.find_element_by_xpath('/html/body/div/div[3]/div[2]/div/div[2]/div/div/div[1]/div[2]/a[1]').click()
 time.sleep(1.5)



  
























