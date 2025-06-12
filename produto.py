import flet as ft
import sqlite3
import time

# BANCO DE DADOS QUE CONECTA OS PRODUTOS
def conectaproduto():
    conexao = sqlite3.connect('assets/bardojoao.db', check_same_thread=False)
    con = conexao.cursor()
    con.execute('select * from produtos')
    parametro = con.fetchall()
    return(parametro)

# BANCO DE DADOS QUE PUXA OS CARRINHOS
def conectacarrinho():
    conexao = sqlite3.connect('assets/bardojoao.db', check_same_thread=False)
    con = conexao.cursor()
    con.execute('select p.nome, c.quantidade, p.imagem, c.preco, c.quantidade*c.preco Total from carrinho c inner join produtos p on p.id = c.idproduto')
    campos = con.fetchall()
    return(campos)

def warning (informacao, cor): 
        return(ft.AlertDialog(
            shape=ft.RoundedRectangleBorder(radius=5),#define as bordas, deixando ele arredondado a 5 pixels
            content=ft.Container(
                content=ft.Text(
                    value=informacao,
                    size=32,
                    weight=ft.FontWeight.BOLD,  #deixa o texto em negrito
                    color="#000000",
                    text_align=ft.TextAlign.CENTER, #alinho o texto ao centro
                ),
                border_radius=12,
            ), 
            bgcolor=cor
            )
        )

def adccarrinho(page, id, callback_produtos):

    conexao = sqlite3.connect('assets/bardojoao.db', check_same_thread=False)
    con = conexao.cursor()
    con.execute('update carrinho set quantidade = quantidade +' +str(1)+ ' where id ='+str(id))
    conexao.commit()
    conexao.close() 
    page.open(warning(informacao="Adicionado ao\nCarrinho!", cor="#f43e2d"))
    page.update()
    time.sleep(3)
    callback_produtos()

# AQUI ESTÁ O PROBLEMA
def acessarcarrinho(page, callback_produtos):
    page.clean()
    page.fonts = {"fonte": 'fonte.ttf', "sobrefonte": 'sobrefonte.ttf'}
    campos = conectacarrinho()
    vetor = []

    # Distribuição de cada bloco
    for carrinho in campos:
        nome, quantidade, imagem, preco, total= carrinho
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
                ft.Text(f"Quantidade: {quantidade}", size=18, color=ft.colors.BLACK),
                ft.Text(f"R$ {preco},00", size=18, color=ft.colors.BLACK),
                ft.Text(f"Valor Total: {total}", size=18, color=ft.colors.BLACK),
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
                            font_family='sobrenome',
                            ),
                        ),
                    ),
                ]
            )
        )
        # centralizar logotipo
        centralizarcarr = ft.Container(content=carr, alignment=ft.alignment.center)
        vetor.append(centralizarcarr)
    #titulo
    texttitulo = ft.Container(
    ft.Text(
        value='Seu Carrinho',
        size=36,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        text_align=ft.TextAlign.CENTER,
    ),
    bgcolor=ft.colors.YELLOW,
    border_radius=10,
    padding=20,
    width=450,
    alignment=ft.alignment.center,
    # vertical_alignment=ft.CrossAxisAlignment.CENTER,
    border=ft.border.all(2, ft.colors.BLACK),
    shadow=ft.BoxShadow(
        spread_radius=2,
        blur_radius=8,
        color=ft.colors.BLACK,
        offset=ft.Offset(4, 4),
    )
    )
    botaoprodutos = ft.Container(
        content=ft.ElevatedButton(
        text='Voltar aos produtos',
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLUE_400,
            color=ft.colors.BLACK,
            padding=15,
            shape=ft.RoundedRectangleBorder(radius=12),
            overlay_color=ft.colors.BLUE_600,  # cor ao clicar
            text_style = ft.TextStyle(size=15, weight=ft.FontWeight.BOLD, font_family='sobrefonte'),
        ),
        on_click=lambda e: callback_produtos(),
    ),
    alignment=ft.alignment.center,
    )
    
    # Centralizar titulo
    centertitulo = ft.Container(
    content=texttitulo, alignment=ft.alignment.center, padding=10)
    tudocarrinhos = ft.Container(
        content= ft.Column(
            controls= [
                centertitulo,
                botaoprodutos,
                *vetor,
            ]
        ),
        )
    lista_de_carrinhos = ft.ListView(
        controls=[ft.Column(
            controls=[tudocarrinhos]
        )],
        expand=True,
        auto_scroll=False,
    )
    page.add(ft.Stack(
        controls = [ft.Image('assets/img/fundoprodutos.jpg'),
         ft.Container(ft.Column(
             [
                lista_de_carrinhos,
             ],
             alignment=ft.MainAxisAlignment.CENTER
         )
        )
        ], expand=True
    )
    )
    page.update()
