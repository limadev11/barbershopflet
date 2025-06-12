import flet as ft
import sqlite3
import bdconfig


def acessar(e, email, senha, callback_menu, page):
            conexao = sqlite3.connect('assets/barbershop.db',check_same_thread=False)
            con = conexao.cursor()
            con.execute('SELECT COUNT(*) FROM usuario WHERE email = ? AND senha = ?', (email.value, senha.value))
            resultado = con.fetchone()
            if resultado[0] == 1:
                # Aqui você pode chamar a função para exibir o menu principal
                callback_menu(page)
                print("Login realizado com sucesso!")  # debug
            else:
                page.snack_bar = ft.SnackBar(ft.Text("Email ou senha incorretos!"))
                page.snack_bar.open = True
                page.update()

def login(page: ft.Page, callback_menu, callback_cadastro):
    page.clean()
    # Conectar ao banco de dados
    conn = sqlite3.connect('assets/barbershop.db')
    cursor = conn.cursor()


    img = ft.Container(
        content=ft.Image(src="img/logo.png", width=400, height=400, fit=ft.ImageFit.CONTAIN),
        alignment=ft.alignment.center,
        padding=20,
    )

    input_email = ft.TextField(
        value='',
        label="Email",
        prefix_icon=ft.icons.PERSON,
        bgcolor=ft.colors.WHITE,
        color=ft.colors.BLACK,
        border_color=ft.colors.BLACK,
        border_radius=8,
    )

    input_senha = ft.TextField(
        value='',
        label="Senha",
        password=True,
        prefix_icon=ft.icons.LOCK,
        bgcolor=ft.colors.WHITE,
        color=ft.colors.BLACK,
        border_color=ft.colors.BLACK,
        border_radius=8,
    )

    botao_login = ft.ElevatedButton(
        'Entrar',
        bgcolor=ft.colors.BLACK,
        color=ft.colors.WHITE,
        width=200,
        on_click=lambda e: acessar(e, input_email, input_senha, callback_menu, page)
    )

    botao_cadastro = ft.TextButton(
        "Não tem conta? Cadastre-se",
        style=ft.ButtonStyle(color="#FFD700"),
        on_click=callback_cadastro
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
        [
            ft.Image('img/fundo.jpg'),
            ft.Container(
                content=login_container,
                alignment=ft.alignment.center
            )
        ]
    ))
