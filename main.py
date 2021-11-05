import requests
import pandas
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time


#mandar por email as infos
import smtplib
import email.message

#1.Pega o HTML e navegar na pagina até o primeiro jogo
url = "https://www.oddsportal.com/soccer/brazil/serie-a/flamengo-rj-atletico-go-bFKRrzEi/"
driver = webdriver.Firefox()
driver.get(url)
driver.find_element(By.XPATH,'//*[@id="odds-data-table"]/div[1]/table/thead/tr/th[2]/a').click()
driver.find_element(By.XPATH,'//*[@id="odds-data-table"]/div[1]/table/thead/tr/th[2]/a').click()
menorODD=driver.find_element(By.XPATH,'//*[@id="odds-data-table"]')
html=menorODD.get_attribute('outerHTML')

print(html)

#element=driver.find_element(By.XPATH,'//*[@id="odds-data-table"]/div[1]/table/thead/tr/th[2]/a').click()


#2.Pega o nome das equipes e armazena a menor odd e compara com a maior od de todas as categorias(informar times e horario da partida)
soup=BeautifulSoup(html,'html.parser')
table=soup.find(id="odds-data-table")

df_full=pandas.read_html(str(table))[0].head(14)
df=df_full[['1','x','2']]
df.columns=['Flamengo','x','Atl Go']
#3.Printar essas informações
#4.Retornar a pagina principal e executar o mesmo passo até o final da pagina

driver.quit()
