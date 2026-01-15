from plantas.planta import Planta

class Briofita(Planta):
    def __init__(self, nome, id_planta, tipo, porte,
                 curiosidade, regiao,
                 nome_fruto, cor_fruto, cor_folhas):

        super().__init__(
            nome, id_planta, tipo, porte,
            curiosidade, regiao,
            nome_fruto, cor_fruto, cor_folhas
        )

    def __str__(self):
        return super().__str__()

    __repr__ = __str__
