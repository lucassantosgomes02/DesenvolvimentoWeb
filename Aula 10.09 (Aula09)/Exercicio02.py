lista = []
for i in range(5):
    lista.append (int(input(f"Digite o {i+1}º número inteiro: ")))

    posicao = 0
    maior_valor = lista[posicao]


for i in range(0, len(lista)):
    if lista[i] > maior_valor:
        maior_valor = lista[i]
        posicao = i

print(f"O maior valor é {maior_valor} e está na posição {posicao}.")
