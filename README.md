# Gerador de QR Code com Python e MySQL

Este é um projeto simples que permite criar QR codes a partir de texto ou links e armazenar esses QR codes em um banco de dados MySQL. É uma aplicação em Python 3 que utiliza as bibliotecas `qrcode`, `Pillow` e `mysql-connector-python`.

## Pré-requisitos

Antes de começar, certifique-se de ter as seguintes bibliotecas Python instaladas:

- `qrcode`
- `Pillow`
- `mysql-connector-python`

Você pode instalá-las usando pip:


pip install qrcode
pip install Pillow
pip install mysql-connector-python

## Uso
1 - Clone este repositório para a sua máquina:
git clone https://github.com/seu-usuario/seu-projeto.git

2 - Execute o script gerar_qr_code.py e siga as instruções para inserir o texto ou link que você deseja transformar em um QR code e o nome do arquivo de saída.

3 - O QR code será gerado e salvo no diretório, e as informações também serão armazenadas no banco de dados.

4 - Para fechar a conexão com o banco de dados, o script fará isso automaticamente.

## Autor
Kevin Souza | kevin.lucas284sz@gmail.com

## Licença

Este projeto está licenciado sob os termos da Licença MIT - consulte o arquivo [LICENSE](https://github.com/MrKevin284/Simple_QR_Code_Generator/blob/main/) para obter mais detalhes.

---

© 2023 [MrKevin284](https://github.com/MrKevin284)
