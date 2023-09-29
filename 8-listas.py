minhaLista = [3, 4, 2, 1, 5]
primeiroElemento = minhaLista[0]
ultimoElemento = minhaLista[len(minhaLista)-1]
print(f"{primeiroElemento}, {ultimoElemento}")

minhaLista.append(6)

minhaLista.insert(2, 2000)
print(minhaLista[2])

del minhaLista[2]
print(f"{minhaLista[2]}")

elementoRemovido = minhaLista.pop()
print(elementoRemovido)

# print(minhaLista[5])

tamanhoDaLista = len(minhaLista)
print(tamanhoDaLista)

for elemento in minhaLista:
    print(elemento)

# minhaLista.sort()
# for elemento in minhaLista:
#     print(elemento)

frase = "eu adoro o pet computação"
parcionar = frase.split()
for partes in parcionar:
    print(partes)

outraFrase = "no-mês-de-janeiro-tem-ano-novo"
parcionar = outraFrase.split("-")
for partes in parcionar:
    print(partes)

