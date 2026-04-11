import mysql.connector
import csv

conexao = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Universidade"
)

cursor = conexao.cursor()

cursor.execute("select * from aluno")

dados=cursor.fetchall()

for linha in dados:
    print(linha)
with open("alunos.csv","w", newline="", encoding="utf-8") as arquivo:
    writer = csv.writer(arquivo)

    colunas = [desc[0]] for desc in cursor.description]
    writer.writerow(colunas)
