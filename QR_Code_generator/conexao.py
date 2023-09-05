import mysql.connector

def conectar():
    conexao = mysql.connector.connect(
        host="localhost",  # Host do servidor MySQL
        user="root",  # Seu nome de usuário do MySQL (geralmente 'root')
        password="",  # Sua senha do MySQL (neste caso, vazia)
        database="QrCodeDB"  # Nome do banco de dados que você criou
    )
    return conexao
