frase = input("Digite uma frase: ")
palavra_alvo = input("Digite a palavra que deseja contar na frase: ")
palavras = frase.split()
numero_de_palavras = len(palavras)
numero_de_ocorrencias = palavras.count(palavra_alvo)
print(f"A frase tem {numero_de_palavras} palavras.")
print(f"A palavra '{palavra_alvo}' ocorre {numero_de_ocorrencias} vezes na frase.")
