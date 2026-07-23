# Implemente uma classe Impressora com o método imprimir(Documento d), que recebe um objeto da classe Documento e imprime suas informações na tela. A classe Documento deve conter os atributos título e conteúdo. A classe Impressora apenas utiliza o documento, sem manter uma referência permanente a ele, caracterizando uma relação de dependência. Desenvolva um programa com um menu interativo no console que permita criar vários documentos, visualizar seu conteúdo por meio da impressora e encerrar o programa.

class Documento:
    def __init__(self, titulo, conteudo):
        self.__titulo = titulo
        self.__conteudo = conteudo

    def get_titulo(self):
        return self.__titulo

    def get_conteudo(self):
        return self.__conteudo
    
    def set_titulo(self, titulo):
        self.__titulo = titulo

    def set_conteudo(self, conteudo):
        self.__conteudo = conteudo


class Impressora:
    def imprimir(self, documento):
        print("\n========== DOCUMENTO ==========")
        print(f"Título: {documento.get_titulo()}")
        print(f"Conteúdo:\n{documento.get_conteudo()}")
        print("===============================\n")

documentos = []
impressora = Impressora()

while True:
    print("\n===== MENU =====")
    print("1 - Criar documento")
    print("2 - Imprimir documento")
    print("3 - Listar documentos")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        titulo = input("Digite o título do documento: ")
        conteudo = input("Digite o conteúdo do documento: ")

        documento = Documento(titulo, conteudo)
        documentos.append(documento)

        print("Documento criado com sucesso!")

    elif opcao == "2":
        if len(documentos) == 0:
            print("Não há documentos cadastrados.")
        else:
            print("\nDocumentos disponíveis:")
            for i in range(len(documentos)):
                print(f"{i + 1} - {documentos[i].get_titulo()}")

            indice = int(input("Escolha o número do documento: ")) - 1

            if 0 <= indice < len(documentos):
                impressora.imprimir(documentos[indice])
            else:
                print("Documento inválido.")

    elif opcao == "3":
        if len(documentos) == 0:
            print("Não há documentos cadastrados.")
        else:
            print("\n===== DOCUMENTOS CADASTRADOS =====")
            for i in range(len(documentos)):
                print(f"{i + 1} - {documentos[i].get_titulo()}")

    elif opcao == "4":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")