from funcoes import FuncoesTrem


i = 0
while i != 5:
    i = int(input("\nO que você deseja fazer?\n1 - Adicionar Vagão\n2 - Remover Vagão\n3 - Buscar Vagão por trem\n4 - "
                  "Contar vagões\n5 - Sair\n\n"))
    funcao = FuncoesTrem()

    if i == 1:
        nVagao = int(input("\nEntre com o número do vagão: "))
        nTrem = int(input("Entre em qual trem será adicionado esse vagão: "))
        print("\n\n")

        funcao.adicionar_vagao(nVagao, nTrem)
        funcao.exibir_composicao()

    if i == 2:
        nVagao = int(input("Entre com o numero do vagao que deseja remover: "))
        funcao.remover_vagao(nVagao)
        funcao.exibir_composicao()

    if i == 4:
        quantidade_vagoes = funcao.contar_vagoes()
        print(f"Quantidade de vagões na composição: {quantidade_vagoes}")
