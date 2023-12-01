def eh_primo(n):
    for i in range (2, n):
        if (n % i) == 0:
            return False
    return True
def contar_primos_entre_1_e_n(n):
    if n < 1:
        return "O número deve ser maior que zero."

    count = 0
    for i in range(1, n + 1):
        if eh_primo(i):
            count += 1
    return print(count)

n = int(input("Digite um número positivo maior que zero: "))
quantidade_primos = contar_primos_entre_1_e_n(n)

