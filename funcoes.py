class Vagao:
    def __init__(self, numero, trem):
        self.numero = numero  # Número do vagão
        self.proximo = None  # Próximo vagão na composição
        self.trem = trem  # Número do trem ao qual o vagão pertence
        self.vagoes_acoplados = []  # Lista de vagoes acoplados a este vagão

    def acoplar_vagao(self, vagao):
        self.vagoes_acoplados.append(vagao)  # Adiciona um vagão à lista de vagoes acoplados

    def exibir_vagoes_acoplados(self):
        for vagao in self.vagoes_acoplados:
            print(f"Vagão {vagao.numero} (Trem {vagao.trem})")  # Exibe vagoes acoplados


class FuncoesTrem:
    def __init__(self):
        self.topo = None  # O topo da composição inicialmente está vazio

    def adicionar_vagao(self, numero, trem):
        # Adiciona um novo vagão à composição
        vagao_novo = Vagao(numero, trem)
        if not self.topo:  # Se a composição está vazia
            self.topo = vagao_novo
            vagao_novo.proximo = self.topo
        else:  # Se a composição já possui vagões
            temp = self.topo
            while temp.proximo != self.topo:
                temp = temp.proximo
            temp.proximo = vagao_novo
            vagao_novo.proximo = self.topo

    def buscar_vagoes_por_trem(self, trem):
        # Busca todos os vagões pertencentes a um trem específico
        if not self.topo:
            print("A composição está vazia")
            return []

        vagoes = []
        temp = self.topo
        while True:
            if temp.trem == trem:
                vagoes.append(temp)
            temp = temp.proximo
            if temp == self.topo:
                break

        return vagoes

    def contar_vagoes(self):
        # Conta a quantidade de vagões na composição
        if not self.topo:
            return 0

        count = 0
        temp = self.topo
        while True:
            count += 1
            temp = temp.proximo
            if temp == self.topo:
                break

        return count

    def remover_vagao(self, numero, trem):
        # Remove um vagão específico da composição
        if not self.topo:
            print("A composição está vazia")
            return
        if self.topo.numero == numero and self.topo.trem == trem:
            if self.topo.proximo == self.topo:
                self.topo = None
            else:
                temp = self.topo
                while temp.proximo != self.topo:
                    temp = temp.proximo
                temp.proximo = self.topo.proximo
                self.topo = self.topo.proximo
        else:
            temp = self.topo
            while temp.proximo != self.topo:
                if temp.proximo.numero == numero and temp.proximo.trem == trem:
                    temp.proximo = temp.proximo.proximo
                    return
                temp = temp.proximo
            print(f"Vagão {numero} do Trem {trem} não encontrado na composição")
