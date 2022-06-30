def cap_4():
    def ex_2():
        velocidade = int(input('Qual a velocidade de seu carro?'))
        if velocidade > 80:
            multa = (velocidade - 80) * 5
            print(f'Você foi multado no valor de R${multa:.2f}')

    def ex_3():
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))
        numero3 = int(input('Digite mais um número: '))

        if numero1 >= numero2 and numero1 >= numero3:
            maior = numero1
            if numero2 <= numero3:
                menor = numero2
            else:
                menor = numero3
        elif numero2 >= numero1 and numero2 >= numero3:
            maior = numero2
            if numero1 <= numero3:
                menor = numero1
            else:
                menor = numero3
        else:
            maior = numero3
            if numero1 <= numero2:
                menor = numero1
            else:
                menor = numero2

        return f"maior = {maior} e menor = {menor}"

    def ex_4():
        salario = float(input('Qual o salário do funcionário? '))

        if salario > 0:
            if salario <= 1250:
                aumento = salario * 0.15
            else:
                aumento = salario * 0.10
        else:
            return 'Salário inválido'

        return f'O novo salário do funcionário é R${salario + aumento:.2f}'

    def ex_5():
        distancia = float(input('Qual a distância da sua viagem? '))
        if distancia > 0:
            if distancia <= 200:
                preco = distancia * 0.50
            else:
                preco = distancia * 0.45
        else:
            return 'Distância inválida'

        return f'O preço da sua viagem é R${preco:.2f}'

    def ex_8():
        numero1 = int(input('Digite um número: '))
        numero2 = int(input('Digite outro número: '))
        operacao = input('Digite a operação (+, -, *, /): ')

        if operacao == "+" or operacao == '-' or operacao == '*' or operacao == '/':
            if operacao == '+':
                resultado = numero1 + numero2
            elif operacao == '-':
                resultado = numero1 - numero2
            elif operacao == '*':
                resultado = numero1 * numero2
            else:
                if numero2 != 0:
                    resultado = numero1 / numero2
                else:
                    return 'Não é possível dividir por zero'
        else:
            return 'Operação inválida'

        return f'O resultado da operação é {resultado}'

    def ex_9():
        preco_casa = float(input('Qual o preço da casa? '))
        salario = float(input('Qual o salário do comprador? '))
        tempo = int(input('Quantos anos de financiamento? '))

        if salario > 0 and preco_casa > 0 and tempo > 0:
            prestacao = preco_casa / (tempo * 12)
            if prestacao <= (salario * 0.3):
                return 'Empréstimo aprovado'
            else:
                return 'Empréstimo negado'
        else:
            return 'Dados inválidos'

    def ex_10():
        qtd_energia_consumida = float(
            input('Qual a quantidade de energia consumida? '))

        if qtd_energia_consumida > 0:
            tipo_instalacao = input(
                'Qual o tipo de instalação? [1]Residencial [2]Comercial [3]Industrial: ')

            if tipo_instalacao == '1':
                if qtd_energia_consumida <= 500:
                    valor_consumo = qtd_energia_consumida * 0.45
                else:
                    valor_consumo = qtd_energia_consumida * 0.65
            elif tipo_instalacao == '2':
                if qtd_energia_consumida <= 1000:
                    valor_consumo = qtd_energia_consumida * 0.55
                else:
                    valor_consumo = qtd_energia_consumida * 0.60
            else:
                if qtd_energia_consumida <= 5000:
                    valor_consumo = qtd_energia_consumida * 0.55
                else:
                    valor_consumo = qtd_energia_consumida * 0.60


if __name__ == '__main__':
    cap_4()
