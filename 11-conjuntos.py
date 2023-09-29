meuConjunto = {1, 2, 3, 4, 5}
outroConjunto = set([4, 5, 6, 7, 8])
print(meuConjunto)
print(outroConjunto)

meuConjunto.add(3)
print(meuConjunto)
meuConjunto.add(6)
print(meuConjunto)

meuConjunto.remove(3)
print(meuConjunto)

conjuntoDesordenado = {3, 2, 1, 4, 5}
print(conjuntoDesordenado) # sempre imprime ordenado

# meuConjunto.remove(10) # dá erro se não existir
# meuConjunto.discard(10) # não dá erro se não existir

uniao = meuConjunto | outroConjunto
print(uniao)

interseccao = meuConjunto & outroConjunto
print(interseccao)

diferenca = meuConjunto - outroConjunto
print(diferenca)

diferencaSimetrica = meuConjunto ^ outroConjunto
print(diferencaSimetrica)

conjuntoImutavel = frozenset([1, 2, 3])
print(conjuntoImutavel)
# conjuntoImutavel.add(4) # dá erro