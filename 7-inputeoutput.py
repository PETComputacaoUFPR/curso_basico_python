# valorDigitado = input("Mensagem para o usuário: ")
# print(valorDigitado)
# a função input sempre retorna uma string
# não importa o que o usuário digite, seja número, etc

# então você deve formatar o que está entrando
# numero = int(input("Digite um número: "))
# print(numero)

#jeito melhor de fazer:
# numero = input("Digite um número: ")
# if numero.isdigit():
#     print(numero)
# else:
#     print("Número inválido")

# a função format()
# texto = "Eu tenho {} anos, e  meu nome é {}"
# nome = input("Digite seu nome: ")
# idade = input("Digite sua idade: ")
# texto = texto.format(idade, nome)
# print(texto)

# texto = "No dia {0} eu fico feliz, pois no dia {0} é meu aniverśario de {1} anos"
# texto = texto.format(11, 20)
# print(texto)