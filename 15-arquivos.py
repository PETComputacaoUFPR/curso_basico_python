with open("arquivoTeste.txt", "r") as arquivo:
    print(arquivo.read())

with open("arquivoTeste.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha)

with open("arquivoTeste.txt", "r") as arquivo:
    linhas = arquivo.readlines()
    print(linhas)

with open("arquivoTeste2.txt", "w") as arquivo:
    arquivo.write("Testando gravação de arquivos em Python")

with open("arquivoTeste2.txt", "r") as arquivo:
    print(arquivo.read())

with open("arquivoTeste2.txt", "a") as arquivo:
    arquivo.write(" - Acrescentando conteúdo")

with open("arquivoTeste2.txt", "r") as arquivo:
    print(arquivo.read())