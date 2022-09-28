from selenium.webdriver.common.by import By
from browser import Browser

class ALONLoginPageLocator(object):
    ID_EMAIL = 'outlined-email'
    ID_SENHA = 'outlined-senha'
    ID_LOGIN = 'vinicius-tome-seu-id'
    XPATH_LOGIN_GOOGLE = '//div/button[1]'
    ID_EMAIL_GOOGLE = 'identifierId'
    XPATH_SENHA_GOOGLE = '//div[1]/div[1]/div[2]/div/div[2]/div/div/div[2]/div/div[1]/div/form/span/section/div/div/div[1]/div[1]/div/div/div/div/div[1]/div/div[1]/div'
    ID_PROX_EMAIL_GOOGLE = 'identifierNext'
    ID_PROX_SENHA_GOOGLE = 'passwordNext'
    
class ALONLoginPage(Browser):

    def acessar_url(self, url):
        self.driver.get(url)
    
    def escrever_email(self, email=None, google=False):
        if google:
            email_login = self.driver.find_element(By.ID, ALONLoginPageLocator.ID_EMAIL_GOOGLE)
            email_login.send_keys('testesprojetoalon@gmail.com')
            return
        email_login = self.driver.find_element(By.ID, ALONLoginPageLocator.ID_EMAIL)
        email_login.send_keys(email)
    
    def escrever_senha(self, senha=None, google=False):
        if google:
            email_login = self.driver.find_element(By.XPATH, ALONLoginPageLocator.XPATH_SENHA_GOOGLE)
            email_login.send_keys('@123456!')
            return
        senha_login = self.driver.find_element(By.ID, ALONLoginPageLocator.ID_SENHA)
        senha_login.send_keys(senha)

    def clicar_login(self, padrao=False, google=False, prox_email_google=False, prox_senha_google=False):
        if padrao:
            self.driver.find_element(By.ID, ALONLoginPageLocator.ID_LOGIN).click()
        if google:
            self.driver.find_element(By.XPATH, ALONLoginPageLocator.XPATH_LOGIN_GOOGLE).click()
        if prox_email_google:
            self.driver.find_element(By.ID, ALONLoginPageLocator.ID_PROX_EMAIL_GOOGLE).click()
        if prox_senha_google:
            self.driver.find_element(By.ID, ALONLoginPageLocator.ID_PROX_SENHA_GOOGLE).click()