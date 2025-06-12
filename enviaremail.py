import smtplib
import random
import string
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def tela_recuperar_senha(page: ft.Page, callback_voltar):
    email_input = ft.TextField(label="Digite seu email")
    aviso = ft.Text("", color=ft.colors.RED)

    def enviar_email(e):
        email_destinatario = email_input.value
        if not email_destinatario:
            aviso.value = "Digite um email!"
            page.update()
            return

        conn = sqlite3.connect("assets/barbershop.db")
        cursor = conn.cursor()
        cursor.execute("SELECT COUNT(*) FROM usuario WHERE email = ?", (email_destinatario,))
        existe = cursor.fetchone()[0]

        if existe == 0:
            aviso.value = "Email não cadastrado!"
            page.update()
            return

        # Gera senha aleatória
        nova_senha = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

        # Atualiza a senha no banco
        cursor.execute("UPDATE usuario SET senha = ? WHERE email = ?", (nova_senha, email_destinatario))
        conn.commit()

        # Lê os parâmetros do banco
        cursor.execute("SELECT valor FROM parametro ORDER BY id")
        params = [x[0] for x in cursor.fetchall()]
        conn.close()

        remetente, senha_email, assunto, corpo, smtp_server, porta = params
        porta = int(porta)

        try:
            msg = MIMEMultipart()
            msg["From"] = remetente
            msg["To"] = email_destinatario
            msg["Subject"] = assunto
            msg.attach(MIMEText(f"{corpo}\n\nSenha temporária: {nova_senha}", "plain"))

            with smtplib.SMTP(smtp_server, porta) as server:
                server.starttls()
                server.login(remetente, senha_email)
                server.sendmail(remetente, email_destinatario, msg.as_string())

            page.dialog = ft.AlertDialog(title=ft.Text("Email enviado com sucesso!"))
            page.dialog.open = True
        except Exception as ex:
            aviso.value = f"Erro ao enviar email: {ex}"

        page.update()

    page.clean()
    page.add(
        ft.Column(
            [
                ft.Text("Recuperar Senha", size=20, weight="bold"),
                email_input,
                aviso,
                ft.ElevatedButton("Enviar email", on_click=enviar_email),
                ft.TextButton("Voltar", on_click=callback_voltar),
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )
