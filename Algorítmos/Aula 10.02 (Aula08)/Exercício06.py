palavra = input("Digite uma palavra: ")
palavra = palavra.replace(" ", "").lower()
palavra_invertida = palavra[::-1]
if palavra == palavra_invertida:
    print("É um palíndromo!")
else:
    print("Não é um palíndromo.")
