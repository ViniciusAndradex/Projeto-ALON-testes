from selenium.webdriver.common.by import By
from browser import Browser

class ALONLoginPageLocator(object):
    ID_EMAIL = 'outlined-email'
    ID_SENHA = 'outlined-senha'
    XPATH_LOGIN = '//div/button[2]'

class ALONLoginPage(Browser):

    def acessar_url(self, url):
        self.driver.get(url)
    
    def escrever_email(self, email):
        email_login = self.driver.find_element(By.ID, ALONLoginPageLocator.ID_EMAIL)
        email_login.send_keys(email)
    
    def escrever_senha(self, senha):
        senha_login = self.driver.find_element(By.ID, ALONLoginPageLocator.ID_SENHA)
        senha_login.send_keys(senha)

    def clicar_login(self):
       j =  self.driver.find_element(By.XPATH, ALONLoginPageLocator.XPATH_LOGIN)
       j.click()
