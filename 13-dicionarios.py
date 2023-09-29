meuDicionario = {"nome": "José", "idade": 25}
nome = meuDicionario["nome"]
idade = meuDicionario.get("idade")
print(meuDicionario)
meuDicionario["idade"] = 26
meuDicionario["cidade"] = "São Paulo"
print(meuDicionario)

del meuDicionario["idade"]
print(meuDicionario)
valorRemovido = meuDicionario.pop("nome")
print(valorRemovido)
print(meuDicionario)

# meuDicionario = {"nome": "José", "idade": 25}
# for i in meuDicionario:
#     print(i, meuDicionario[i])

# listaDeChaves = list(meuDicionario.keys())
# print(listaDeChaves)

# listaDeValores = list(meuDicionario.values())
# print(listaDeValores)
