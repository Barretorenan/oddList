import requests
import pandas
import lxml
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import time
#mandar por email as infos
import smtplib
import email.message
from datetime import datetime

##Pegar a hora atual para analisar a coluna de horas e procurar se ainda vai ocorrer, colocar um contador de erros no if caso ocorra 5 else consecutivos, para o programa, no true colocar um zerador
contador=2
#pega a data e transforma em formula para o link
data=datetime.today().strftime('%Y-%m-%d')
data = data.replace('-', '')
#pagina do dia
home=("https://www.oddsportal.com/matches/soccer/{}/".format(data))


#1.Pega o HTML e navegar na pagina até o primeiro jogo
url = "https://www.oddsportal.com/soccer/brazil/serie-a/flamengo-rj-atletico-go-bFKRrzEi/"

#####esconder a aba
driver = webdriver.Firefox()
driver.get(home)
def entra_Partida(contador):
    xpath_jogos = ('//*[@id="table-matches"]/table/tbody/tr[{}]/td[2]/a'.format(contador))
    if analisa_Xpath(xpath_jogos)==True:
        driver.find_element(By.XPATH, ('{}').format(xpath_jogos)).click()
        pegaOdds()
        contador=contador+1
        driver.get(home)
        entra_Partida(contador)
    else:
        contador=contador+1
        entra_Partida(contador)



def analisa_Xpath(link):
    xpath=True
    try:
        driver.find_element(By.XPATH,link)
        return True
    except:

        return False


#2.Pega o nome das equipes e armazena a menor odd e compara com a maior od de todas as categorias(informar times e horario da partida)
def pegaOdds():
# trabalhando a string
    #ordena ODDS da casa, menor para maior
    driver.find_element(By.XPATH,'//*[@id="odds-data-table"]/div[1]/table/thead/tr/th[2]/a').click()
#pega maior odd time 1
    driver.find_element(By.XPATH,'//*[@id="odds-data-table"]/div[1]/table/thead/tr/th[2]/a').click()
#pega menor odd time 1
    driver.find_element(By.XPATH,'//*[@id="odds-data-table"]/div[1]/table/thead/tr/th[2]/a').click()
#pega maior empate
    driver.find_element(By.XPATH,'//*[@id="odds-data-table"]/div[1]/table/thead/tr/th[2]/a').click()
#pega menor odd empata
    driver.find_element(By.XPATH,'//*[@id="odds-data-table"]/div[1]/table/thead/tr/th[2]/a').click()
#pega maior odd time 2
    driver.find_element(By.XPATH,'//*[@id="odds-data-table"]/div[1]/table/thead/tr/th[2]/a').click()
#pega menor odd time 2

#Pega nomes dos times da casa e visitante
    times = driver.find_element(By.XPATH, '//*[@id="col-content"]/h1')
    strTimes = times.get_attribute('outerHTML')
    strTimes_text = strTimes.replace('<h1>', '')
    strTimes_text = strTimes_text.replace('</h1>', '')
    nomeTimes = strTimes_text.split(' - ')
    timeCasa = nomeTimes[0]
    timeVisitante = nomeTimes[1]
    ODD=driver.find_element(By.XPATH,'//*[@id="odds-data-table"]')
    html=ODD.get_attribute('outerHTML')
#trabalhando os dados
    soup=BeautifulSoup(html,'html.parser')
    table=soup.find(id="odds-data-table")
    df_full=pandas.read_html(str(table))[0].head(14)
    df=df_full[['Bookmakers','1','X','2']]
    df.columns=['Casa',timeCasa,'x',timeVisitante]
    print(df)




def pegaMAXMIN():
    driver.get(url)
    driver.find_element(By.XPATH, '//*[@id="odds-data-table"]/div[1]/table/thead/tr/th[2]/a').click()
    print("Max")
    elemento=driver.find_element(By.XPATH,'//*[@id="odds-data-table"]/div[1]/table/tbody/tr[1]/td[2]/div')
    elemnto2=elemento.get_attribute('outerHTML')



    print(elemento.getText())
    #pega o primeiro valor da casa 1


pegaMAXMIN()
#entra_Partida(2)

#3.Printar essas informações
#4.Retornar a pagina principal e executar o mesmo passo até o final da pagina
driver.quit()
