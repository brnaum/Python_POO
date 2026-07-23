# No universo de Dragon Ball, desenvolva um sistema em Python para simular um torneio de artes marciais, utilizando orientação a objetos. Crie uma classe totalmente abstrata um método abstrato chamada Lutador, contendo apenas métodos abstratos para obter o nome do lutador, o nível de poder e realizar um ataque. Em seguida, implemente subclasses como Saiyajin, Androide e Namekuseijin, cada uma com um comportamento específico ao atacar. O sistema deve conter um menu interativo que permita cadastrar lutadores de diferentes raças, listar todos os lutadores inscritos no torneio e simular ataques, demonstrando o uso de herança, abstração total e polimorfismo. Implemente também tratamento de exceções, garantindo que os nomes não estejam vazios e que o nível de poder seja um valor numérico positivo.

from abc import ABC, abstractmethod

class Lutador(ABC):

    @abstractmethod
    def get_nome(self):
        pass

    @abstractmethod
    def get_nivel_poder(self):
        pass

    @abstractmethod
    def atacar(self):
        pass

class Saiyajin(Lutador):
    def __init__(self, nome, nivel_poder):
        self.__nome = nome
        self.__nivel_poder = nivel_poder

    def get_nome(self):
        return self.__nome

    def get_nivel_poder(self):
        return self.__nivel_poder

    def atacar(self):
        print(f"{self.__nome} lançou um Kamehameha!")
        print(f"Nível de poder: {self.__nivel_poder}")

class Androide(Lutador):
    def __init__(self, nome, nivel_poder):
        self.__nome = nome
        self.__nivel_poder = nivel_poder

    def get_nome(self):
        return self.__nome

    def get_nivel_poder(self):
        return self.__nivel_poder

    def atacar(self):
        print(f"{self.__nome} disparou um Canhão de Energia!")
        print(f"Nível de poder: {self.__nivel_poder}")

class Namekuseijin(Lutador):
    def __init__(self, nome, nivel_poder):
        self.__nome = nome
        self.__nivel_poder = nivel_poder

    def get_nome(self):
        return self.__nome

    def get_nivel_poder(self):
        return self.__nivel_poder

    def atacar(self):
        print(f"{self.__nome} utilizou o Canhão Especial!")
        print(f"Nível de poder: {self.__nivel_poder}")


lutadores = []

while True:
    print("\n====== TORNEIO DRAGON BALL ======")
    print("1 - Cadastrar Lutador")
    print("2 - Listar Lutadores")
    print("3 - Simular Ataques")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print("\n1 - Saiyajin")
        print("2 - Androide")
        print("3 - Namekuseijin")

        tipo = input("Escolha a raça: ")

        try:
            nome = input("Nome: ")

            if nome.strip() == "":
                raise ValueError("O nome não pode estar vazio.")

            nivel = float(input("Nível de poder: "))

            if nivel <= 0:
                raise ValueError("O nível de poder deve ser positivo.")

            if tipo == "1":
                lutadores.append(Saiyajin(nome, nivel))
                print("Saiyajin cadastrado com sucesso!")

            elif tipo == "2":
                lutadores.append(Androide(nome, nivel))
                print("Androide cadastrado com sucesso!")

            elif tipo == "3":
                lutadores.append(Namekuseijin(nome, nivel))
                print("Namekuseijin cadastrado com sucesso!")

            else:
                print("Tipo inválido.")

        except ValueError as erro:
            print("Erro:", erro)

    elif opcao == "2":

        if len(lutadores) == 0:
            print("Nenhum lutador cadastrado.")

        else:
            print("\n===== LUTADORES =====")

            for lutador in lutadores:
                print(f"Nome: {lutador.get_nome()}")
                print(f"Nível de Poder: {lutador.get_nivel_poder()}")
                print("-" * 30)

    elif opcao == "3":

        if len(lutadores) == 0:
            print("Nenhum lutador cadastrado.")

        else:
            print("\n===== ATAQUES =====")

            for lutador in lutadores:
                lutador.atacar()
                print("-" * 30)

    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")