# language: pt


Funcionalidade: Testar o campo de Email na página de primeiro acesso do ALon

    Contexto: acessar página teste
        Dado que acessa a seção de primeiro acesso da página ALon em específico o campo de Email
    
    Cenário: acessar a página de primeiro acesso, inserir caracteres inválidos no campo Email e tentar efetuar o login 
        Dado que preenche o campo Email INVÁLIDO
        Dado que preenche o campo Confirmar Email
        Dado que preenche o campo Senha
        Dado que preenche o campo Confirmar Senha 
        Quando clico no botão Acessar
        Então devo falhar em acessar o sistema