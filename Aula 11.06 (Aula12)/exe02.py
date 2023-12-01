def ehprimo(n):
    for i in range (2, n):
        if (n % i) == 0:
            return print(f"{False}, O numéro não é primo")
    return print(f"{True}, O numéro é primo")

n = int(input("Digite o valor: "))
ehprimo(n)

