pessoas = {}

for i in range(5):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))
    pessoas[nome] = idade

idades = list(pessoas.values())
media_das_idades = sum(idades)/len(idades)

for nome, idade in pessoas.items():
    if idade > media_das_idades:
        print(nome)