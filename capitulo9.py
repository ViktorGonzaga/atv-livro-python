import sys


def cap_9():
    def ex_1():
        print("Digite o nome do arquivo: ")
        nome_arquivo = input()

        arquivo = open(nome_arquivo, "r")

        for linha in arquivo.readlines():
            print(linha, end="")

        arquivo.close()

    def ex_2():
        print("Digite o nome do arquivo: ")
        nome_arquivo = input()

        print("Digite a linha de inicio: ")
        linha_inicio = int(input())

        print("Digite a linha de fim: ")
        linha_fim = int(input())

        arquivo = open(nome_arquivo, "r")

        for i, linha in enumerate(arquivo.readlines()):
            if i >= linha_inicio - 1 and i <= linha_fim - 1:
                print(linha, end="")

        arquivo.close()

    def ex_3():
        impares = open("impares.txt", "r")
        pares = open("pares.txt", "r")
        pareseimpares = open("pareseimpares.txt", "w")

        impares_lista = impares.readlines()
        pares_lista = pares.readlines()

        while len(impares_lista) > 0 and len(pares_lista) > 0:
            pareseimpares.write(impares_lista.pop(0))
            pareseimpares.write(pares_lista.pop(0))

        impares.close()
        pares.close()
        pareseimpares.close()

    def ex_4():
        # Por alguma razão, não está funcionando com o arquivo capitulo8.py

        nome_arquivo_1 = sys.argv[1]
        nome_arquivo_2 = sys.argv[2]

        arquivo_1 = open(nome_arquivo_1, "r")
        arquivo_2 = open(nome_arquivo_2, "r")
        arquivo_3 = open("arquivo_3.txt", "w")

        for i in arquivo_1.readlines():
            arquivo_3.write(i)

        arquivo_3.close()

        arquivo_3 = open("arquivo_3.txt", "a")

        for i in arquivo_2.readlines():
            arquivo_3.write(i)

        arquivo_1.close()
        arquivo_2.close()
        arquivo_3.close()

    def ex_5():
        pares = open("pares.txt", "r")
        pares_invertidos = open("pares_invertidos.txt", "w")

        lista_pares = pares.readlines()
        lista_pares_invertidos = []

        for i in lista_pares[::-1]:
            lista_pares_invertidos.append(i)

        for j in lista_pares_invertidos:
            pares_invertidos.write(j)

    def ex_6():
        entrada = open("entrada.txt", "r")
        largura = 79
        for linha in entrada.readlines():
            if linha[0] == ';':
                continue
            elif linha[0] == '>':
                print(linha[1:].rjust(largura))
            elif linha[0] == '*':
                print(linha[1:].center(largura))
            elif linha[0] == '=':
                print("="*40)
            else:
                print(linha)
        entrada.close()

    def ex_7():
        LARGURA = 76
        LINHAS = 60
        
        # Aparentemente as quebras de linha estão fazendo com que a quantida de linhas seja maior que o esperado
        nome_do_arquivo = sys.argv[1]
        arquivo = open(nome_do_arquivo, "r")
        arquivo_saida = open("paginacao.txt", "w")
        qtd_linhas = 0
        pagina = 1
        for linha in arquivo.readlines():
            tamanho_linha = len(linha)
            if tamanho_linha > LARGURA:
                while tamanho_linha > LARGURA:
                    arquivo_saida.write(linha[:LARGURA] + "\n")
                    linha = linha[LARGURA:]
                    qtd_linhas += 1
                    if qtd_linhas == LINHAS:
                        arquivo_saida.write(f"Página {pagina}\n")
                        pagina += 1
                        qtd_linhas = 0
                    tamanho_linha = len(linha)
            arquivo_saida.write(linha + "\n")
            qtd_linhas += 1
            if qtd_linhas == LINHAS:
                arquivo_saida.write(f"-------------------Pagina {pagina}-----------------\n")
                qtd_linhas = 0
                pagina += 1

        arquivo.close()
        arquivo_saida.close()

    
    def ex_8():
        LARGURA = int(input("Digite a largura da página: "))
        LINHAS = int(input("Digite a quantidade de linhas da página: "))
        
        # Aparentemente as quebras de linha estão fazendo com que a quantida de linhas seja maior que o esperado
        nome_do_arquivo = sys.argv[1]
        arquivo = open(nome_do_arquivo, "r")
        arquivo_saida = open("paginacao_personalizada.txt", "w")
        qtd_linhas = 0
        pagina = 1
        for linha in arquivo.readlines():
            tamanho_linha = len(linha)
            if tamanho_linha > LARGURA:
                while tamanho_linha > LARGURA:
                    arquivo_saida.write(linha[:LARGURA] + "\n")
                    linha = linha[LARGURA:]
                    qtd_linhas += 1
                    if qtd_linhas == LINHAS:
                        arquivo_saida.write(f"-----------------Pagina {pagina}------------------\n")
                        pagina += 1
                        qtd_linhas = 0
                    tamanho_linha = len(linha)
            arquivo_saida.write(linha)
            qtd_linhas += 1
            if qtd_linhas == LINHAS:
                arquivo_saida.write(f"-------------------Pagina {pagina}-----------------\n")
                qtd_linhas = 0
                pagina += 1

        arquivo.close()
        arquivo_saida.close()
        

    def ex_9():
        if len(sys.argv) == 1:
            print("Não foi informado o nome do arquivo")
        else:
            lista_arquivos = sys.argv[1:]

            for i in lista_arquivos:
                arquivo = open(i, "r")
                for linha in arquivo.readlines():
                    print(linha)
                arquivo.close()
        
    
    def ex_10():
        if len(sys.argv) == 1:
            print("Não foi informado o nome do arquivo")
        else:
            lista_arquivos = sys.argv[1:]
            arquivo_saida = open("arquivo_saida.txt", "w")
            for i in lista_arquivos:
                arquivo = open(i, "r")
                for linha in arquivo.readlines():
                    arquivo_saida.write(linha)
                arquivo.close()
            arquivo_saida.close()


if __name__ == '__main__':
    cap_9()
