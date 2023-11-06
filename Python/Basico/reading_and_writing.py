from pathlib import Path

# Lendo um arquivo usando pathlib
caminho_arquivo_leitura = Path(__file__).parent / 'texto.txt'
try:
    with open(caminho_arquivo_leitura,"r", encoding='utf-8') as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("O arquivo não foi encontrado.")

# Escrevendo em um arquivo usando pathlib
caminho_arquivo_escrita = caminho_arquivo_leitura
conteudo_novo_arquivo = "Conteúdo para escrever no novo arquivo."
with caminho_arquivo_escrita.open("w") as arquivo:
    arquivo.write(conteudo_novo_arquivo)
    print("Conteúdo foi escrito no novo arquivo.")