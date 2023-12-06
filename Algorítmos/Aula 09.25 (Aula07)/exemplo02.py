soma = 0
for i in range(1,11):
    n = int(input(f" Entre com a {i}a. idade: "))
    soma = soma + n
média = soma / 10
print(f"A média das idade é {média:5.2f}")