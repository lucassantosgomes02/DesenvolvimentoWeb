ano_de_nascimento = int(input("digite ano de nascimento: "))
ano_atual = int(input("Digite o ano atual "))
idade_em_anos = ano_atual - ano_de_nascimento
idade_em_meses = idade_em_anos * 12
idade_em_dias = idade_em_anos * 365
idade_em_semanas = idade_em_dias / 7

print("A idade em anos é ", idade_em_anos)
print("A idade em meses é ", idade_em_meses)
print("A idade em dias é ", idade_em_dias)
print("A idade em semana é ", idade_em_semanas)