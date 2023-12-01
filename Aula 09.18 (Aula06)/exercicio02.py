valor_compra = float(input("Digite o valor da compra: "))
if valor_compra <= 1000:
    desconto = valor_compra * 0.10
elif valor_compra <= 5000:
    desconto = valor_compra * 0.20
else:
    desconto = valor_compra * 0.30
valor_com_desconto = valor_compra - desconto
print(f"Desconto aplicado: R${desconto:.2f}")
print(f"Valor final com desconto: R${valor_com_desconto:.2f}")