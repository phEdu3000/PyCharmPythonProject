import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # coloca sua senha se tiver
    database="Universidade"
)

cursor = conexao.cursor()