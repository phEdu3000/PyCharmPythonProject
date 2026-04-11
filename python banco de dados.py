import mysql.connector

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",  # coloca sua senha se tiver
    database="Universidade"
)

cursor = conexao.cursor()

cursor.execute("select * from aluno")

dados=cursor.fetchall()

for linha in dados:
    print(linha)
