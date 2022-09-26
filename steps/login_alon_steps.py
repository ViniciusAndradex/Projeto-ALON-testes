from behave import *
from login import Login
from pages.login_alon_page import ALONLoginPage

obj_alon_login = ALONLoginPage()
obj_login = Login()

@given(u'que realiza o acesso a página do ALON')
def step_impl(context):
    obj_alon_login.acessar_url('http://localhost:5174/')

@given(u'que preenche o campo de e-mail e senha')
def step_impl(context):
    obj_login.logar()
    obj_alon_login.clicar_login()

@given(u'que preenche o campo de e-mail com branco e senha valida')
def step_impl(context):
    obj_login.logar('', '123456')
    obj_alon_login.clicar_login()

@given(u'que preenche o campo de e-mail com invalido e senha valida')
def step_impl(context):
    obj_login.logar('vinicius@g ', '123456')
    obj_alon_login.clicar_login()

@given(u'que preenche o campo de e-mail valido e senha')
def step_impl(context):
    obj_login.logar('vinicius@gmail.com', '123456')
    obj_alon_login.clicar_login()

@given(u'que preenche o campo de e-mail com espaço no inicio e senha valida')
def step_impl(context):
    obj_login.logar(' vinicius@gmail.com', '123456')
    obj_alon_login.clicar_login()

@given(u'que preenche o campo de e-mail com espaço no final e inicio e senha valida')
def step_impl(context):
    obj_login.logar(' vinicius@gmail.com ', '123456')
    obj_alon_login.clicar_login()

@given(u'que preenche o campo de e-mail com espaço no final e senha valida')
def step_impl(context):
    obj_login.logar('vinicius@gmail.com ', '123456')
    obj_alon_login.clicar_login()

@given(u'que preenche o campo de e-mail valido e senha em branco')
def step_impl(context):
    obj_login.logar('vinicius@gmail.com', '')
    obj_alon_login.clicar_login()

@given(u'que preenche o campo de e-mail valido e senha invalida')
def step_impl(context):
    obj_login.logar('vinicius@gmail.com', '132')

@then(u'devo falhar no login.')
def step_impl(context):
    pass


@then(u'devo efetuar o login.')
def step_impl(context):
    pass