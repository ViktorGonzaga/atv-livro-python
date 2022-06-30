import random

def cap_8():
    # Capítulo sobre funções
    NOME = 'Viktor da Silva Gonzaga'
    def maximo(a,b):
        if a > b:
            return a
        else:
            return b
    
    def multiplo(a,b):
        if a % b == 0:
            return True
        else:
            return False

    def area_quadrado(l):
        if l > 0:
            return l**2
        else:
            return 'Valor inválido'
    

    def area_triangulo(base,altura):
        if base > 0 and altura > 0:
            return base*altura/2
        else:
            return 'Valor inválido'
    
    def pequisa(lista, valor):
        if valor in lista:
            return True
        else:
            return False

    def soma_for(lista):
        total = 0
        for i in lista:
            total += i
        return total

    # Funções recursivas
    def mdc(a,b):
        if b == 0:
            return a
        else:
            return mdc(b, a % b)

    def mmc(a,b):
        return (a*b)/mdc(a,b)

    def fibonacci(n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            x = 0
            y = 1
            while n > 1:
                x, y = y, x + y
                n -= 1
            return y
    
    def ex_11(string, minimo, maximo):
        if minimo < len(string) and maximo > len(string):
            return True
        else:
            return False

    def ex_12(string, lista):
        if string in lista:
            return True
        else:
            return False
    
    def jogo_sorte():
        n = random.randint(1,10)
        chances = 3
        while True:
            if chances == 0:
                print('Você perdeu!')
                break
            x = int(input('Digite um número: '))
            if x == n:
                print('Você acertou!')
                break
            else:
                print('Você errou!')
                chances -= 1

    jogo_sorte()
    


if __name__ == '__main__':
    cap_8()
