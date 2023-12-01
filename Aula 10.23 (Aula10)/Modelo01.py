lista = [1]
while len(lista) < 7:
    lista.append(lista[-1]*len(lista))
    print(lista)