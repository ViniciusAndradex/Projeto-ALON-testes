# language: pt

Funcionalidade: Testar o sistema de login do ALON
    
    Contexto: Acessar a página do ALON
        Dado que realiza o acesso a página do ALON

    Cenário: Entrar no site e tentar efetuar login com um e-mail valido e senha invalida
        Dado que preenche o campo de e-mail valido e senha invalida
        Então devo falhar no login.