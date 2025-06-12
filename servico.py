import flet as ft
import sqlite3
import time


def adicionar_ao_carrinho(e, page, callback_produto, valor):
    acessarcarrinho(page, callback_produto, valor)
    time.sleep(0.5)
    carr(page, callback_produto)


def conectaproduto(comando):
    conexao = sqlite3.connect('assets/barbershop.db')
    con = conexao.cursor()
    con.execute(comando)
    parametro = con.fetchall()
    return parametro


def conectacarrinho():
    print("Conectou no carrinho (modo teste)")
    conexao = sqlite3.connect('assets/barbershop.db')
    con = conexao.cursor()
    con.execute(
        'SELECT s.nome, s.imagem, c.preco, c.quantidade FROM carrinho c INNER JOIN servicos s ON s.id = c.idservico'
    )
    parametro = con.fetchall()
    return parametro


def acessarcarrinho(page, callback_produtos, id):
    parametro = conectaproduto('select * from servicos where id=' + str(id))
    conexao = sqlite3.connect('assets/barbershop.db')
    con = conexao.cursor()
    con.execute('INSERT INTO carrinho (idservico, quantidade, preco) VALUES (' +
                str(id) + ', 1, ' + str(parametro[0][3]) + ')')
    descricao = ft.Text('Produto salvo no carrinho: ' + str(id),
                        size=18,
                        color=ft.Colors.BLACK)
    conexao.commit()
    page.clean()
    page.add(descricao)
    time.sleep(3)


def carr(page, callback_produtos):
    conexao = sqlite3.connect('assets/barbershop.db')
    con = conexao.cursor()
    con.execute(
        'SELECT s.nome, s.imagem, c.preco, c.quantidade FROM carrinho c INNER JOIN servicos s ON s.id = c.idservico'
    )
    parametro = con.fetchall()
    vetor = []

    for carrinho in parametro:
        nome, imagem, preco, quantidade = carrinho
        carr = ft.Container(
            width=350,
            padding=20,
            margin=10,
            border_radius=20,
            bgcolor=ft.colors.WHITE,
            border=ft.border.all(1, ft.colors.GREY_300),
            shadow=ft.BoxShadow(
                blur_radius=15,
                color=ft.colors.with_opacity(0.2, ft.colors.BLACK),
                offset=ft.Offset(2, 2),
            ),
            content=ft.Column(
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=10,
                controls=[
                    ft.Text(nome, size=28, weight=ft.FontWeight.BOLD, color=ft.colors.BLACK),
                    ft.Text(f"R$ {preco},00", size=18, color=ft.colors.BLACK),
                    ft.Image(
                        src=imagem,
                        fit=ft.ImageFit.CONTAIN,
                        width=180,
                        height=180,
                        border_radius=10,
                    ),
                    ft.ElevatedButton(
                        text='Pagar',
                        style=ft.ButtonStyle(
                            bgcolor=ft.colors.BROWN_400,
                            color=ft.colors.BLACK,
                            padding=17,
                            shape=ft.RoundedRectangleBorder(radius=12),
                            overlay_color=ft.colors.BROWN_700,
                            text_style=ft.TextStyle(
                                size=18,
                                weight=ft.FontWeight.BOLD,
                            ),
                        ),
                    ),
                ]
            )
        )
        vetor.append(ft.Container(content=carr, alignment=ft.alignment.center))

    titulo = ft.Container(
        content=ft.Text(
            value='🛒 Seu Carrinho',
            size=36,
            weight=ft.FontWeight.BOLD,
            color=ft.colors.BLACK,
            text_align=ft.TextAlign.CENTER,
        ),
        alignment=ft.alignment.center,
        padding=20
    )

    btnvoltar = ft.ElevatedButton(
        "Voltar",
        bgcolor=ft.colors.GREY_700,
        color=ft.colors.WHITE,
        width=150,
        on_click=lambda e: callback_produtos()
    )

    botoes = ft.Row(
        controls=[btnvoltar],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )

    scroll_view = ft.ListView(
        controls=vetor,
        expand=True,
        spacing=10,
        padding=10,
        auto_scroll=False
    )

    page.clean()
    page.add(titulo, scroll_view, botoes)
    page.update()


