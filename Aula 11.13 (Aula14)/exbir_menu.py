def exibir_menu():

    menu = int(input(" 1- Cadastrar\n 2- Exibir Frase\n 3- Sair \n" ))

    while menu == 0 or menu > 3:
        print("Valor inválido, escolha uma das opções:")
        menu = int(input(" 1- Cadastrar \n 2- Exibir Frase \n 3- Sair \n"))

    return menu













