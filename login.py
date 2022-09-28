from pages.login_alon_page import ALONLoginPage

class Login(ALONLoginPage):

    def logar(self, email=None, senha=None, google=False):
        if google:
            super().escrever_email(google=True)
            super().clicar_login(prox_email_google=True)
            super().browser_wait(6)
            super().escrever_senha(google=True)
            super().clicar_login(prox_senha_google=True)
        else:
            super().escrever_email(email)
            super().escrever_senha(senha)
