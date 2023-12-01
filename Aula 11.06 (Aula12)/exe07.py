def eh_primo(numero):
    if numero <= 1:
        return False
    if numero <= 3:
        return True
    if numero % 2 == 0 or numero % 3 == 0:
        return False
    i = 5
    while i * i <= numero:
        if numero % i == 0 or numero % (i + 2) == 0:
            return False
        i += 6
    return True


def contar_primos_entre_1_e_n(n):
    if n < 1:
        return "O número deve ser maior que zero."

    count = 0
    for i in range(1, n + 1):
        if eh_primo(i):
            count += 1
    return count


n = int(input("Digite um número positivo maior que zero: "))
quantidade_primos = contar_primos_entre_1_e_n(n)

if isinstance(quantidade_primos, str):
    print(quantidade_primos)
else:
    print(f"Existem {quantidade_primos} números primos entre 1 e {n}.")