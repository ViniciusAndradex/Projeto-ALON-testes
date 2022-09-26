from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from browser import Browser

class ALonPrimeiroAcessoPageLocator(object):
    ID_INPUT_EMAIL = "alguma coisa 1"
    ID_INPUT_CONFIRMAR_EMAIL = "alguma coisa 2"
    ID_INPUT_SENHA = "alguma coisa 3"
    ID_INPUT_CONFIRMAR_SENHA = "alguma coisa 4"
    ID_CLICK_ACESSAR = "alguma coisa 5"

class ALonPrimeiroAcessoPage(Browser):
    
    def acessar_pag_primeiro_acesso(self, url):
        self.driver.get(url)

    def escrever_email(self, email):
        inserir_email = self.driver.find_element(
            By.ID, ALonPrimeiroAcessoPageLocator.ID_INPUT_EMAIL)
        inserir_email.send_keys(email)

    def escrever_senha(self, senha):
        inserir_senha = self.driver.find_element(
            By.ID, ALonPrimeiroAcessoPageLocator.ID_INPUT_SENHA)
        inserir_senha.send_keys(senha)

    def confirmar_senha(self, confirma_senha):
        inserir_confirma_senha = self.driver.find_element(
            By.ID, ALonPrimeiroAcessoPageLocator.ID_INPUT_CONFIRMAR_SENHA)
        inserir_confirma_senha.send_keys(confirma_senha)

    def clicar_acessar(self):
        clicar_em_acessar = self.driver.find_element(
            By.ID, ALonPrimeiroAcessoPageLocator.ID_CLICK_ACESSAR)
        clicar_em_acessar.click()