# ACESSAR A ÁREA DE DESCRIÇÃO DE CADA PRODUTOS
def descprodutos(page, id, callback_produtos):
    # BANCO DE DADOS QUE CONECTA AS INFORMAÇÕES A DESCRIÇÃO
    conexao = sqlite3.connect('assets/bardojoao.db', check_same_thread=False)
    con = conexao.cursor()
    con.execute('select * from produtos where id='+str(id))
    campos = con.fetchone()
    page.clean()


    # TODA ÁREA DESCRITIVA
    cartao = ft.Container(
        width=560,
        height=800,
        padding=20,
        border_radius=20,
        bgcolor=ft.colors.YELLOW_400,
        content=ft.Column(
            controls= [
                ft.Container(
                alignment = ft.alignment.center,
                content = ft.Image(src=campos[2], fit=ft.ImageFit.CONTAIN, border_radius = 10,),
                ),

                ft.Text(
                    value=campos[1],
                    size=20,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.colors.BLACK,
                ),
                ft.Text(
                    value=campos[4],
                    size=25,
                    text_align=ft.TextAlign.LEFT,
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Row(
                    controls=[
                        ft.Text(
                    value="Preço:",
                    size=30,
                    weight=ft.FontWeight.BOLD,
                    text_align=ft.TextAlign.CENTER,
                    color=ft.colors.BLACK,
                ),
                ft.Text(
                    value="R$ "+str(campos[3])+",00",
                    size=30,
                    text_align=ft.TextAlign.LEFT,
                    color=ft.colors.BLACK,
                    weight=ft.FontWeight.BOLD
                ),
                ft.Container(
                ),
                ft.ElevatedButton(
                    content=ft.Row(
                        controls = [
                        ft.Row(
                            controls=[
                                ft.Icon(ft.icons.SHOPPING_CART, size=25, color=ft.colors.BLACK ), #icone
                                ft.Text(
                                    "Carrinho", #texto
                                    style=ft.TextStyle(size=15, weight=ft.FontWeight.BOLD)
                                ),
                            ],
                            spacing=10,
                            alignment=ft.MainAxisAlignment.CENTER,
                        )
                    ],
                        alignment=ft.MainAxisAlignment.CENTER,  
                    ),
                    style=ft.ButtonStyle(
                        bgcolor=ft.colors.YELLOW_900,
                        color=ft.colors.BLACK,
                        padding=20,
                        shape=ft.RoundedRectangleBorder(radius=12),
                    ),
                    width=130, #altura e largura do botão
                    height=50,
                    on_click=lambda e, id=id: adccarrinho(page, id),
                ), #fim do botão do carrinho ----------------------------------
                    ],
                    ),
                    ft.Row(
                    alignment=ft.MainAxisAlignment.CENTER,
                    controls=[
                        ft.ElevatedButton(
                            text="Voltar aos produtos",
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.YELLOW_800,
                                color=ft.colors.BLACK,
                                padding=20,
                                shape=ft.RoundedRectangleBorder(radius=12),
                                text_style=ft.TextStyle(size=15, weight=ft.FontWeight.BOLD),
                            ),
                            width=200,
                            height=50,
                            on_click=lambda e: callback_produtos()
                        ),
                        ft.ElevatedButton(
                            text="Comprar",
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.BLUE_800,
                                color=ft.colors.BLACK,
                                padding=20,
                                shape=ft.RoundedRectangleBorder(radius=12),
                                text_style=ft.TextStyle(size=20, weight=ft.FontWeight.BOLD),
                            ),
                            width=220,
                            height=55,
                        )
                    ],
                ),
            ], #fim do controls do cartao
            spacing=12,
            alignment=ft.MainAxisAlignment.CENTER,
        ),
    )

    page.add(ft.Container(content=cartao, alignment=ft.alignment.center))
    page.update()

