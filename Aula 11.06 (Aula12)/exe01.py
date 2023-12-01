def parImpar(x):
    if x % 2 == 0:
        valor = True
        return print(f"{valor}, o número é par")
    else:
        valor = False
        return print(f"{valor}, o número é impar")

numero = int(input("Digite o valor: "))
parImpar(numero)