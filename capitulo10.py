def ex_1():
    class Televisao:
        def __init__(self):
            self.ligada = False
            self.canal = 2
            self.tamanho = 45
            self.marca = 'Samsung'
            
    # Criando um objeto/instância da classe
    tv = Televisao()
    # Criando segundo objeto/instância da classe
    tv_2 = Televisao()
    # Imprimindo marca do objeto 1
    print(tv.marca)
    # Alterando o valor da marca do objeto 1
    tv.marca = 'LG'
    # Imprimindo marca do objeto 1
    print(tv.marca)
    # Imprimindo marca do objeto 2
    print(tv_2.marca)


def ex_2():
    class Televisao:
        def __init__(self, cinicial = 1, min = 1, max = 100):
            self.ligada = False
            self.canal = cinicial
            self.canal_min = min
            self.canal_max = max
        def muda_canal_para_baixo(self):
            if self.canal > self.canal_min:
                self.canal -= 1
        def muda_canal_para_cima(self):
            if self.canal < self.canal_max:
                self.canal += 1


def ex_3():
    class Televisao:
        def __init__(self, cinicial = 1, min = 1, max = 100):
            self.ligada = False
            self.canal = cinicial
            self.canal_min = min
            self.canal_max = max
        def muda_canal_para_baixo(self):
            if self.canal > self.canal_min:
                self.canal -= 1
            else:
                self.canal = self.canal_max
        def muda_canal_para_cima(self):
            if self.canal < self.canal_max:
                self.canal += 1
            else:
                self.canal = self.canal_min
    
    tv = Televisao(20, 1, 20)
    tv.muda_canal_para_cima()
    print(tv.canal)
    
    # Resolvidos exercicios 4 e 5 também aqui
