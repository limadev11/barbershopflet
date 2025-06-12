import flet as ft

BARBEARIAS_GV = [
    {"name": "Nova Cena", "vicinity": "Rua Marechal Floriano , 2442 - Em frente ao 6º batalhão - 35030-330 Lourdes", "img": "img/barber.jfif"},
]

def exibemenu(page: ft.Page, voltar_callback):
    page.clean()
    page.title = "BarberShop"

    # ---------- FUNÇÃO DE AGENDAMENTOS ----------
    def agendamentos_pagina(e):
        page.clean()
        page.title = "Agendamentos"

        agendamentos_feitos = [
            {"profissional": "Nova Cena", "data": "10/05/2025", "horario": "14:00"},
            {"profissional": "Nova Cena", "data": "12/05/2025", "horario": "16:00"},
        ]

        lista_agendamentos = ft.Column(
            controls=[
                ft.ListTile(
                    title=ft.Text(f"{ag['data']} às {ag['horario']}"),
                    subtitle=ft.Text(f"Profissional: {ag['profissional']}"),
                    leading=ft.Icon(ft.icons.CALENDAR_MONTH),
                )
                for ag in agendamentos_feitos
            ]
        )

        profissional_dropdown = ft.Dropdown(
            label="Escolha o profissional",
            width=350,
            options=[ft.dropdown.Option(b["name"]) for b in BARBEARIAS_GV],
            border_radius=8,
        )

        data_input = ft.TextField(
            label="Data do Agendamento",
            hint_text="DD/MM/AAAA",
            width=350,
            prefix_icon=ft.icons.CALENDAR_MONTH,
            border_radius=8,
        )

        horario_dropdown = ft.Dropdown(
            label="Horário",
            width=350,
            options=[ft.dropdown.Option(h) for h in ["08:00", "09:00", "10:00", "11:00", "14:00", "15:00", "16:00", "17:00"]],
            border_radius=8,
        )

        status_text = ft.Text(value="", color=ft.colors.RED_400)

        def confirmar_agendamento(prof, data, hora, status_text):
            if not prof or not data or not hora:
                status_text.value = "Preencha todos os campos!"
                status_text.color = "red"
            else:
                status_text.value = f"Agendamento confirmado para {data} às {hora} com {prof}."
                status_text.color = "green"
            page.update()

        agendar_btn = ft.ElevatedButton(
            text="Confirmar Agendamento",
            width=350,
            on_click=lambda e: confirmar_agendamento(
                profissional_dropdown.value,
                data_input.value,
                horario_dropdown.value,
                status_text
            ),
            style=ft.ButtonStyle(shape=ft.RoundedRectangleBorder(radius=8)),
        )

        page.add(
            ft.Column(
                controls=[
                    ft.TextButton("← Voltar", on_click=lambda _: exibemenu(page, voltar_callback)),
                    ft.Text("Seus Agendamentos", size=18, weight="bold"),
                    lista_agendamentos,
                    ft.Divider(height=30),
                    ft.Text("Agendar Horário", size=24, weight="bold", text_align="center"),
                    profissional_dropdown,
                    data_input,
                    horario_dropdown,
                    agendar_btn,
                    status_text,
                ],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                spacing=20,
                scroll=ft.ScrollMode.AUTO
            )
        )


    # ---------- HEADER ----------
    header = ft.Container(
        padding=10,
        content=ft.Row(
            controls=[
                ft.Image(src="assets/img/favicon.jfif", width=80, height=80,border_radius=80),
                ft.Column([
                    ft.Text("Nova Cena", color=ft.colors.ON_SURFACE, size=20, weight="bold"),
                    ft.Row([
                        ft.Icon(name=ft.Icons.STAR, color=ft.colors.AMBER_400, size=20),
                        ft.Text("5.0", color=ft.colors.ON_SURFACE)
                    ])
                ]),
                ft.Container(expand=True),
                ft.IconButton(ft.Icons.FAVORITE_BORDER, icon_color=ft.colors.ON_SURFACE),
                ft.ElevatedButton("Agendar", bgcolor=ft.colors.AMBER, color=ft.colors.ON_PRIMARY, on_click=agendamentos_pagina),
                ft.IconButton(ft.Icons.MORE_VERT, icon_color=ft.colors.ON_SURFACE),
            ],
            alignment=ft.MainAxisAlignment.SPACE_BETWEEN
        )
    )


    # ---------- ABAS ----------
    tabs = ft.Tabs(
        selected_index=0,
        animation_duration=300,
        label_color="white",
        indicator_color="#FF9800",
        tabs=[
            ft.Tab(text="Serviços"),
            ft.Tab(text="Profissionais"),
            ft.Tab(text="Fidelidade"),
            ft.Tab(text="Produtos"),
        ],
        divider_color="grey"
    )
    
    # ----------  COMODIDADES ----------
    titulo_comodidades = ft.Container(
        padding=ft.padding.only(left=10),
        content=ft.Text("Comodidades", color="white", size=16, weight="bold")
    )
    
    # ----------  FACILIDADES ----------
    
    facilidades = ft.Container(
        padding=10,
        content=ft.Row(
            [
                ft.Icon(ft.Icons.WIFI, color="grey"),
                ft.Icon(ft.Icons.LOCAL_PARKING, color="grey"),
                ft.Icon(ft.Icons.ACCESSIBLE, color="grey"),
                ft.Icon(ft.Icons.CLOUD_OFF, color="grey"),
            ],
            alignment=ft.MainAxisAlignment.SPACE_EVENLY,
        )
    )
    
    # ----------  PESQUISAR ----------
    
    search = ft.Container(
    padding=10,
    content=ft.TextField(
        hint_text="Pesquisar",
        prefix_icon=ft.Icons.SEARCH,
        filled=True,
        fill_color=ft.colors.SURFACE_VARIANT,
        border_radius=10,
        text_style=ft.TextStyle(color=ft.colors.ON_SURFACE),
        hint_style=ft.TextStyle(color=ft.colors.ON_SURFACE_VARIANT),
    )
)
    
    # ----------  SERVIÇOS ----------
    titulo_servicos = ft.Container(
        padding=ft.padding.only(left=10),
        content=ft.Text("Serviços", color="white", size=16, weight="bold")
    )
    
    
    # ----------  LISTA DE SERVIÇOS ----------
    servicos = ft.Column([
        ft.ListTile(
        leading=ft.Icon(ft.Icons.CONTENT_CUT, color=ft.colors.ON_SURFACE),
        title=ft.Text("Barba", color=ft.colors.ON_SURFACE),
        subtitle=ft.Text("R$ 25,00", color=ft.colors.ON_SURFACE_VARIANT),
        ),
            ft.ListTile(
    leading=ft.Icon(ft.Icons.CONTENT_CUT, color=ft.colors.ON_SURFACE),
    title=ft.Text("Corte", color=ft.colors.ON_SURFACE),
    subtitle=ft.Text("R$ 35,00", color=ft.colors.ON_SURFACE_VARIANT),
    ),
        ft.ListTile(
    leading=ft.Icon(ft.Icons.CONTENT_CUT, color=ft.colors.ON_SURFACE),
    title=ft.Text("Hidratação", color=ft.colors.ON_SURFACE),
    subtitle=ft.Text("R$ 45,00", color=ft.colors.ON_SURFACE_VARIANT),
    ),

    ])
    


    # ---------- BARRA DE NAVEGAÇÃO ----------
    destinos = ["inicio", "servicos", "profissionais", "fidelidade", "produtos"]

    def atualizar_conteudo(e):
        destino = destinos[e.control.selected_index]
        if destino == "inicio":
            exibemenu(page, voltar_callback)
        elif destino == "servicos":
            page.clean()
            page.title = "Serviços"
            page.add(
                ft.Column(
                    controls=[
                        header,
                        tabs,
                        titulo_comodidades,
                        facilidades,
                        search,
                        titulo_servicos,
                        servicos,
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )
        elif destino == "profissionais":
            page.clean()
            page.title = "Profissionais"
            page.add(
                ft.Column(
                    controls=[
                        header,
                        tabs,
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )
        elif destino == "fidelidade":
            page.clean()
            page.title = "Fidelidade"
            page.add(
                ft.Column(
                    controls=[
                        header,
                        tabs,
                        titulo_comodidades,
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )
        elif destino == "produtos":
            page.clean()
            page.title = "Produtos"
            page.add(
                ft.Column(
                    controls=[
                        header,
                        tabs,
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )
        elif destino == "inicio":
            page.clean()
            page.title = "Início"
            page.add(
                ft.Column(
                    controls=[
                        header,
                        tabs,
                        titulo_comodidades,
                        facilidades,
                        search,
                        titulo_servicos,
                        servicos,
                    ],
                    expand=True,
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN
                )
            )

    nav_bar = ft.NavigationBar(
        selected_index=0,
        bgcolor=ft.Colors.BLACK,
        destinations=[
            ft.NavigationBarDestination(icon=ft.icons.HOME, label="Início"),
            ft.NavigationBarDestination(icon=ft.icons.PERSON, label="Menu"),
        ],
        on_change=atualizar_conteudo
    )

    # ---------- EXIBIR COMPONENTES ----------
    page.add(
    ft.Stack(
        [
            ft.Image('img/fundo.jpg', fit=ft.ImageFit.COVER, opacity=0.2),
            ft.Container(
                content=ft.Column(
                    controls=[
                        header,
                        tabs,
                        titulo_comodidades,
                        facilidades,
                        search,
                        titulo_servicos,
                        servicos,
                        ft.Container(height=50),
                        nav_bar
                    ],
                    alignment=ft.MainAxisAlignment.SPACE_BETWEEN,
                    expand=True
                )
            )
        ]
    )
)

