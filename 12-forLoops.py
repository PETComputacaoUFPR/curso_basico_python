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