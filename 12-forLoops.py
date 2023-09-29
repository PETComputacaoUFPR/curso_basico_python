nomes = ["João", "Maria", "José", "Pedro", "Ana", "Paulo", "Lucas", "Luana", "Luiza", "Luiz"]
for nome in nomes:
    print(nome)

for numero in range(1, 5):
    print(numero)

for caracter in "eu adoro o pet computação":
    print(caracter)

for indice, nome in enumerate(nomes):
    print(f"{indice}: {nome}")

matriz = [[1,2,3], [4,5,6], [7,8,9]]
for linha in matriz:
    for elemento in linha:
        print(elemento)

numeros = [1,2,3,4,5,6,7,8,9,10]
for numero in numeros:
    if numero == 6:
        continue
    if numero % 2 == 0:
        print(numero)
    if numero == 9:
        break

pessoa = {"nome": "Alice", "idade": 30, "cidade": "Nova York"}

for chave in pessoa:
    print(chave)  # Isso imprimirá as chaves

for valor in pessoa.values():
    print(valor)  # Isso imprimirá os valores

for chave, valor in pessoa.items():
    print(f"{chave}: {valor}")  # Isso imprimirá as chaves e valores

# for(int i = 0; i < numeroDeRotacoes; i++)
numeroDeRotacoes = 5  # Substitua pelo número desejado de rotações

for i in range(numeroDeRotacoes):
    # O código dentro deste bloco será executado o número de vezes especificado em numeroDeRotacoes
    print(f"Rotação {i + 1}")

# desempacotando tuplas com for
lista = []
tupla = (1, 2, 3)
for i in range (len(tupla)):
    lista.append(tupla[i])    

for i in range (len(lista)):
    print(lista[i])

numeros = [1, 2, 3, 4, 5]
quadrados = []
for numero in numeros:
    quadrados.append(numero ** 2)

print(quadrados) 

# numeros = [1, 2, 3, 4, 5]
# quadrados = [numero ** 2 for numero in numeros]

# print(quadrados)  