import math
def qualVolume(raio):
    volume = (4/3) * math.pi * (raio**3)

    return print(f" o volume é {volume:5.2f}")


raio = float(input("Digite o raio: "))
qualVolume(raio)