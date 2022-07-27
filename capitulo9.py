import sys
import random
import os.path

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
                arquivo_saida.write(
                    f"-------------------Pagina {pagina}-----------------\n")
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
                        arquivo_saida.write(
                            f"-----------------Pagina {pagina}------------------\n")
                        pagina += 1
                        qtd_linhas = 0
                    tamanho_linha = len(linha)
            arquivo_saida.write(linha)
            qtd_linhas += 1
            if qtd_linhas == LINHAS:
                arquivo_saida.write(
                    f"-------------------Pagina {pagina}-----------------\n")
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

    def ex_11():
        nome_do_arquivo = sys.argv[1]
        arquivo = open(nome_do_arquivo, "r")
        dicionario_palavras = {}

        for linha in arquivo.readlines():
            lista_palavras = linha.split()
            for i in lista_palavras:
                if i in dicionario_palavras:
                    dicionario_palavras[i] += 1
                else:
                    dicionario_palavras[i] = 1

        print(dicionario_palavras)
        arquivo.close()

    def ex_13():
        nome_do_arquivo = sys.argv[1]
        arquivo = open(nome_do_arquivo, "r")

        inicio = int(input("Digita o número da linha de início: "))
        fim = int(input("Digita o número da linha de fim: "))

        contador = 0

        for linha in arquivo.readlines():
            contador += 1
            if contador >= inicio and contador <= fim:
                print(linha)
        arquivo.close()

    def ex_15():
        nome_do_jogador = input("Digite o nome do jogador: ").title().strip()
        if len(nome_do_jogador) == 0:
            print("Não foi informado o nome do jogador")
            nome_do_jogador = "Jogador"
        palavras = []
        nome_do_arquivo = sys.argv[1]
        arquivo = open(nome_do_arquivo, "r")
        for linha in arquivo.readlines():
            lista_palavras = linha.split()
            for i in lista_palavras:
                if i not in palavras:
                    palavras.append(i)
        random.shuffle(palavras)
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
                arquivo_ranking = open("ranking.txt", "a")
                arquivo_ranking.write(f"{nome_do_jogador} ")
                arquivo_ranking.close()
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

        coletar_ranking = open("ranking.txt", "r")
        dicionario_nomes = {}
        for linha in coletar_ranking.readlines():
            lista_nomes = linha.split()
            for i in lista_nomes:
                if i not in dicionario_nomes:
                    dicionario_nomes[i] = 1
                else:
                    dicionario_nomes[i] += 1
        coletar_ranking.close()
        print("RANKING:")
        if len(dicionario_nomes) < 5:
            for i in dicionario_nomes:
                print(f"{i} - {dicionario_nomes[i]}")
        else:
            lista_pontos = []
            for nome, pontos in dicionario_nomes.items():
                lista_pontos.append(pontos)
            lista_pontos.sort(reverse=True)

            primeiro_lugar = lista_pontos[0]
            segundo_lugar = lista_pontos[1]
            terceiro_lugar = lista_pontos[2]
            quarto_lugar = lista_pontos[3]
            quinto_lugar = lista_pontos[4]

            for nome, pontos in dicionario_nomes.items():
                if pontos == lista_pontos[0]:
                    primeiro_lugar = nome, pontos
                elif pontos == lista_pontos[1]:
                    segundo_lugar = nome, pontos
                elif pontos == lista_pontos[2]:
                    terceiro_lugar = nome, pontos
                elif pontos == lista_pontos[3]:
                    quarto_lugar = nome, pontos
                elif pontos == lista_pontos[4]:
                    quinto_lugar = nome, pontos

            print(
                f"Primeiro lugar: {primeiro_lugar[0]} - {primeiro_lugar[1]} Pontos")
            print(
                f"Segundo lugar: {segundo_lugar[0]} - {segundo_lugar[1]} Pontos")
            print(
                f"Terceiro lugar: {terceiro_lugar[0]} - {terceiro_lugar[1]} Pontos")
            print(
                f"Quarto lugar: {quarto_lugar[0]} - {quarto_lugar[1]} Pontos")
            print(
                f"Quinto lugar: {quinto_lugar[0]} - {quinto_lugar[1]} Pontos")

        coletar_ranking.close()

    
    def ex_16():
        agenda = []
        def pede_nome():
            return(input("Nome: "))
        def pede_telefone():
            return(input("Telefone: "))
        def pede_email():
            return(input("Email: "))
        def pede_nome_arquivo():
            return(input("Nome do arquivo: "))
        def mostra_dados(nome, telefone, email):
            print("Nome: %s Telefone: %s Email: %s" % (nome, telefone, email))
        def cadastra():
            nome = pede_nome()
            telefone = pede_telefone()
            email = pede_email()
            agenda.append([nome, telefone, email])
        def le():
            nome_arquivo = pede_nome_arquivo()
            arquivo = open(nome_arquivo, "r")
            for linha in arquivo.readlines():
                nome, telefone, email = linha.split("#")
                agenda.append([nome, telefone, email])
            arquivo.close()
        def remove():
            nome = pede_nome()
            for contato in agenda:
                if contato[0] == nome:
                    agenda.remove(contato)
        def altera():
            nome = pede_nome()
            for contato in agenda:
                if contato[0] == nome:
                    contato[0] = pede_nome()
                    contato[1] = pede_telefone()
                    contato[2] = pede_email()
                    
        def lista():
            print("Lista de contatos")
            for contato in agenda:
                mostra_dados(contato[0], contato[1], contato[2])
        def grava():
            nome_arquivo = pede_nome_arquivo()
            arquivo = open(nome_arquivo, "a")
            for contato in agenda:
                arquivo.write("%s %s %s\n" % (contato[0], contato[1], contato[2]))
            arquivo.close()
        def valida_nome(nome):
            if nome == "0":
                return False
            if not nome.isalpha():
                return False
            return True
        def valida_telefone(telefone):
            if len(telefone) != 9:
                return False
            if not telefone.isdigit():
                return False
            return True
        def valida_email(email):
            if '@' not in email:
                return False
            if '.' not in email:
                return False
            return True
        def valida_dados(nome, telefone, email):
            if valida_nome(nome) and valida_telefone(telefone) and valida_email(email):
                return True
            return False
        def menu():
            print("""
--- MENU ---
1 - Cadastrar
2 - Alterar
3 - Remover
4 - Listar
5 - Gravar
6 - Ler
0 - Sair
""")
        def run():
            while True:
                menu()
                opcao = int(input("Digite sua opção: "))
                if opcao == 1:
                    cadastra()
                elif opcao == 2:
                    altera()
                elif opcao == 3:
                    remove()
                elif opcao == 4:
                    lista()
                elif opcao == 5:
                    grava()
                elif opcao == 6:
                    le()
                elif opcao == 0:
                    break
                else:
                    print("Opção inválida")
        run()

    
    def ex_29():
        filmes = {
            "drama": ["Cidadão Kane", "O Poderoso Chefão"],
            "comedia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
            "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
            "guerra": ["Rambo", "Platoon","Tora!Tora!Tora!"],
        }
        pagina = open("filmes.html", "w", encoding='utf-8')
        pagina.write("""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="utf-8">
            <title>Filmes</title>
        </head>
        <body>
        """)
        for c, v in filmes.items():
            pagina.write(f"<h1>{c}</h1>")
            for i in v:
                pagina.write(f"<p>{i}</p>")
        pagina.write("""
        </body>
        </html>
        """)
        pagina.close()


    def ex_30():
        filmes = {
            "drama": ["Cidadão Kane", "O Poderoso Chefão"],
            "comedia": ["Tempos Modernos", "American Pie", "Dr. Dolittle"],
            "policial": ["Chuva Negra", "Desejo de Matar", "Difícil de Matar"],
            "guerra": ["Rambo", "Platoon","Tora!Tora!Tora!"],
        }
        pagina = open("filmes.html", "w", encoding='utf-8')
        pagina.write("""
        <!DOCTYPE html>
        <html lang="pt-br">
        <head>
            <meta charset="utf-8">
            <title>Filmes</title>
        </head>
        <body>
        <h1>Filmes</h1>
        """)
        for c, v in filmes.items():
            pagina.write(f"<h2>{c}</h2>")
            pagina.write("<ul>")
            for i in v:
                pagina.write(f"<li>{i}</li>")
            pagina.write("</ul>")
        pagina.write("""
        </body>
        </html>
        """)
        pagina.close()


    def ex_31():
        if os.path.exists("z"):
            if os.path.isdir("z"):
                print("É um diretório")
            else:
                print("É um arquivo")
        else:
            print("Não existe")
    
    def ex_32():
        nome = sys.argv[1]
        if os.path.exists(nome):
            if os.path.isdir(nome):
                print("É um diretório")
            else:
                print("É um arquivo")
        else:
            print("Não existe")

    def ex_33():
        nome_diretorio = sys.argv[1]
        if os.path.exists(nome_diretorio) and os.path.isdir(nome_diretorio):
            pagina = open("index.html", "w", encoding='utf-8')
            pagina.write("""
            <!DOCTYPE html>
            <html lang="pt-br">
            <head>
                <meta charset="utf-8">
                <tittle>links para arquivos de imagens</title>
            </head>
            <body>
            """)
            for arquivo in os.listdir(nome_diretorio):
                if arquivo.endswith(".png"):
                    pagina.write(f"<img src='{arquivo}'><br>")
            pagina.write("""
            </body>
            </html>
            """)
            pagina.close()
        else:
            print("Não existe")
        
    

if __name__ == '__main__':
    cap_9()
