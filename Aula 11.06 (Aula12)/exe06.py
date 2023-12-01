def totalSegundos( h, m, s):
    hSeg = h * 3600
    mSeg = m * 60
    segundos = hSeg + mSeg + s
    return print(f" o total de segundos é: {segundos}s")

h = int(input("Digite a hora: "))
m = int(input("Digite os minutos: "))
s = int(input("Digite os segundos: "))
totalSegundos(h, m, s)