data = input("Digite a data no formato dd/mm/aaaa: ")
data_formatada = data[6:] + data[3:5] + data[0:2]
print("Data formatada: ", data_formatada)
