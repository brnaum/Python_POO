# Desenvolva uma classe Departamento com nome e um vetor de objetos Funcionario, onde cada funcionário tem nome e salário, permitindo que funcionários existam independentemente do departamento para que possam ser adicionados ou removidos livremente (agregação). Implemente métodos no Departamento para adicionar funcionários, calcular a média salarial e listar todos os funcionários. Crie um programa com menu interativo no console que permita criar departamentos, criar funcionários, adicionar funcionários a departamentos, listar funcionários e mostrar a média salarial, além de permitir sair do programa

class Funcionario:
    def __init__(self, nome, salario):
        self.__nome = nome
        self.__salario = salario

    def get_nome(self):
        return self.__nome

    def get_salario(self):
        return self.__salario

    def set_nome(self, nome):
        self.__nome = nome

    def set_salario(self, salario):
        if salario >= 0:
            self.__salario = salario
        else:
            print("Salário inválido!")


class Departamento:
    def __init__(self, nome):
        self.__nome = nome
        self.__funcionarios = []

    def get_nome(self):
        return self.__nome

    def adicionar_funcionario(self, funcionario):
        self.__funcionarios.append(funcionario)
        print("Funcionário adicionado ao departamento!")

    def remover_funcionario(self, nome):
        for funcionario in self.__funcionarios:
            if funcionario.get_nome().lower() == nome.lower():
                self.__funcionarios.remove(funcionario)
                print("Funcionário removido do departamento!")
                return

        print("Funcionário não encontrado.")

    def listar_funcionarios(self):
        if len(self.__funcionarios) == 0:
            print("Nenhum funcionário no departamento.")
            return

        print(f"\nFuncionários do departamento {self.__nome}:")
        for funcionario in self.__funcionarios:
            print(f"Nome: {funcionario.get_nome()} | Salário: R$ {funcionario.get_salario():.2f}")

    def calcular_media_salarial(self):
        if len(self.__funcionarios) == 0:
            return 0

        soma = 0
        for funcionario in self.__funcionarios:
            soma += funcionario.get_salario()

        return soma / len(self.__funcionarios)


funcionarios = []
departamentos = []

while True:
    print("\n========= MENU =========")
    print("1 - Criar departamento")
    print("2 - Criar funcionário")
    print("3 - Adicionar funcionário ao departamento")
    print("4 - Listar funcionários de um departamento")
    print("5 - Mostrar média salarial do departamento")
    print("6 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do departamento: ")
        departamento = Departamento(nome)
        departamentos.append(departamento)
        print("Departamento criado com sucesso!")

    elif opcao == "2":
        nome = input("Nome do funcionário: ")
        salario = float(input("Salário: R$ "))
        funcionario = Funcionario(nome, salario)
        funcionarios.append(funcionario)
        print("Funcionário criado com sucesso!")

    elif opcao == "3":
        if len(funcionarios) == 0 or len(departamentos) == 0:
            print("Cadastre pelo menos um departamento e um funcionário.")
        else:
            print("\nFuncionários:")
            for i in range(len(funcionarios)):
                print(f"{i+1} - {funcionarios[i].get_nome()}")

            indice_func = int(input("Escolha o funcionário: ")) - 1

            print("\nDepartamentos:")
            for i in range(len(departamentos)):
                print(f"{i+1} - {departamentos[i].get_nome()}")

            indice_dep = int(input("Escolha o departamento: ")) - 1

            if (0 <= indice_func < len(funcionarios)) and (0 <= indice_dep < len(departamentos)):
                departamentos[indice_dep].adicionar_funcionario(funcionarios[indice_func])
            else:
                print("Opção inválida.")

    elif opcao == "4":
        if len(departamentos) == 0:
            print("Nenhum departamento cadastrado.")
        else:
            for i in range(len(departamentos)):
                print(f"{i+1} - {departamentos[i].get_nome()}")

            indice = int(input("Escolha o departamento: ")) - 1

            if 0 <= indice < len(departamentos):
                departamentos[indice].listar_funcionarios()
            else:
                print("Departamento inválido.")

    elif opcao == "5":
        if len(departamentos) == 0:
            print("Nenhum departamento cadastrado.")
        else:
            for i in range(len(departamentos)):
                print(f"{i+1} - {departamentos[i].get_nome()}")

            indice = int(input("Escolha o departamento: ")) - 1

            if 0 <= indice < len(departamentos):
                media = departamentos[indice].calcular_media_salarial()
                print(f"Média salarial: R$ {media:.2f}")
            else:
                print("Departamento inválido.")

    elif opcao == "6":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")