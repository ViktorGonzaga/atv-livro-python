class Estados:
    def __init__(self, sigla, nome):
        self.sigla = sigla
        self.nome = nome
        self.cidades = []
    def adiciona_cidade(self, cidade):
        self.cidades.append(cidade)
    def exibe_cidades(self):
        print(self.nome + " - " + self.sigla)
        for cidade in self.cidades:
            print(cidade.nome + " - " + str(cidade.poulacao) + " habitantes")