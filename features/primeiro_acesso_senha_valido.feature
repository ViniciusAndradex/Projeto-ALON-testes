# language: pt


Funcionalidade: Testar o campo de Senha na página de primeiro acesso do ALon

    Contexto: acessar página teste
        Dado que acessa a seção de primeiro acesso da página ALon em específico o campo de Senha
    
    Cenário: acessar a página de primeiro acesso, inserir uma senha válida no campo Senha e efetuar o login 
        Dado que preenche o campo Email
        Dado que preenche o campo Confirmar Email 
        Dado que preenche o campo Senha VÁLIDO
        Dado que preenche o campo Confirmar Senha
        Quando clico no botão Acessar
        Então acessar o sistema