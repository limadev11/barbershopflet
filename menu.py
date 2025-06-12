# import flet as ft
# import sqlite3

# # Função para buscar serviços no banco de dados
# def conectaservicos():
#     conn = sqlite3.connect('assets/barbershop.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM servicos')
#     dados = cursor.fetchall()
#     return dados

# def conectaprofissionais():
#     conn = sqlite3.connect('assets/barbershop.db')
#     cursor = conn.cursor()
#     cursor.execute('SELECT * FROM profissionais')
#     profissionais = cursor.fetchall()
#     conn.close()
#     return [
#         {
#             "id": p[0],
#             "nome": p[1],
#             "especialidade": p[2],
#             "descricao": p[3],
#             "disponivel": p[4],
#         } for p in profissionais
#     ]

# def confirmar_agendamento(e, page):
#         page.dialog = ft.AlertDialog(
#             title=ft.Text("Agendamento confirmado!"),
#             content=ft.Text("Seu agendamento foi enviado com sucesso.")
#         )
#         page.dialog.open = True
#         page.update()

# # Função principal
# def exibemenu(page: ft.Page):
#     page.clean()
#     page.title = "BarberShop"

#     # Função para confirmar agendamento

#     # Header
#     header = ft.Container(
#         padding=10,
#         content=ft.Row(
#             controls=[
#                 ft.Image(src="assets/img/favicon.jfif", width=80, height=80, border_radius=80),
#                 ft.Column([
#                     ft.Text("Nova Cena", color="white", size=20),
#                     ft.Row([
#                         ft.Icon(name=ft.icons.STAR, color=ft.colors.AMBER_400, size=20),
#                         ft.Text("5.0", color="white")
#                     ])
#                 ]),
#                 ft.Container(expand=True),
#                 ft.IconButton(ft.icons.FAVORITE_BORDER, icon_color="white"),
#                 # ft.ElevatedButton("Agendar", bgcolor=ft.colors.AMBER, color="white", on_click=confirmar_agendamento),
#                 ft.IconButton(ft.icons.MORE_VERT, icon_color="white"),
#             ],
#             alignment=ft.MainAxisAlignment.SPACE_BETWEEN
#         )
#     )

#         # Conteúdo das abas
#     conteudo_abas = ft.Column()

#     # Chamada correta para carregar os serviços
#     servicos_info = conectaservicos()

#     # Renderiza visualmente os serviços
#     for s in servicos_info:
#         print(servicos_info)
#         id, nome, descricao, preco, duracao_minutos = servicos_info
        
#         servicos = ft.Column([
#         ft.ListTile(
#             title=ft.Text(nome, size=18, color="white"),
#             subtitle=ft.Column([
#                 ft.Text(f"Descrição: {descricao}", bgcolor="white", color="black"),
#                 ft.Text(f"Duração: {duracao_minutos} min", bgcolor="white", color="black"),
#                 ft.Text(f"Preço: R$ {preco:.2f}", bgcolor="white", color="black"),
#             ], spacing=2),
#             leading=ft.Icon(ft.icons.CONTENT_CUT, color="white")
#         ) for s in servicos_info
#     ])

#     # Exibir na aba inicialmente
#     conteudo_abas.controls = [servicos]


#     # --- PRODUTOS ---
#     produtos = ft.Column([
#         ft.ListTile(
#             title=ft.Text("Produto Exemplo", size=18, color="white"),
#             leading=ft.Image(src="assets/img/produto_exemplo.jpg", width=100, height=100, fit=ft.ImageFit.COVER),
#             subtitle=ft.Column([
#                 ft.Text("Descrição do produto", bgcolor="white", color="black"),
#                 ft.Text("Preço: R$ 29.90", bgcolor="white", color="black"),
#             ]),
#             trailing=ft.ElevatedButton("Comprar", bgcolor="amber", color="white", on_click=lambda e: None)
#         )
#     ])

#     # --- PROFISSIONAIS ---
 

#     # Função que muda o conteúdo da aba
#     def mudar_conteudo(e):
#         if tabs.selected_index == 0:
#             conteudo_abas.controls = [servicos]
#         elif tabs.selected_index == 1:
#             conteudo_abas.controls = [lista_profissionais]
#         elif tabs.selected_index == 2:
#             conteudo_abas.controls = [produtos]
#         page.update()

#     # Tabs
#     tabs = ft.Tabs(
#         selected_index=0,
#         animation_duration=300,
#         label_color="white",
#         indicator_color="#FF9800",
#         tabs=[
#             ft.Tab(text="Serviços"),
#             ft.Tab(text="Profissionais"),
#             ft.Tab(text="Produtos"),
#         ],
#         divider_color="grey",
#         on_change=mudar_conteudo
#     )

#     # Comodidades
#     titulo_comodidades = ft.Container(
#         padding=ft.padding.only(left=10),
#         content=ft.Text("Comodidades", color="white", size=16, weight="bold")
#     )

#     facilidades = ft.Container(
#         padding=10,
#         content=ft.Row(
#             [
#                 ft.Icon(ft.icons.WIFI, color="grey"),
#                 ft.Icon(ft.icons.LOCAL_PARKING, color="grey"),
#                 ft.Icon(ft.icons.ACCESSIBLE, color="grey"),
#                 ft.Icon(ft.icons.CLOUD_OFF, color="grey"),
#             ],
#             alignment=ft.MainAxisAlignment.SPACE_EVENLY,
#         )
#     )

#     # Barra de navegação inferior
#     nav_bar = ft.NavigationBar(
#         selected_index=0,
#         bgcolor=ft.colors.BLACK,
#         destinations=[
#             ft.NavigationBarDestination(icon=ft.icons.HOME, label="Início"),
#             ft.NavigationBarDestination(icon=ft.icons.PERSON, label="Menu"),
#         ]
#     )

#     # Conteúdo inicial
#     conteudo_abas.controls = [servicos]

#     # Adiciona tudo na página
#     page.add(
#         ft.Stack([
#             ft.Image('assets/img/fundo.jpg', fit=ft.ImageFit.COVER, opacity=0.2),
#             ft.Container(
#                 content=ft.Column([
#                     header,
#                     tabs,
#                     conteudo_abas,
#                     titulo_comodidades,
#                     facilidades,
#                     ft.Container(height=100, bgcolor=ft.colors.BLACK, padding=10),
#                     nav_bar
#                 ])
#             )
#         ])
#     )
