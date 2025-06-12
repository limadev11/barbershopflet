import flet as ft
import sqlite3

def cadastro(page, callback_login):
    page.clean()
    def gravar(e):
        conexao = sqlite3.connect('barbershop.db', check_same_thread=False)
        con = conexao.cursor()
        con.execute('insert into usuario (nome, sobrenome, email, telefone, senha) values (?, ?, ?, ?, ?)',
                    (nome_input.value, sobrenome_input.value, email_input.value, telefone_input.value, senha_input.value))
        conexao.commit()
        conexao.close()
        txtmensagem = 'Cadastro realizado com sucesso!'
        page.update()
        page.go(txtmensagem)
        page.update()
        import time 
        time.sleep(2)
        callback_login()
    img = ft.Container(
        content=ft.Image(
            src='img/logo1.png',
            width=200,
            height=200,
            fit=ft.ImageFit.CONTAIN,
        ),
        alignment=ft.alignment.center,
        padding=20
    )

    nome_input = ft.TextField(label="Digite seu nome", prefix_icon=ft.icons.PERSON, width=300, height=50, text_style=ft.TextStyle(color=ft.colors.BLACK), bgcolor=ft.colors.WHITE, border_radius=8)
    sobrenome_input = ft.TextField(label="Digite seu sobrenome", prefix_icon=ft.icons.PERSON, width=300, height=50, text_style=ft.TextStyle(color=ft.colors.BLACK), bgcolor=ft.colors.WHITE, border_radius=8)
    email_input = ft.TextField(label="Digite seu E-mail", prefix_icon=ft.icons.EMAIL, width=300, height=50, text_style=ft.TextStyle(color=ft.colors.BLACK), bgcolor=ft.colors.WHITE, border_radius=8)
    telefone_input = ft.TextField(label="Digite seu telefone", prefix_icon=ft.icons.PHONE, width=300, height=50, text_style=ft.TextStyle(color=ft.colors.BLACK), bgcolor=ft.colors.WHITE, border_radius=8)
    senha_input = ft.TextField(label='Digite sua senha', prefix_icon=ft.icons.LOCK, password=True, can_reveal_password=True, width=300, height=50, text_style=ft.TextStyle(color=ft.colors.BLACK), bgcolor=ft.colors.WHITE, border_radius=8)
    senhaconfirm_input = ft.TextField(label='Confirme sua senha', prefix_icon=ft.icons.LOCK, password=True, can_reveal_password=True, width=300, height=50, text_style=ft.TextStyle(color=ft.colors.BLACK), bgcolor=ft.colors.WHITE, border_radius=8)

    botaoexecutar = ft.ElevatedButton(
        'Efetuar Cadastro',
        bgcolor=ft.colors.BLACK,
        color=ft.colors.WHITE,
        width=200,
        on_click=gravar,
        )

    botaovoltar = ft.ElevatedButton(
        'Voltar',
        icon=ft.icons.ARROW_BACK,
        bgcolor=ft.colors.BLACK,
        color=ft.colors.WHITE,
        width=200,
        on_click=callback_login
    )

    page.add(
        ft.Column(
            [
                img,
                ft.Container(content=nome_input, alignment=ft.alignment.center, padding=3),
                ft.Container(content=sobrenome_input, alignment=ft.alignment.center, padding=3),
                ft.Container(content=email_input, alignment=ft.alignment.center, padding=3),
                ft.Container(content=telefone_input, alignment=ft.alignment.center, padding=3),
                ft.Container(content=senha_input, alignment=ft.alignment.center, padding=3),
                ft.Container(content=senhaconfirm_input, alignment=ft.alignment.center, padding=3),
                ft.Container(content=botaoexecutar, alignment=ft.alignment.center, padding=3),
                ft.Container(content=botaovoltar, alignment=ft.alignment.center, padding=3),
            ],
        )
    )

    page.update()
