from behave import *
from selenium.webdriver.common.by import By
from time import sleep
from pages.primeiro_acesso_ALon_page import ALonPrimeiroAcessoPage

ALPrimeiroAcesso = ALonPrimeiroAcessoPage()

@given(u'que acessa a seção de primeiro acesso da página ALon em específico o campo de Confirmar Email')
def step_impl(context):
    ALPrimeiroAcesso.acessar_pag_primeiro_acesso('http://localhost:5173/primeiro-acesso')

@given(u'que preenche o campo Email')
def step_impl(context):
    ALPrimeiroAcesso.escrever_email('aksdaskn@gmail.com')


@given(u'que preenche o campo Confirmar Email EM BRANCO')
def step_impl(context):
    ALPrimeiroAcesso.confirmar_email('')


@given(u'que preenche o campo Senha')
def step_impl(context):
    ALPrimeiroAcesso.escrever_senha('askjhdba')

@given(u'que preenche o campo Confirmar Senha')
def step_impl(context):
    ALPrimeiroAcesso.confirmar_senha('askjhdba')


@when(u'clico no botão Acessar')
def step_impl(context):
    ALPrimeiroAcesso.clicar_acessar()


@then(u'devo falhar em acessar o sistema')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then devo falhar em acessar o sistema') #Devo dar o assert em algum elemento indicando que houve algum erro em acessar a página


@given(u'que preenche o campo Confirmar Email INVÁLIDO')
def step_impl(context):
    ALPrimeiroAcesso.confirmar_email(' a w qda dawd @ 31')


@given(u'que preenche o campo Confirmar Email VALIDO')
def step_impl(context):
    ALPrimeiroAcesso.confirmar_email('aksdaskn@gmail.com')


@then(u'devo acessar o sistema')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then devo acessar o sistema') #Devo dar o assert em algum elemento indicando que o login foi efetuado com sucesso


@given(u'que acessa a seção de primeiro acesso da página ALon em específico o campo de Confirmar Senha')
def step_impl(context):
    ALPrimeiroAcesso.confirmar_email('askjhdba')


@given(u'que preenche o campo Confirmar Email')
def step_impl(context):
    ALPrimeiroAcesso.confirmar_email('aksdaskn@gmail.com')


@given(u'que preenche o campo Confirmar Senha EM BRANCO')
def step_impl(context):
    ALPrimeiroAcesso.confirmar_senha('')


@given(u'que preenche o campo Confirmar Senha INVÁLIDO')
def step_impl(context):
    ALPrimeiroAcesso.confirmar_senha(' as j k adsa sadas ')


@given(u'que preenche o campo Confirmar Senha VÁLIDO')
def step_impl(context):
    ALPrimeiroAcesso.confirmar_senha('askjhdba')


@given(u'que acessa a seção de primeiro acesso da página ALon em específico o campo de Email')
def step_impl(context):
    ALPrimeiroAcesso.escrever_email('aksdaskn@gmail.com')

@given(u'que preenche o campo Email EM BRANCO')
def step_impl(context):
    ALPrimeiroAcesso.escrever_email('')

@given(u'que preenche o campo Email INVÁLIDO')
def step_impl(context):
    ALPrimeiroAcesso.escrever_email(' a w qda dawd @ 31')

@given(u'que preenche o campo Email VÁLIDO')
def step_impl(context):
    ALPrimeiroAcesso.escrever_email('aksdaskn@gmail.com')

@given(u'que acessa a seção de primeiro acesso da página ALon em específico o campo de Senha')
def step_impl(context):
    ALPrimeiroAcesso.escrever_senha('askjhdba')

@given(u'que preenche o campo Senha EM BRANCO')
def step_impl(context):
    ALPrimeiroAcesso.escrever_senha('')

@given(u'que preenche o campo Senha INVÁLIDO')
def step_impl(context):
    ALPrimeiroAcesso.escrever_senha('a as fka makd a ak')

@given(u'que preenche o campo Senha VÁLIDO')
def step_impl(context):
    ALPrimeiroAcesso.escrever_senha('askjhdba')


@then(u'acessar o sistema')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then acessar o sistema') #Devo dar o assert em algum elemento que indica que foi um sucesso acessar a página seguinte