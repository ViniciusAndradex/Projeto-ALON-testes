# language: pt


Funcionalidade: Testar o campo de Confirmar a senha na página de primeiro acesso do ALon

    Contexto: acessar página teste
        Dado que acessa a seção de primeiro acesso da página ALon em específico o campo de Confirmar Senha
    
    Cenário: acessar a página de primeiro acesso, inserir caracteres válidos no campo Confirmar Senha e efetuar o login 
        Dado que preenche o campo Email
        Dado que preenche o campo Confirmar Email
        Dado que preenche o campo Senha
        Dado que preenche o campo Confirmar Senha VÁLIDO
        Quando clico no botão Acessar
        Então devo acessar o sistema
