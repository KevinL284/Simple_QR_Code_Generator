import qrcode
from PIL import Image
import conexao

# Em um terminal dentro da sua pasta digite os seguintes comandos: 
# pip install mysql-connector-python
# pip install qrcode --user
# pip install Pillow



# Função para criar o QR code e salvar as informações no banco de dados
def criar_qr_code_e_salvar(dados, nome_arquivo, conexao_bd):
    # Criar o QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(dados)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(nome_arquivo)

    # Salvar as informações no banco de dados
    cursor = conexao_bd.cursor()
    cursor.execute("INSERT INTO qr_codes (dados, nome_arquivo) VALUES (%s, %s)", (dados, nome_arquivo))
    conexao_bd.commit()
    cursor.close()

# Conectar ao servidor MySQL usando o módulo de conexão
conexao_bd = conexao.conectar()

# Solicitar ao usuário que insira os dados para o QR code
dados = input("Digite o texto ou link que deseja transformar em um QR code: ")
nome_arquivo = input("Digite o nome do arquivo de saída (com extensão .png): ")

# Chamar a função para criar o QR code e salvar as informações
criar_qr_code_e_salvar(dados, nome_arquivo, conexao_bd)

print(f"QR code gerado e informações salvas no banco de dados com sucesso em {nome_arquivo}")

# Fechar a conexão com o banco de dados
conexao_bd.close()