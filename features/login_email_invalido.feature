# language: pt

Funcionalidade: Testar o sistema de login do ALON
    
    Contexto: Acessar a página do ALON
        Dado que realiza o acesso a página do ALON

    Cenário: Entrar no site e tentar efetuar login com um e-mail invalido
        Dado que preenche o campo de e-mail com invalido e senha valida
        Então devo falhar no login.
