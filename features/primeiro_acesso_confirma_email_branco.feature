# language: pt


Funcionalidade: Testar o campo de Confirmar o Email na página de primeiro acesso do ALon

    Contexto: acessar página teste
        Dado que acessa a seção de primeiro acesso da página ALon em específico o campo de Confirmar Email
    
    Cenário: acessar a página de primeiro acesso, não inserir nenhum caractere no campo Confirmar Email e tentar efetuar o login 
        Dado que preenche o campo Email
        Dado que preenche o campo Confirmar Email EM BRANCO
        Dado que preenche o campo Senha
        Dado que preenche o campo Confirmar Senha 
        Quando clico no botão Acessar
        Então devo falhar em acessar o sistema