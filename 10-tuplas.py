# tuplas são listas imutáveis
minhaTupla = (1,2,3)
outraTupla = tuple([4,5,6])
print(minhaTupla)

elementoZero = minhaTupla[0]
print(elementoZero)

# minhaTupla[0] = 2000
tuplaConcatenada = minhaTupla + outraTupla
print(tuplaConcatenada)

# tuplas são muito usadas para retornar mais de um valor de uma função
def retornaMaisDeUmValor():
    return (1,2)

primeiro, segundo = retornaMaisDeUmValor()
print(f"{primeiro}, {segundo}")

quantidadeDeDois = tuplaConcatenada.count(2)
print(quantidadeDeDois)

indiceDoSeis = tuplaConcatenada.index(6)
print(indiceDoSeis)

# estratégia para adicionar elemmentos em uma tupla
tuplaNova = (*tuplaConcatenada, 7)
print(tuplaNova)