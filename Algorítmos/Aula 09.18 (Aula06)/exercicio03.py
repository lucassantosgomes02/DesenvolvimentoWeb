largura = float(input("Digite a largura do comodo em metros: "))
comprimento = float(input("Digite o comprimento do comodo em metros: "))
pe_direito = 2.80
area_paredes_laterais = ((pe_direito * largura) * 2) + ((pe_direito * comprimento) * 2)
area_da_porta = 2.10 * 0.80
rendimento_por_litro = 3
quantidade_de_litros = (area_paredes_laterais - area_da_porta) / rendimento_por_litro
print(f"Será necessário {quantidade_de_litros:8.2f} litros de tinta para pintar as paredes do comodo .")