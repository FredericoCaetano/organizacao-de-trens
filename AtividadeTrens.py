class Vagao:
    def __init__(self, numero, trem):
        self.numero = numero
        self.proximo = None
        self.trem = trem
        self.vagoes_acoplados = []

    def acoplar_vagao(self, vagao):
        self.vagoes_acoplados.append(vagao)

    def exibir_vagoes_acoplados(self):
        for vagao in self.vagoes_acoplados:
            print(f"Vagão {vagao.numero} (Trem {vagao.trem})")


class FuncoesTrem:
    def __init__(self):
        self.topo = None

    def adicionar_vagao(self, numero, trem):
        vagao_novo = Vagao(numero, trem)
        if not self.topo:
            self.topo = vagao_novo
            vagao_novo.proximo = self.topo
        else:
            temp = self.topo
            while temp.proximo != self.topo:
                temp = temp.proximo
            temp.proximo = vagao_novo
            vagao_novo.proximo = self.topo

    def buscar_vagoes_por_trem(self, trem):
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

    def acoplar_vagao_ao_ultimo(self, vagao_acoplado):
        if not self.topo:
            print("A composição está vazia")
            return

        temp = self.topo
        while temp.proximo != self.topo:
            temp = temp.proximo
        temp.acoplar_vagao(vagao_acoplado)

    def contar_vagoes(self):
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

    def remover_vagao(self, numero):
        if not self.topo:
            print("A composição está vazia")
            return
        if self.topo.numero == numero:
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
                if temp.proximo.numero == numero:
                    temp.proximo = temp.proximo.proximo
                    return
                temp = temp.proximo
            print(f"Vagão {numero} não encontrado na composição")

    def exibir_composicao(self):
        if not self.topo:
            print("A composição está vazia")
            return
        temp = self.topo
        while True:
            print(f"Vagão {temp.numero} (Trem {temp.trem})", end=" -> ")
            temp = temp.proximo
            if temp == self.topo:
                break