def exibeprodutos(page, valor, callback_produto):
    parametro = conectaproduto(f'SELECT * FROM servicos WHERE id={valor}')
    page.clean()
    imagem = ft.Image(src=parametro[0][5], width=290, height=290, border_radius=7, fit=ft.ImageFit.CONTAIN)
    nome = ft.Text(parametro[0][1], size=24, style=ft.TextStyle(weight=ft.FontWeight.BOLD), color=ft.Colors.BLACK)
    descricao = ft.Text(parametro[0][2], size=18, color=ft.Colors.BLACK)
    preco = ft.Text(value='R$' + str(parametro[0][3]), size=22, color=ft.Colors.BLACK)
    duracao_minutos = ft.Text(value=str(parametro[0][4]) + ' Minutos', size=22, color=ft.Colors.BLACK)

    btnvoltar = ft.Container(
        content=ft.ElevatedButton("Voltar", bgcolor=ft.Colors.TRANSPARENT, color=ft.Colors.WHITE, width=190,
                                  on_click=lambda e: callback_produto()),
        alignment=ft.alignment.center
    )

    btncarrinho = ft.ElevatedButton(
        "Adicionar ao carrinho",
        bgcolor=ft.Colors.TRANSPARENT,
        color=ft.Colors.WHITE,
        width=190,
        on_click=lambda e: adicionar_ao_carrinho(e, page, callback_produto, valor)
    )

    btncarrinho.style = ft.ButtonStyle(
        bgcolor=ft.Colors.BLACK12,
        color=ft.Colors.WHITE,
        shape=ft.RoundedRectangleBorder(radius=12),
        overlay_color=ft.Colors.BROWN_700,
        text_style=ft.TextStyle(
            size=18,
            weight=ft.FontWeight.BOLD,
        ),
    )

    botoes = ft.Row(controls=[btnvoltar, btncarrinho], alignment=ft.MainAxisAlignment.CENTER, spacing=20)

    conteudo = ft.Container(
        content=ft.Column(
            controls=[
                ft.Column(
                    controls=[imagem, nome, descricao, preco, duracao_minutos],
                    horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                    spacing=10
                ),
                botoes
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
            expand=True
        ),
        padding=30
    )

    page.add(conteudo)
    page.update()


def produtos(page, callback_login):
    page.clean()
    page.bgcolor = ft.Colors.WHITE
    parametro = conectaproduto('SELECT * FROM servicos')
    vetor = []

    for produto in parametro:
        id, nome, descricao, preco, duracao_minutos, imagem = produto
        imgprodutos = ft.Container(
            content=ft.Row([
                ft.GestureDetector(
                    ft.Image(
                        src=imagem,
                        width=115,
                        height=115,
                        border_radius=7,
                        fit=ft.ImageFit.CONTAIN
                    ),
                    on_tap=lambda e, id=id: exibeprodutos(page, id, lambda: produtos(page, callback_login)),
                ),
                ft.Text(nome, color=ft.Colors.BLACK),
                ft.Text(preco, color=('#808080')),
                ft.Text(f"{duracao_minutos} minutos", color=ft.Colors.BLACK)
            ]),
            alignment=ft.alignment.center,
            padding=10,
            border=ft.border.all(width=1, color=ft.Colors.GREY),
            border_radius=9
        )
        vetor.append(imgprodutos)

    btnvoltar = ft.Container(
        content=ft.ElevatedButton("Voltar", bgcolor=ft.Colors.TRANSPARENT, color=ft.Colors.WHITE, width=150,
                                  on_click=lambda e: callback_login()),
        alignment=ft.alignment.center,
        padding=30
    )

    page.add(
        ft.Image(src='img/logomarca.png', width=75, height=75, border_radius=5),
        ft.ListView(
            controls=[*vetor, btnvoltar],
            expand=True,
            spacing=10,
            padding=10,
            auto_scroll=False
        )
    )
    page.update()
