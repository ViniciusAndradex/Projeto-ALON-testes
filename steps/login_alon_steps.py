from behave import *
from login import Login
from pages.login_alon_page import ALONLoginPage
from selenium.webdriver.common.by import By

obj_alon_login = ALONLoginPage()
obj_login = Login()

@given(u'que realiza o acesso a página do ALON')
def step_impl(context):
    obj_alon_login.acessar_url('http://localhost:5173/')

@given(u'que preenche o campo de e-mail e senha')
def step_impl(context):
    obj_login.logar()
    obj_alon_login.clicar_login(padrao=True)

@given(u'que preenche o campo de e-mail com branco e senha valida')
def step_impl(context):
    obj_login.logar('', '123456')
    obj_alon_login.clicar_login(padrao=True)

@given(u'que preenche o campo de e-mail com invalido e senha valida')
def step_impl(context):
    obj_login.logar('vinicius@g ', '123456')
    obj_alon_login.clicar_login(padrao=True)

@given(u'que preenche o campo de e-mail valido e senha')
def step_impl(context):
    obj_login.logar('vinicius@gmail.com', '123456')
    obj_alon_login.clicar_login(padrao=True)

@given(u'que preenche o campo de e-mail com espaço no inicio e senha valida')
def step_impl(context):
    obj_login.logar(' vinicius@gmail.com', '123456')
    obj_alon_login.clicar_login(padrao=True)

@given(u'que preenche o campo de e-mail com espaço no final e inicio e senha valida')
def step_impl(context):
    obj_login.logar(' vinicius@gmail.com ', '123456')
    obj_alon_login.clicar_login(padrao=True)

@given(u'que preenche o campo de e-mail com espaço no final e senha valida')
def step_impl(context):
    obj_login.logar('vinicius@gmail.com ', '123456')
    obj_alon_login.clicar_login(padrao=True)

@given(u'que preenche o campo de e-mail valido e senha em branco')
def step_impl(context):
    obj_login.logar('vinicius@gmail.com', '')
    obj_alon_login.clicar_login(padrao=True)

@given(u'que preenche o campo de e-mail valido e senha invalida')
def step_impl(context):
    obj_login.logar('vinicius@gmail.com', '132')
    obj_alon_login.clicar_login(padrao=True)

@given(u'que acessa a tela do google e faça o login')
def step_impl(context):
    context.janela_atual = obj_alon_login.driver.current_window_handle
    obj_alon_login.clicar_login(google=True)
    for window_handle in obj_alon_login.driver.window_handles:
        if window_handle != context.janela_atual:
            obj_alon_login.driver.switch_to.window(window_handle)
    obj_login.logar(google=True)

@then(u'devo efetuar o login.')
def step_impl(context):
    # if obj_alon_login.driver.window_handles != context.janela_atual:
    #     obj_alon_login.driver.switch_to.window(context.janela_atual)
    assert 'entrou' in obj_alon_login.driver.find_element(By.XPATH, '//div/h1').text

@then(u'o sistema deve apresentar uma mensagem campo obrigatorio.')
def step_impl(context):
    assert 'O campo é obrigatório' in obj_alon_login.driver.find_element(By.ID, 'outlined-email-helper-text').text

@then(u'o sistema deve apresentar uma mensagem email invalido.')
def step_impl(context):
    assert 'E-mail inválido' in obj_alon_login.driver.find_element(By.ID, 'outlined-email-helper-text').text

@then(u'o sistema deve apresentar uma mensagem senha minima 5 caractere.')
def step_impl(context):
    assert 'A senha deve ter no mínimo 5 caracteres' in obj_alon_login.driver.find_element(By.ID, 'outlined-senha-helper-text').text