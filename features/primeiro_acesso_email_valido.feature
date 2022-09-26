# language: pt


Funcionalidade: Testar o campo de email na página de primeiro acesso do ALon

    Contexto: acessar página teste
        Dado que acessa a seção de primeiro acesso da página ALon em específico o campo de Email
    
    Cenário: acessar a página de primeiro acesso, inserir um email válido no campo Email e efetuar o login 
        Dado que preenche o campo Email VÁLIDO
        Dado que preenche o campo Confirmar Email
        Dado que preenche o campo Senha
        Dado que preenche o campo Confirmar Senha
        Quando clico no botão Acessar
        Então devo acessar o sistema