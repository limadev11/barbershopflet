import flet as ft
import sqlite3

from menu import exibemenu
from bdconfig import bdconfig

select = bdconfig()

def login(page, callback_menu, callback_cadastro):
    page.clean()

    def acessar(e):
        conexao = sqlite3.connect('assets/barbershop.db', check_same_thread=False)
        con = conexao.cursor()
        con.execute('select count(*) from usuario where email = ? and senha = ?', (input_email.value, input_senha.value))
        resultado = con.fetchone()
        if resultado[0] == 0:
            page.open(txtmensagem)
            page.update()
            login(page, callback_menu, callback_cadastro)
            page.update()
        else:
            page.update()
            exibemenu(page, callback_menu)
            
    img = ft.Container(
        content=ft.Image(src="img/logo.png", width=400, height=400, fit=ft.ImageFit.CONTAIN),
        alignment=ft.alignment.center,
        padding=20,
    )

    input_email = ft.TextField(
        label="Email",
        prefix_icon=ft.icons.PERSON,
        border_radius=8,
    )

    input_senha = ft.TextField(
        label="Senha",
        password=True,
        prefix_icon=ft.icons.LOCK,
        border_radius=8,
    )

    botao_login = ft.ElevatedButton(
        'Entrar',
        bgcolor=ft.colors.BLACK,
        color=ft.colors.WHITE,
        width=200,
        on_click=acessar
    )

    botao_cadastro = ft.TextButton(
        "Não tem conta? Cadastre-se",
        on_click=callback_cadastro
    )
    txtmensagem = ft.AlertDialog(
            content=ft.Text("Erro de Senha ou Email", color="white", size=20, weight="bold"),
            alignment=ft.alignment.center,
            bgcolor="#333333",
        )

    login_container = ft.Column(
        controls=[
            img,
            input_email,
            input_senha,
            botao_login,
            botao_cadastro
        ],
        spacing=20,
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER
    )
    
    page.add(ft.Stack(
        [ft.Image('img/fundo.jpg'),
         ft.Container(ft.Column(
             [
                 login_container,
            ],
         )
        )
        ]
    )
    )

    page.add(login_container)
    