def produtos(page, puxar_login):
    page.clean()
    page.fonts = {"fonte": 'fonte.ttf', "sobrefonte": 'sobrefonte.ttf'}
    parametro = conectaproduto()
    vetor = []

    # Aqui é a área que vai colocar cada produto no painel
    for produto in parametro:
        id, nome, img, preco, descricao = produto
        desc = ft.Container(
            content=ft.Row(
                [
                    ft.Image(
                            src=img,
                            fit=ft.ImageFit.CONTAIN,
                            width=200,
                            height=200,
                            border_radius=10,
                        ),
                        ft.Column(controls=[
                    ft.Text(nome, color=ft.colors.BLACK, weight=ft.FontWeight.BOLD, size=20, font_family="sobrefonte.ttf", width=170),
                    ft.Text(value="R$ "+str(preco)+",00", color=ft.colors.BLACK, weight=ft.FontWeight.BOLD, size=50, font_family="sobrefonte.ttf"),
                    ft.Container(
                            content=ft.ElevatedButton(
                            text='Comprar',
                            style=ft.ButtonStyle(
                                bgcolor=ft.colors.BROWN_400,
                                color=ft.colors.BLACK,
                                padding=17,
                                shape=ft.RoundedRectangleBorder(radius=12),
                                overlay_color=ft.colors.BROWN_700,  # cor ao clicar
                                text_style = ft.TextStyle(size=20,weight=ft.FontWeight.BOLD, font_family='sobrenome'),
                            ), 
                            on_click=lambda e, id=id: descprodutos(page, id, lambda: produtos(page, puxar_login)),
                        ),
                        alignment=ft.alignment.center,
                        )
                    
                    ]
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER,
                vertical_alignment=ft.CrossAxisAlignment.CENTER,
            ),
        width=510,
        height=250,
        bgcolor=ft.colors.YELLOW,
        border_radius=10,
        border=ft.border.all(2, ft.colors.BLACK),
        padding=20,
        alignment=ft.alignment.center,
        shadow=ft.BoxShadow(blur_radius=8, color=ft.colors.GREY),
        )
        # centralizar logotipo
        centralizardesc = ft.Container(content=desc, alignment=ft.alignment.center)

        vetor.append(centralizardesc)
    #titulo
    texttitulo = ft.Container(
    ft.Text(
        value='Produtos Disponíveis!',
        size=36,
        weight=ft.FontWeight.BOLD,
        color=ft.colors.BLACK,
        text_align=ft.TextAlign.CENTER,
    ),

    bgcolor=ft.colors.YELLOW,
    border_radius=10,
    padding=20,
    width=450,
    alignment=ft.alignment.center,
    # vertical_alignment=ft.CrossAxisAlignment.CENTER,
    border=ft.border.all(2, ft.colors.BLACK),
    shadow=ft.BoxShadow(
        spread_radius=2,
        blur_radius=8,
        color=ft.colors.BLACK,
        offset=ft.Offset(4, 4),
    )
)
    # Centralizar titulo
    centertitulo = ft.Container(
    content=texttitulo, alignment=ft.alignment.center, padding=10)
    # Centralizar descrição
    centerdescricao = ft.Container(content=desc, alignment=ft.alignment.center, padding=10)

    #logotipo
    logotipo = ft.Image(
        src='img/logotipo.png',
        fit=ft.ImageFit.CONTAIN
    )
    # centralizar logotipo
    centralizarLogotipo = ft.Container(content=logotipo, alignment=ft.alignment.center)
    # BOTÃO PARA VOLTAR
    botaovoltar = ft.Container(
        content=ft.ElevatedButton(
        text='VOLTAR AO LOGIN',
        style=ft.ButtonStyle(
            bgcolor=ft.colors.BLUE_400,
            color=ft.colors.BLACK,
            padding=15,
            shape=ft.RoundedRectangleBorder(radius=12),
            overlay_color=ft.colors.BLUE_600,  # cor ao clicar
            text_style = ft.TextStyle(size=15, weight=ft.FontWeight.BOLD, font_family='sobrefonte'),
        ),
        on_click=lambda e: puxar_login(),
    ),
    alignment=ft.alignment.center,
    )
    # BOTAO DO CARRINHO
    botaocarrinho = ft.Container(
        content=ft.ElevatedButton(
        text='ACESSAR CARRINHO',
        style=ft.ButtonStyle(
            bgcolor=ft.colors.ORANGE_400,
            color=ft.colors.BLACK,
            padding=15,
            shape=ft.RoundedRectangleBorder(radius=12),
            overlay_color=ft.colors.ORANGE_600,  # cor ao clicar
            text_style = ft.TextStyle(size=15, weight=ft.FontWeight.BOLD, font_family='sobrefonte'),
        ),
        on_click=lambda e, id=id: acessarcarrinho(page, lambda: produtos(page, puxar_login))
    ),
    alignment=ft.alignment.center,
    )
    doisbotoes = ft.Row(
    controls=[
        botaovoltar,
        botaocarrinho,
    ],
    alignment=ft.MainAxisAlignment.CENTER,  # alinha horizontalmente ao centro
    spacing=20  
    )
    compras = ft.Container(
        content= ft.Column(
            controls= [
                centertitulo,
                centralizarLogotipo,
                doisbotoes,
                *vetor,
            ]
        ),
        )
    lista_de_produtos = ft.ListView(
        controls=[ft.Column(
            controls=[compras]
        )],
        expand=True,
        auto_scroll=False,
    )
    page.add(ft.Stack(
        controls = [ft.Image('assets/img/fundoprodutos.jpg'),
         ft.Container(ft.Column(
             [
                lista_de_produtos,
             ],
             alignment=ft.MainAxisAlignment.CENTER
         )
        )
        ], expand=True
    )
    )
    page.update()