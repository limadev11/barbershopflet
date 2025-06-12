import flet as ft
from flet import Icon
from index import login
from cadastro import cadastro
from servico import produtos

def main(page: ft.Page):
    # Configurações da janela
    page.title = 'BarberShop'
    page.window.width = 560
    page.window.height = 800
    page.window.center()
    # page.window.favicon = "img/barber.jfif"

    # Funções de navegação
    def abre_login(e=None):
        login(page, abre_produto, abre_cadastro)


    def abre_cadastro(e=None):
        cadastro(page, abre_login)

    def abre_produto(e=None):
        produtos(page, abre_login)

    # Abre a tela de login ao iniciar
    abre_login()

# Inicialização do app
ft.app(target=main, assets_dir="assets")