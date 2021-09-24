from selenium import webdriver
from time import sleep

def entrarNoSite(login, senha):
    driver = webdriver.Firefox()
    driver.get(" url ")
    sleep(1)
    loginXpath = ('//*[@id="login_id"]')
    senhaXpath = ('//*[@id="senha_id"]')
    botaoEntrarXpath = ('//*[@id="botaoLogin_id"]')
    inputArquivoXpath = ('//*[@id="file_id"]')
    minhaImagem = (" caminho do arquivo ") # Ex. C:\\Users\\User\\Desktop\\minhaFoto.png
    textoXpath = ('/html/body/div/div[2]/div')
    botaoSairXpath = ('/html/body/div/div[3]/button')
    driver.find_element_by_xpath(loginXpath).send_keys(login)
    driver.find_element_by_xpath(senhaXpath).send_keys(senha)
    driver.find_element_by_xpath(botaoEntrarXpath).click()
    sleep(1)
    driver.find_element_by_xpath(inputArquivoXpath).send_keys(minhaImagem)
    sleep(5)
    print(driver.find_element_by_xpath(textoXpath).text)
    driver.find_element_by_xpath(botaoSairXpath).click()
    driver.quit()

for x in range(5):
    entrarNoSite("meuUsuario", "123")