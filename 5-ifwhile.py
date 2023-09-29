idade = 15
if idade >= 18:
    print("Você é maior de idade!")
else:
    print("Você é menor de idade.")

# repetição
contador = 0
while contador < 5:
    print(f"Contador: {contador}")
    contador += 1 # contador++ não funciona
    if contador == 2:
        break # Sai do loop
