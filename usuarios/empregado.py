class Empregado:
    def __init__(self, nome):
        self.nome = nome
        self._senha = None

    def tem_senha(self):
        return self._senha is not None

    def definir_senha(self, senha):
        self._senha = senha

    def autenticar(self):
        return self._senha is not None
