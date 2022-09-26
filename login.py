from pages.login_alon_page import ALONLoginPage

class Login(ALONLoginPage):

    def logar(self, email, senha):
        super().escrever_email(email)
        super().escrever_senha(senha)
