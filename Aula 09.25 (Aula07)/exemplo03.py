soma = 0
qtd = int(input("Digite a quantidade de idades: "))
for i in range(1,qtd+1):
    n = int(input(f" Entre com a {i}a. idade: "))
    soma = soma + n
média = soma / qtd
print(f"A média das idade é {média:5.2f}")