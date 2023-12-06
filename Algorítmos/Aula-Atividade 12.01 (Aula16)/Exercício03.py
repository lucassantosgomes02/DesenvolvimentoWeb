def calcular_soma_multiplicacao(numero_str):
    soma = 0
    multiplicacao = 1
    for digito_str in numero_str:
        digito = int(digito_str)
        soma += digito
        multiplicacao *= digito
    return soma, multiplicacao
RA = input("Digite os dois últimos digitos do RA: ")
try:
    soma, multiplicacao = calcular_soma_multiplicacao(RA)
    print(f"Soma = {soma} e Multiplicação = {multiplicacao}")
except ValueError:
    print("Por favor, digite um número válido no formato string.")
