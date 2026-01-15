class Planta:
    def __init__(self, nome, id_planta, tipo, porte,
                 curiosidade, regiao,
                 nome_fruto, cor_fruto, cor_folhas):

        self.nome = nome
        self.id_planta = id_planta
        self.tipo = tipo
        self.porte = porte
        self.curiosidade = curiosidade
        self.regiao = regiao
        self.nome_fruto = nome_fruto
        self.cor_fruto = cor_fruto
        self.cor_folhas = cor_folhas

    def __str__(self):
        texto = (
            f"Nome: {self.nome}\n"
            f"ID: {self.id_planta}\n"
            f"Tipo: {self.tipo}\n"
            f"Porte: {self.porte}\n"
            f"Região: {self.regiao}\n"
            f"Cor das folhas: {self.cor_folhas}\n"
        )

        if self.curiosidade:
            texto += f"Curiosidade: {self.curiosidade}\n"

        if self.nome_fruto:
            texto += f"Fruto: {self.nome_fruto} ({self.cor_fruto})\n"

        return texto
    __repr__ = __str__