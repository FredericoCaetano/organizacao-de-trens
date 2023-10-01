from funcoes import FuncoesTrem

# Cria uma instância da classe FuncoesTrem
funcao = FuncoesTrem()

# Loop principal para interagir com o programa
i = 0
while i != 5:
    i = int(input(
        "\nO que você deseja fazer?\n1 - Adicionar Vagão\n2 - Remover Vagão\n3 - "
        "Buscar Vagão por trem\n4 - Contar vagões\n5 - Sair\n\n"))

    # Opção para adicionar um novo vagão
    if i == 1:
        nVagao = int(input("\nEntre com o número do vagão que deseja adicionar: "))
        nTrem = int(input("Entre em qual trem será adicionado esse vagão: "))
        print("\n\n")

        funcao.adicionar_vagao(nVagao, nTrem)

    # Opção para remover um vagão
    if i == 3:
        nVagao = int(input("\nEntre com o numero do vagao que deseja remover: "))
        nTrem = int(input("Entre com o número do trem que será removido esse vagão: "))
        funcao.remover_vagao(nVagao, nTrem)

    # Opção para buscar vagoes por trem
    if i == 4:
        nTrem = int(input("\nEntre com o número do trem: "))
        vagoes_encontrados = funcao.buscar_vagoes_por_trem(nTrem)
        if vagoes_encontrados:
            print(f"Vagões do Trem {nTrem}:")
            for vagao in vagoes_encontrados:
                print(f"Vagão {vagao.numero} (Trem {vagao.trem})")
        else:
            print(f"Não foram encontrados vagões para o Trem {nTrem}")

    # Opção para contar a quantidade de vagões na composição
    if i == 5:
        quantidade_vagoes = funcao.contar_vagoes()
        print(f"\nQuantidade de vagões na composição: {quantidade_vagoes}")

    # Opção para tratar erro
    else:
        print("\nOpção inválida!")
