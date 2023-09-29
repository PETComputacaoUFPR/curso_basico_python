# Primeiro - Esquisitisse do python:
textoComAspasSimples = 'Isso é uma string.'
textoComAspasDuplas = "Isso também é uma string."

# Coisas legais:
comeco = "Olá, "
final = "mundo!"
mensagemFinal = comeco + final
print(f"{mensagemFinal}")

# Funciona como um vetor também
texto = "Pet Computacao" #14 letras
caracter = texto[0]
print(f"{caracter}", end = '') #esse "end" muda o que acontece no final da linha
caracter = texto[1]
print(f"{caracter}", end = '')
caracter = texto[2]
print(f"{caracter}")

# Para saber a quantidade de caracteres numa string
comprimento = len(texto) #14
print(f"O tamanho do texto é de: {comprimento}")

# Métodos de string 
alto = "QUE DIA LINDO!"
alto = alto.lower()
print(f"{alto}")

baixo = "que dia triste :("
baixo = baixo.upper()
print(f"{baixo}")

texto = "      ...Curso Básico de Python...        "
print(f"{texto.strip()}") # o que você coloca dentro de strip()
# é removido no começo e final da linha

texto = "fazemos, parte, do, pet, computação"
listaTexto = texto.split() #o que está dentro split() é o separador da lista
i = 0
while i < 5:
    print(f"{listaTexto[i]}")
    i += 1

# algo muito legal: idenxação negativa
texto = "Pet"
print(f"{texto[-1]}") # pega a partir do final da string

# função boba title()
texto = "bom dia pessoal!"
print(f"{texto.title()}")

# funcões úteis d+ count() // replace()
texto = "hoje nos temos sorte que esta um lindo dia"
contagem = texto.count('o')
print(f"Numero de 'o':{contagem}")

texto = texto.replace("sorte", "azar")
texto = texto.replace("lindo", "pessimo")
print(f"{texto}")

#Extraindo informações algébricas de strings
operacao = "7 + 9 + 11"
resultado = eval(operacao)
print(resultado)

# a = 2
# operacao = "7 + 9 + 11 + a"
# resultado = eval(operacao)
# print(resultado)