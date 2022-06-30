def cap_5():
    def ex_1():
        contagem = 1
        while contagem <= 100:
            print(contagem)
            contagem += 1

    def ex_2():
        contagem = 50
        while contagem <= 100:
            print(contagem)
            contagem += 1

    def ex_3():
        contagem = 10
        while contagem >= 0:
            print(contagem)
            contagem -= 1
        print('Fogo!')

    def ex_4():
        contagem = 1
        fim = int(input('Digite o número final: '))
        while contagem <= fim:
            print(contagem)
            contagem += 2

    def ex_5():
        multiplos_de_3 = 0
        qtd_repeticoes = 0
        while qtd_repeticoes < 10:
            print(multiplos_de_3)
            multiplos_de_3 += 3
            qtd_repeticoes += 1

    def ex_6():
        n = int(input('Digite um número: '))
        x = 1
        while x <= 10:
            print(n*x)
            x += 1

    def ex_7():
        n = int(input('Digite um número: '))
        inicio = int(input('Digite o número inicial: '))
        fim = int(input('Digite o número final: '))

        while inicio <= fim:
            print(n*inicio)
            inicio += 1

    def ex_8():
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))

        contador = numero2

        resultado = 0

        while contador > 0:
            resultado += numero1
            contador -= 1

        print(resultado)

    def ex_9():
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))

        resultado = 0
        resto = 0

        if numero2 > 0 and numero1 >= 0:
            while numero1 >= numero2:
                resultado += 1
                numero1 -= numero2
            resto = numero1
            print(resultado)
            print(resto)
        else:
            print('Não é possível fazer a divisão')

    def ex_10():
        pontos = 0
        questao = 1
        while questao <= 3:
            resposta = input('Resposta da questao %d: ' % questao)
            if questao == 1 and resposta == 'b' or resposta == 'B':
                pontos += 1
            elif questao == 2 and resposta == 'a' or resposta == 'A':
                pontos += 1
            elif questao == 3 and resposta == 'c' or resposta == 'C':
                pontos += 1

            questao += 1
        print('Pontos: %d' % pontos)

    def ex_11():
        deposito_inicial = float(input('Digite o valor do deposito inicial: '))
        taxa_juros = float(input('Digite a taxa de juros: '))
        meses = 1

        while meses <= 24:
            deposito_inicial += (deposito_inicial * taxa_juros) / 100
            print('Mês %d: %.2f' % (meses, deposito_inicial))
            meses += 1

    def ex_12():
        deposito_inicial = float(input('Digite o valor do deposito inicial: '))
        taxa_juros = float(input('Digite a taxa de juros: '))
        meses = 1
        valor_mensal_depositado = float(
            input('Digite o valor mensal depositado: '))

        deposito_variavel = deposito_inicial

        while meses <= 24:
            deposito_variavel += (deposito_inicial * taxa_juros) / 100
            print('Mês %d: %.2f' % (meses, deposito_variavel))
            deposito_inicial += valor_mensal_depositado
            meses += 1

    def ex_13():
        divida_inicial = float(input('Digite o valor da divida inicial: '))
        juros_mensais = float(input('Digite o valor dos juros mensais: '))
        valor_pago_mensalmente = float(
            input('Digite o valor pago mensalmente: '))
        meses = 0
        divida = divida_inicial
        total_pago = 0
        if valor_pago_mensalmente > 0 and juros_mensais > 0 and divida_inicial > 0:
            while divida > 0:
                divida += (divida * juros_mensais) / 100
                divida -= valor_pago_mensalmente
                total_pago += valor_pago_mensalmente
                meses += 1

            if divida < 0:
                total_pago += divida

            juros_pagos = total_pago - divida_inicial

            print('Total de meses: %d' % meses)
            print('Total pago: %.2f' % total_pago)
            print('Juros pagos: %.2f' % juros_pagos)

    def ex_14():
        quantidade_digitados = 0
        soma = 0
        media = 0
        while True:
            numero = int(input('Digite um número (0 para finalizar): '))
            if numero == 0:
                break
            quantidade_digitados += 1
            soma += numero
        if quantidade_digitados > 0:
            media = soma / quantidade_digitados
            print('A soma dos numeros é: %d' % soma)
            print('Quantidade de números digitados: %d' % quantidade_digitados)
            print('Média: %.2f' % media)
        else:
            print('Não foi digitado nenhum número')

    def ex_15():
        preco = 0
        while True:
            codigo_produto = int(
                input('Digite o codigo do produto (0 para sair): '))
            if codigo_produto == 0:
                break
            quantidade = int(input('Digite a quantidade: '))
            if quantidade > 0:
                if codigo_produto == 1:
                    preco += quantidade * 0.5
                elif codigo_produto == 2:
                    preco += quantidade * 1.00
                elif codigo_produto == 3:
                    preco += quantidade * 4.00
                elif codigo_produto == 5:
                    preco += quantidade * 7.00
                elif codigo_produto == 9:
                    preco += quantidade * 8.00
                else:
                    print('Código inválido')
            else:
                print('Quantidade inválida')
        print('Total: %.2f' % preco)

    def ex_18():
        valor = int(input('Digite o valor a pagar: '))
        notas = 0
        atual = 100
        apagar = valor

        while True:
            if apagar >= atual:
                notas += 1
                apagar -= atual
            else:
                print("%d notas de R$ %d" % (notas, atual))
                if apagar == 0:
                    break
                if atual == 100:
                    atual = 50
                elif atual == 50:
                    atual = 20
                elif atual == 20:
                    atual = 10
                elif atual == 10:
                    atual = 5
                elif atual == 5:
                    atual = 2
                elif atual == 2:
                    atual = 1
                notas = 0

    def ex_19():
        valor = float(input('Digite o valor a pagar: '))
        notas = 0
        atual = 100
        apagar = valor

        if valor >= 0.1:
            while True:
                if apagar >= atual:
                    notas += 1
                    apagar -= atual
                else:
                    print("%d notas de R$ %.2f" % (notas, atual))
                    if apagar < 0.01:
                        break
                    if atual == 100:
                        atual = 50
                    elif atual == 50:
                        atual = 20
                    elif atual == 20:
                        atual = 10
                    elif atual == 10:
                        atual = 5
                    elif atual == 5:
                        atual = 2
                    elif atual == 2:
                        atual = 1
                    elif atual == 1:
                        atual = 0.5
                    elif atual == 0.5:
                        atual = 0.25
                    elif atual == 0.25:
                        atual = 0.10
                    elif atual == 0.10:
                        atual = 0.05
                    elif atual == 0.05:
                        atual = 0.01
                    notas = 0
        else:
            print('Valor inválido')

    def ex_21():
        while True:
            valor = float(input('Digite o valor a pagar: '))
            if valor == 0:
                break
            notas = 0
            atual = 100
            apagar = valor

            if valor >= 0.1:
                while True:
                    if apagar >= atual:
                        notas += 1
                        apagar -= atual
                    else:
                        print("%d notas de R$ %.2f" % (notas, atual))
                        if apagar < 0.01:
                            break
                        if atual == 100:
                            atual = 50
                        elif atual == 50:
                            atual = 20
                        elif atual == 20:
                            atual = 10
                        elif atual == 10:
                            atual = 5
                        elif atual == 5:
                            atual = 2
                        elif atual == 2:
                            atual = 1
                        elif atual == 1:
                            atual = 0.5
                        elif atual == 0.5:
                            atual = 0.25
                        elif atual == 0.25:
                            atual = 0.10
                        elif atual == 0.10:
                            atual = 0.05
                        elif atual == 0.05:
                            atual = 0.01
                        notas = 0
            else:
                print('Valor inválido')

    def ex_22():
        operacao = input('Digite a operação: ')
        numero = 1
        if operacao == '+':
            while numero < 11:
                complemento = 1
                while complemento < 11:
                    print('%d + %d = %d' %
                          (numero, complemento, numero + complemento))
                    complemento += 1
                print('-----------')
                numero += 1
        elif operacao == '-':
            while numero < 11:
                complemento = 1
                while complemento < 11:
                    print('%d - %d = %d' %
                          (numero, complemento, numero - complemento))
                    complemento += 1
                print('-----------')
                numero += 1
        elif operacao == '*':
            while numero < 11:
                complemento = 1
                while complemento < 11:
                    print('%d * %d = %d' %
                          (numero, complemento, numero * complemento))
                    complemento += 1
                print('-----------')
                numero += 1
        elif operacao == '/':
            while numero < 11:
                complemento = 1
                while complemento < 11:
                    print('%d / %d = %.2f' %
                          (numero, complemento, numero / complemento))
                    complemento += 1
                print('-----------')
                numero += 1
        else:
            print('Operação inválida')

    def ex_23():
        # identificar se um numero é primo
        while True:
            numero = int(input('Digite um número: '))
            if numero <= 0:
                break
            elif numero == 2:
                primo = True
            else:
                if numero > 1:
                    primo = True
                    x = 3
                    while x < numero:
                        if numero % x == 0 or numero % 2 == 0:
                            primo = False
                            break
                        x += 2
                else:
                    primo = False
                    print('Número inválido')
            if primo:
                print('É primo')
            else:
                print('Não é primo')

    def ex_24():
        n = int(input('Digite a quantidade de números primos desejada: '))
        if n < 0:
            print('Número inválido')
        else:
            if n >= 1:
                print('2')
                p = 1
                y = 3
                while p < n:
                    primo = True
                    x = 3
                    while x < y:
                        if y % x == 0:
                            primo = False
                            break
                        x += 2
                    if primo:
                        print(y)
                        p += 1
                    y += 2

    def primo(n):
        if n < 2:
            return False
        elif n == 2:
            return True
        else:
            for i in range(2, n):
                if n % i == 0:
                    return False
            return True

    def ex_24_2():
        n = int(input('Digite a quantidade de números primos desejada: '))
        if n < 0:
            print('Número inválido')
        else:
            if n >= 1:
                print('2')
                x = 3
                while n > 1:
                    if primo(x):
                        print(x)
                        n -= 1
                    x += 2

    def ex_25():
        # Calcular a raiz quadrade de um número pelo metodo de Newton
        n = int(input('Digite o número: '))
        b = 2
        p = (b + (n/b))/2
        p_ao_quadrado = p**2
        while abs(p_ao_quadrado - n) > 0.0001:
            b = p
            p = (b + (n/b))/2
            p_ao_quadrado = p**2

        print('A raiz quadrada de %d é %.2f' % (n, p))

    def ex_26():
        # Calcular o resto de uma divisão com apenas o uso de adição e subtração
        numero1 = int(input('Digite o primeiro número: '))
        numero2 = int(input('Digite o segundo número: '))

        if numero1 > 0 and numero2 > 0:
            if numero1 < numero2:
                resto = numero1
            elif numero1 == numero2:
                resto = 0
            else:
                while numero1 >= numero2:
                    numero1 -= numero2
                resto = numero1
            print('O resto da divisão é %d' % resto)
        else:
            print('Entrada inválida')

    def ex_27():
        # Descobrir se um número é  palíndromo
        numero = input('Digite um número: ')
        if numero == numero[::-1]:
            print('É palíndromo')
        else:
            print('Não é palíndromo')


if __name__ == '__main__':
    cap_5()
