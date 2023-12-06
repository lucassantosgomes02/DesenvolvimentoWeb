def eh_primo(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def contar_primos_ate_n(n):
    count = 0
    for i in range(n + 1):
        if eh_primo(i):
            count += 1
    return count

Y = 26
total_primos = Y * 2 + 5
num_primos = [i for i in range(total_primos + 1) if eh_primo(i)]
soma_primos = sum(num_primos)


print("Os números primos vão até", total_primos, "A seguir a relação:", num_primos)
print("E a soma deles é:", soma_primos)
