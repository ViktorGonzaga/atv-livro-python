import random


def cap_8():
    # Capítulo sobre funções
    NOME = 'Viktor da Silva Gonzaga'

    def maximo(a, b):
        if a > b:
            return a
        else:
            return b

    def multiplo(a, b):
        if a % b == 0:
            return True
        else:
            return False

    def area_quadrado(l):
        if l > 0:
            return l**2
        else:
            return 'Valor inválido'

    def area_triangulo(base, altura):
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
    def mdc(a, b):
        if b == 0:
            return a
        else:
            return mdc(b, a % b)

    def mmc(a, b):
        return (a*b)/mdc(a, b)

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
        n = random.randint(1, 10)
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

    def ex_8():
        palavras = []
        while True:
            palavra = input(
                "Digite uma palavra secreta (fim para sair): ").lower().strip()
            if palavra != "fim" and palavra not in palavras:
                palavras.append(palavra)
                print(palavras)
            elif palavra == "fim":
                break
            else:
                print("Palavra já existente")

        indice = random.randint(0, len(palavras)-1)
        palavra = palavras[indice]
        print("\n"*100)
        digitadas = []
        acertos = []
        erros = 0
        while True:
            senha = ""
            for letra in palavra:
                if letra in acertos:
                    senha += letra
                else:
                    senha += "."
            print(senha)
            if senha == palavra:
                print("Você acertou!")
                break
            tentativa = input("\nDigite uma letra: ").lower().strip()
            if tentativa in digitadas:
                print("Você já tentou esta letra!")
                continue
            else:
                digitadas += tentativa
                if tentativa in palavra:
                    acertos += tentativa
                else:
                    erros += 1
                    print("Você errou!")
            print("X==:==\nX  :  ")
            if erros >= 1:
                print("X  O  ")
            else:
                print("X")
            linha2 = ""
            if erros == 2:
                linha2 = "  |  "
            elif erros == 3:
                linha2 = " \|  "
            elif erros >= 4:
                linha2 = " \|/ "
            print(f"X{linha2}")
            linha3 = ""
            if erros == 5:
                linha3 += " /   "
            elif erros >= 6:
                linha3 += " / \ "
            print(f"X{linha3}")
            print("X\n===========")
            if erros == 6:
                print("Enforcado!")
                print(f"A palavra era: {palavra}")
                break

    def ex_15():
        ESPAÇOS_POR_NÍVEL = 4

        def imprime_elementos(l, nivel=0):
            espacos = ' ' * ESPAÇOS_POR_NÍVEL * nivel
            if type(l) == list:
                print(espacos, "[")
                for e in l:
                    imprime_elementos(e, nivel + 1)
                print(espacos, "]")
            else:
                print(espacos, l)

        L = [1, [2, 3, 4, [5, 6, 7]]]

        imprime_elementos(L)


if __name__ == '__main__':
    cap_8()
