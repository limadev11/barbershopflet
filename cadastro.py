import flet as ft
import sqlite3
import bdconfig # Certifique-se de que este módulo existe e está configurado corretamente
import os

def cadastro(page, callback_login):
    page.clean()

    def exibir_mensagem(mensagem, bgcolor=ft.colors.GREEN):
        page.snack_bar = ft.SnackBar(
            content=ft.Text(mensagem),
            bgcolor=bgcolor,
            action=ft.TextButton("Fechar", on_click=lambda e: page.snack_bar.close())
        )
        page.snack_bar.open = True
        page.update()

    def gravar(e):
        nome = nome_input.value.strip()
        sobrenome = sobrenome_input.value.strip()
        email = email_input.value.strip()
        telefone = telefone_input.value.strip()
        senha = senha_input.value.strip()
        senha_confirm = senhaconfirm_input.value.strip()

        # Validação dos campos obrigatórios
        if not all([nome, sobrenome, email, telefone, senha, senha_confirm]):
            exibir_mensagem("Por favor, preencha todos os campos.", ft.colors.RED)
            print("Erro: campos obrigatórios não preenchidos.")
            return

        if senha != senha_confirm:
            exibir_mensagem("As senhas não coincidem.", ft.colors.RED)
            print("Erro: senhas diferentes.")
            return

        # Caminho absoluto para garantir que o banco certo seja usado
        db_path = os.path.join(os.path.dirname(__file__), 'assets/barbershop.db')

        conexao = None
        try:
            conexao = sqlite3.connect(db_path, check_same_thread=False)
            cursor = conexao.cursor()

            print("Tentando inserir no banco os valores:")
            print("Nome:", nome)
            print("Sobrenome:", sobrenome)
            print("Email:", email)
            print("Telefone:", telefone)
            print("Senha:", senha)

            cursor.execute('''
                INSERT INTO usuario (nome, sobrenome, email, telefone, senha)
                VALUES (?, ?, ?, ?, ?)
            ''', (nome, sobrenome, email, telefone, senha))
            conexao.commit()

            exibir_mensagem("Cadastro realizado com sucesso!", ft.colors.GREEN)
            print("Cadastro realizado com sucesso.")
            callback_login()

        except sqlite3.IntegrityError:
            exibir_mensagem("Este e-mail já está cadastrado.", ft.colors.RED)
            print("Erro: e-mail já cadastrado.")
        except Exception as e:
            print("Erro ao cadastrar:", str(e))
            exibir_mensagem(f"Erro ao cadastrar: {str(e)}", ft.colors.RED)
        finally:
            if conexao:
                conexao.close()

    # Imagem do logo
    img = ft.Container(
        content=ft.Image(
            src='assets/img/logo1.png',
            width=200,
            height=200,
            fit=ft.ImageFit.CONTAIN,
        ),
        alignment=ft.alignment.center,
        padding=20
    )

    # Campos de entrada
    campos_style = {
        "width": 300,
        "height": 50,
        "text_style": ft.TextStyle(color=ft.colors.BLACK),
        "bgcolor": ft.colors.WHITE,
        "border_radius": 8
    }

    nome_input = ft.TextField(label="Digite seu nome", prefix_icon=ft.icons.PERSON, **campos_style)
    sobrenome_input = ft.TextField(label="Digite seu sobrenome", prefix_icon=ft.icons.PERSON, **campos_style)
    email_input = ft.TextField(label="Digite seu E-mail", prefix_icon=ft.icons.EMAIL, **campos_style)
    telefone_input = ft.TextField(label="Digite seu telefone", prefix_icon=ft.icons.PHONE, **campos_style)
    senha_input = ft.TextField(
        label='Digite sua senha',
        prefix_icon=ft.icons.LOCK,
        password=True,
        can_reveal_password=True,
        **campos_style
    )
    senhaconfirm_input = ft.TextField(
        label='Confirme sua senha',
        prefix_icon=ft.icons.LOCK,
        password=True,
        can_reveal_password=True,
        **campos_style
    )

    # Botões
    botao_style = {
        "width": 200,
        "height": 50,
        "bgcolor": ft.colors.BLACK,
        "color": ft.colors.WHITE
    }

    botaoexecutar = ft.ElevatedButton(
        text='Efetuar Cadastro',
        on_click=gravar,
        **botao_style
    )

    botaovoltar = ft.ElevatedButton(
        text='Voltar',
        icon=ft.icons.ARROW_BACK,
        on_click=callback_login,
        **botao_style
    )

    # Layout principal
    page.add(
        ft.Column(
            controls=[
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
            scroll=ft.ScrollMode.AUTO,
            expand=True
        )
    )
