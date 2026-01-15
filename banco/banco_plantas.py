class BancoPlantas:
    def __init__(self):
        self.plantas = []

    def adicionar(self, planta):
        self.plantas.append(planta)

    def buscar(self, chave):
        for p in self.plantas:
            if p.nome.lower() == chave.lower() or p.id_planta == chave:
                return p
        return None

    def remover(self, chave):
        planta = self.buscar(chave)
        if planta:
            self.plantas.remove(planta)
            return True
        return False
