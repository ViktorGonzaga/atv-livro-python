def cap_3():
    def ex_1():
        return ('inteiro, flutuante, flutuante, inteiro, inteiro, flutuante')
    
    def ex_4():
        salario = 1201
        pagar_imposto = salario > 1200
        return pagar_imposto

    def ex_6():
        nota1 = 7
        nota2 = 8
        nota3 = 9
        media = (nota1 + nota2 + nota3) / 3
        situacao = media > 7
        return situacao

    def ex_7():
        a = int(input("Digite um número inteiro:"))
        b = int(input("Digite outro número inteiro:"))

        return a + b

    def ex_8():
        metros = float(input("Digite uma medida em metros:"))
        milimetros = metros * 1000

        return milimetros

    def ex_9():
        dias = int(input("Digite um número de dias:"))
        horas = int(input("Digite um número de horas:"))
        minutos = int(input("Digite um número de minutos:"))
        segundos = int(input("Digite um número de segundos:"))

        return (dias * 24 * 60 * 60) + (horas * 60 * 60) + (minutos * 60) + segundos

    def ex_10():
        salario = float(input('Digite seu salário:'))
        aumento  = int('Qual foi a porcentagem de aumento?')
        
        return salario + (aumento / 100 * salario)

    def ex_11():
        preco = float(input('Digite o preço do produto:'))
        desconto = int('Qual foi o desconto?')

        return preco - (desconto / 100 * preco)

    def ex_12():
        distancia = float(input('Digite a distância da viagem:'))
        velocidade = int('Qual a velocidade média da viagem?')

        return distancia / velocidade

    def ex_13():
        temperatura_celsius = float(input('Digite a temperatura em Celsius:'))

        return (9 * temperatura_celsius / 5) + 32

    def ex_14():
        km_percorridos = float(input('Digite a distância percorrida:'))
        dias = int(input('Quantos dias o carro foi utilizado?'))
        preco = 60 * dias + 0.15 * km_percorridos

        return preco

    def ex_15():
        cigarros_dia = int(input('Quantos cigarros você fuma por dia?'))
        anos_fumados = int(input('Quantos anos você fuma?'))
        tempo_perdido = cigarros_dia * 10 * 365 * anos_fumados

        return tempo_perdido


if __name__ == '__main__':
    cap_3()
