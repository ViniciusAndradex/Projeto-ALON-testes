# language: pt

Funcionalidade: Testar o sistema de login do ALON
    
    Contexto: Acessar a página do ALON
        Dado que realiza o acesso a página do ALON

    Cenário: Entrar no site e tentar efetuar login com um e-mail valido porem com espaço no final
        Dado que preenche o campo de e-mail com espaço no final e senha valida
        Então o sistema deve apresentar uma mensagem email invalido.
