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
        palavra = input("Digite a palavra secreta: ").lower().strip()
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
            print("X  O  " if erros >= 1 else "X")
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

        numero_digitado = int(
            input("Digite um número (para sortear a palavra): "))
        indice = (numero_digitado*776) % len(palavras)
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


if __name__ == '__main__':
    cap_7()
