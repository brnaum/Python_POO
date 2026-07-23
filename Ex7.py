# Implemente uma classe Casa que contenha vários objetos do tipo Comodo, sendo que cada cômodo possui nome (ex: sala, cozinha, banheiro) e área. Os cômodos devem ser implementados de forma que só existam se a casa existir (relação de composição), e não devem ser acessados ou manipulados diretamente de fora. Implemente um método na casa para calcular a área total, somando as áreas de todos os cômodos. Desenvolva um programa com menu interativo no console que permita criar uma casa, adicionar cômodos à casa, listar os cômodos da casa, calcular e exibir a área total da casa e encerrar o programa.

class Comodo:
    def __init__(self, nome, area):
        self.__nome = nome
        self.__area = area

    def get_nome(self):
        return self.__nome

    def get_area(self):
        return self.__area

    def set_nome(self, nome):
        self.__nome = nome

    def set_area(self, area):
        if area > 0:
            self.__area = area
        else:
            print("Área inválida!")


class Casa:
    def __init__(self):
        self.__comodos = []

    def adicionar_comodo(self, nome, area):
        comodo = Comodo(nome, area)
        self.__comodos.append(comodo)
        print("Cômodo adicionado com sucesso!")

    def listar_comodos(self):
        if len(self.__comodos) == 0:
            print("A casa não possui cômodos.")
            return

        print("\n===== CÔMODOS DA CASA =====")
        for comodo in self.__comodos:
            print(f"Nome: {comodo.get_nome()}")
            print(f"Área: {comodo.get_area()} m²")
            print("-" * 25)

    def calcular_area_total(self):
        total = 0

        for comodo in self.__comodos:
            total += comodo.get_area()

        return total


casa = Casa()

while True:
    print("\n====== MENU ======")
    print("1 - Adicionar cômodo")
    print("2 - Listar cômodos")
    print("3 - Calcular área total")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do cômodo: ")
        area = float(input("Área do cômodo (m²): "))

        casa.adicionar_comodo(nome, area)

    elif opcao == "2":
        casa.listar_comodos()

    elif opcao == "3":
        total = casa.calcular_area_total()
        print(f"\nÁrea total da casa: {total:.2f} m²")

    elif opcao == "4":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")