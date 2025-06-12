import flet as ft
import sqlite3


def bdconfig():
    conexao = sqlite3.connect('assets/barbershop.db',check_same_thread=False)
    con = conexao.cursor()
    con.execute('select * from usuario')
    usuario = con.fetchall()
    return (usuario)