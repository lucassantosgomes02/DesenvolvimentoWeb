salario_atual = float(input("Qual o salario atual? "))
percentual_de_aumento = float(input("Qual o percentual de aumento? "))
novo_salario = salario_atual + (salario_atual * percentual_de_aumento)
print(f"O novo salário é: {novo_salario:8.2f}")