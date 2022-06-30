def cap_6():
    def ex_1():
        notas = [0,0,0,0,0,0,0]
        soma = 0
        x = 0
        while x < 7:
            notas[x] = float(input("Digite a nota: "))
            soma += notas[x]
            x += 1
        x = 0
        while x < 7:
            print("Nota: ", notas[x])
            x += 1
        print("Media: {}" .format(soma/7))
    
    def ex_2():
        print('Primeira lista:')
        lista1 = []
        lista2 = []
        while True:
            n = input('Digite um elemento da lista ("Fim para sair"): ')
            if n == 'fim':
                break
            lista1.append(n)
        print("Segunda Lista")
        while True:
            n = input('Digite um elemento da lista ("Fim para sair"): ')
            if n == 'fim':
                break
            lista2.append(n)
        lista1.extend(lista2)
        print(lista1)


    def ex_3():
        print('Primeira lista:')
        lista1 = []
        lista2 = []
        while True:
            n = input('Digite um elemento da lista ("Fim para sair"): ')
            if n == 'fim':
                break
            lista1.append(n)
        print("Segunda Lista")
        while True:
            n = input('Digite um elemento da lista ("Fim para sair"): ')
            if n == 'fim':
                break
            x = 0
            adiciona = True
            while x < len(lista1):
                if lista1[x] == n:
                    adiciona = False
                x += 1
            if adiciona:
                lista1.append(n)
        lista1.extend(lista2)
        print(lista1)


    def ex_5():
        ultimo = 10
        fila = list(range(1, ultimo+1))
        sair = False
        while True:
            print("\nExistem %d clientes na fila" % len(fila))
            print(f"\nFila atual: {fila}")
            print('\nDigite F para adicionar um cliente ao final da fila,')
            print('Ou A para realizar o atendimento. S para sair')
            operacao = input('Digite a opção: ')
            x = 0
            while x < len(operacao):
                if operacao[x] == 'A':
                    if len(fila) > 0:
                        atendido = fila.pop(0)
                        print("Cliente %d atendido" % atendido)
                    else:
                        print("Fila vazia")
                elif operacao[x] == 'F':
                    ultimo += 1
                    fila.append(ultimo)
                elif operacao[x] == 'S':
                    sair = True
                    break
                else:
                    print('Opção inválida')
                x += 1
            if sair:
                print(fila)
                break
    
    def ex_6():
        ultimo = 10
        fila1 = list(range(1, ultimo+1))
        fila2 = list(range(1, ultimo+1))
        while True:
            sair = False
            fila = int(input("Digite a fila (0 para sair): "))
            if fila == 0:
                break
            elif fila == 1:
                while True:
                    print("\nExistem %d clientes na fila" % len(fila1))
                    print(f"\nFila atual: {fila1}")
                    print('\nDigite F para adicionar um cliente ao final da fila,')
                    print('Ou A para realizar o atendimento. S para sair')
                    operacao = input('Digite a opção: ')
                    x = 0
                    while x < len(operacao):
                        if operacao[x] == 'A':
                            if len(fila1) > 0:
                                atendido = fila1.pop(0)
                                print("Cliente %d atendido" % atendido)
                            else:
                                print("Fila vazia")
                        elif operacao[x] == 'F':
                            ultimo += 1
                            fila1.append(ultimo)
                        elif operacao[x] == 'S':
                            sair = True
                            break
                        else:
                            print('Opção inválida')
                        x += 1
                    if sair:
                        print(fila1)
                        break
            elif fila == 2:
                while True:
                    print("\nExistem %d clientes na fila" % len(fila2))
                    print(f"\nFila atual: {fila2}")
                    print('\nDigite F para adicionar um cliente ao final da fila,')
                    print('Ou A para realizar o atendimento. S para sair')
                    operacao = input('Digite a opção: ')
                    x = 0
                    while x < len(operacao):
                        if operacao[x] == 'A':
                            if len(fila2) > 0:
                                atendido = fila2.pop(0)
                                print("Cliente %d atendido" % atendido)
                            else:
                                print("Fila vazia")
                        elif operacao[x] == 'F':
                            ultimo += 1
                            fila2.append(ultimo)
                        elif operacao[x] == 'S':
                            sair = True
                            break
                        else:
                            print('Opção inválida')
                        x += 1
                    if sair:
                        print(fila1)
                        break
            else:
                print('Opção inválida')
        
        print(f'Lista 1: {fila1}')
        print(f'Lista 2: {fila2}')

    
    def ex_7():
        parenteses = input('Digite uma quantidade de parenteses: ')
        abertos = []
        fechados = []
        if len(parenteses) > 0:
            x = 0
            while x < len(parenteses):
                if parenteses[x] == '(':
                    abertos.append(parenteses[x])
                elif parenteses[x] == ')':
                    fechados.append(parenteses[x])
                x += 1
            if len(abertos) == len(fechados):
                print('Parenteses balanceados')
            else:
                print('Parenteses não balanceados')
        else:
            print('Digite ao menos um parenteses')

    def ex_7_2():
        parenteses = input('Digite uma quantidade de parênteses ')
        lista = []
        if len(parenteses) > 0:
            x = 0
            while x < len(parenteses):
                if parenteses[x] == '(':
                    lista.append(1)
                x += 1
            x = 0
            while x < len(parenteses):
                if parenteses[x] == ')':
                    if len(lista) > 0:
                        lista.pop()
                    else:
                        print('Parenteses não balanceados')
                        break
                x += 1
            if len(lista) == 0:
                print('Parenteses balanceados')
            else:
                print('Parenteses não balanceados')
        else:
            print('Digite ao menos um parenteses')


    def ex_8():
        l = [15, 7, 27, 39]
        p = int(input('Digite um número: '))
        x = 0
        while x < len(l):
            if l[x] == p:
                break
            x += 1
        if x == len(l):
            print('Número não encontrado')
        else:
            print('Número encontrado na posição %d' % x)	


    def ex_9():
        l = [15, 7, 27, 39]
        p = int(input('Digite um número: '))
        v = int(input('Digite outro valor: '))
        x = 0
        while x < len(l):
            if l[x] == p:
                print(f"Número {p} encontrado na posição {x}")
                break
            elif l[x] == v:
                print(f"Número {v} encontrado na posição {x}")
                break
            x += 1
        if x == len(l):
            print('Número não encontrado')

    def ex_10():
        l = [15, 7, 27, 39]
        p = int(input('Digite um número: '))
        v = int(input('Digite outro valor: '))
        x = 0
        encontrado_p = False
        encontrado_v = False
        while x < len(l):
            if l[x] == p:
                encontrado_p = True
                posicao_p = x
            elif l[x] == v:
                encontrado_v = True
                posicao_v = x
            x += 1
        if encontrado_p:
            print(f"Número {p} encontrado na posição {posicao_p}")
        else:
            print(f'O número {p} não foi encontrado')
        if encontrado_v:
            print(f"Número {v} encontrado na posição {posicao_v}")
        else:
            print(f'O número {v} não foi encontrado')
        
    
    def ex_11():
        l = []
        while True:
            n = int(input("Digite um número: "))
            if n == 0:
                break
            l.append(n)
        for x in l:
            print(x)
        
        # Não da para usar o for em loops que necessitam de condições de parada dinâmicas
    
    def ex_12():
        l = [5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39]
        minimo = l[0]
        for e in l:
            if e < minimo:
                minimo = e
        print(f'O menor número da lista é {minimo}')


    def ex_13():
        t = [-10, -8, 0, 2, 5, -2, -4]
        maximo = t[0]
        minimo = t[0]
        soma = 0
        for e in t:
            soma += e
            if e > maximo:
                maximo = e
            if e < minimo:
                minimo = e
        print(f'A maior temperatura foi de: {maximo}')
        print(f'A menor temperatura foi de: {minimo}')
        print(f'A média das temperaturas é: {soma/len(t)}')

    
    def ex_14():
        l = list(range(1,6))
        fim = 5
        while fim > 1:
            trocou = False
            x = 0
            while x < fim - 1:
                if l[x] > l[x+1]:
                    l[x], l[x+1] = l[x+1], l[x]
                    trocou = True
                x += 1
            if not trocou:
                break
            fim -= 1
        for e in l:
            print(e)

    
    def ex_15():
        l = [3,3,1,5,4]
        fim = 5
        while fim > 1:
            trocou = False
            x = 0
            while x < fim - 1:
                if l[x] > l[x+1]:
                    l[x], l[x+1] = l[x+1], l[x]
                    trocou = True
                x += 1
            if not trocou:
                break
            fim -= 1
        for e in l:
            print(e)


    def ex_16():
            l = [1,2,3,4,5]
            fim = 5
            while fim > 1:
                trocou = False
                x = 0
                while x < fim - 1:
                    if l[x] < l[x+1]:
                        l[x], l[x+1] = l[x+1], l[x]
                        trocou = True
                    x += 1
                if not trocou:
                    break
                fim -= 1
            for e in l:
                print(e)


    def  ex_17():
        estoque = { "Tomate": [1000,2.30],
                    "Alface": [500,0.45],
                    "Batata": [2001,1.20],
                    "Feijão": [100,1.50] }
        total = 0
        while True:
            print(estoque)
            nome = input('Digite o nome do produto: ')
            if nome == 'sair':
                break
            if nome not in estoque:
                print('Produto não encontrado')
                break
            if nome in estoque:
                quantidade = int(input('Digite a quantidade: '))
                if quantidade > estoque[nome][0]:
                    print('Quantidade insuficiente')
                if quantidade <= estoque[nome][0]:
                    preco = estoque[nome][1] * quantidade
                    estoque[nome][0] -= quantidade
            total += preco
        print(f'O total a pagar é: {total}')
        for e in estoque:
            print(f'{e}: {estoque[e][0]}')


    def ex_18():
        frase = input('Digite uma frase: ')
        dicionario = {}
        for letra in frase:
            if letra in dicionario:
                dicionario[letra] += 1
            else:
                dicionario[letra] = 1

        print(dicionario)


    ex_18()

if __name__=='__main__':
    cap_6()