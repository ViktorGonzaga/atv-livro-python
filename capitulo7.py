def cap_7():
    def ex_1():
        string1 = input("Digite uma string: ")
        string2 = input("Digite outra string: ")

        p = 0

        while p > -1:
            p = string1.find(string2, p)
            if p > -1:
                print(
                    f"A string '{string2}' foi encontrada na string '{string1}' na posição {p}")
                break

    def ex_2():
        string1 = input("Digite uma string: ")
        string2 = input("Digite outra string: ")
        string3 = ''

        p = list(string1)
        q = list(string2)

        r = []

        for i in p:
            if i in q and i not in r:
                r.append(i)

        string3 = ''.join(r)

        print(f'Resultado: {string3}')

    def ex_3():
        string1 = input("Digite uma string: ")
        string2 = input("Digite outra string: ")
        string3 = ''

        p = list(string1)
        q = list(string2)

        r = []

        for i in p:
            if i not in q and i not in r:
                r.append(i)
        for i in q:
            if i not in p and i not in r:
                r.append(i)

        string3 = ''.join(r)

        print(f'Resultado: {string3}')

    def ex_4():
        string = input("Digite uma string: ")
        dicionario = {}
        for letra in string:
            if letra in dicionario:
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1

        for key, value in dicionario.items():
            print(f'{key}: {value}x')

    def ex_5():
        string1 = input("Digite uma string: ")
        string2 = input("Digite outra string: ")
        string3 = ''

        p = list(string1)
        q = list(string2)

        for i in p:
            if i not in q:
                string3 += i

        print(f'3ª string: {string3}')

    def ex_6():
        string1 = input("Digite uma string: ")
        string2 = input("Digite outra string: ")
        string3 = input("Digite outra string: ")

        if len(string2) == len(string3):
            resultado = ''
            for letra in string1:
                posicao = string2.find(letra)
                if posicao > -1:
                    resultado += string3[posicao]
                else:
                    resultado += letra

            if resultado == '':
                print('Todos os caracteres foram removidos')
            else:
                print(
                    f'Os caracteres {string2} foram substituidos por {string3}')
                print(f'Na string {string1} o resultado é: {resultado}')
        else:
            print("As strings 2 e 3 devem ter o mesmo tamanho")

    def ex_7():
        print(2)

    ex_7()


if __name__ == '__main__':
    cap_7()
