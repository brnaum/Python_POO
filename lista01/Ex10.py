# Implemente um sistema em Python para representar personagens do universo dos Cavaleiros do Zodíaco, utilizando herança múltipla. Crie uma classe Personagem com os atributos nome e constelacao, e métodos como apresentar(). Crie também duas classes auxiliares: CavaleiroDeBronze com o atributo poder_de_luta e um método golpe_especial(), e CavaleiroDeOuro com o atributo casa_do_zodiaco e um método defender_casa(). Em seguida, implemente a classe CavaleiroHibrido, que herda tanto de CavaleiroDeBronze quanto de CavaleiroDeOuro, combinando os comportamentos de ambas. O programa deve oferecer um menu interativo no console com as opções de cadastrar personagens, listar todos os personagens, executar os golpes especiais ou defesas, e encerrar o programa. Explore o uso da herança múltipla e do polimorfismo para definir o comportamento de cada tipo de cavaleiro.

class Personagem:
    def __init__(self, nome, constelacao):
        self.__nome = nome
        self.__constelacao = constelacao

    def get_nome(self):
        return self.__nome

    def get_constelacao(self):
        return self.__constelacao

    def set_nome(self, nome):
        self.__nome = nome

    def set_constelacao(self, constelacao):
        self.__constelacao = constelacao

    def apresentar(self):
        print(f"Nome: {self.__nome}")
        print(f"Constelação: {self.__constelacao}")


class CavaleiroDeBronze(Personagem):
    def __init__(self, nome, constelacao, poder_de_luta):
        super().__init__(nome, constelacao)
        self.__poder_de_luta = poder_de_luta

    def get_poder_de_luta(self):
        return self.__poder_de_luta

    def golpe_especial(self):
        print(f"{self.get_nome()} utilizou seu golpe especial!")
        print(f"Poder de luta: {self.__poder_de_luta}")


class CavaleiroDeOuro(Personagem):
    def __init__(self, nome, constelacao, casa_do_zodiaco):
        super().__init__(nome, constelacao)
        self.__casa_do_zodiaco = casa_do_zodiaco

    def get_casa_do_zodiaco(self):
        return self.__casa_do_zodiaco

    def defender_casa(self):
        print(f"{self.get_nome()} está defendendo a Casa de {self.__casa_do_zodiaco}!")


class CavaleiroHibrido(CavaleiroDeBronze, CavaleiroDeOuro):
    def __init__(self, nome, constelacao, poder_de_luta, casa_do_zodiaco):
        Personagem.__init__(self, nome, constelacao)
        self.__poder_de_luta = poder_de_luta
        self.__casa_do_zodiaco = casa_do_zodiaco

    def golpe_especial(self):
        print(f"{self.get_nome()} realizou um golpe híbrido!")
        print(f"Poder de luta: {self.__poder_de_luta}")

    def defender_casa(self):
        print(f"{self.get_nome()} protege a Casa de {self.__casa_do_zodiaco}!")



personagens = []

while True:
    print("\n===== CAVALEIROS DO ZODÍACO =====")
    print("1 - Cadastrar personagem")
    print("2 - Listar personagens")
    print("3 - Executar ações")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n1 - Cavaleiro de Bronze")
        print("2 - Cavaleiro de Ouro")
        print("3 - Cavaleiro Híbrido")

        tipo = input("Escolha o tipo: ")

        nome = input("Nome: ")
        constelacao = input("Constelação: ")

        if tipo == "1":
            poder = int(input("Poder de luta: "))
            personagens.append(CavaleiroDeBronze(nome, constelacao, poder))
            print("Cavaleiro de Bronze cadastrado!")

        elif tipo == "2":
            casa = input("Casa do Zodíaco: ")
            personagens.append(CavaleiroDeOuro(nome, constelacao, casa))
            print("Cavaleiro de Ouro cadastrado!")

        elif tipo == "3":
            poder = int(input("Poder de luta: "))
            casa = input("Casa do Zodíaco: ")
            personagens.append(CavaleiroHibrido(nome, constelacao, poder, casa))
            print("Cavaleiro Híbrido cadastrado!")

        else:
            print("Tipo inválido!")

    elif opcao == "2":
        if len(personagens) == 0:
            print("Nenhum personagem cadastrado.")
        else:
            print("\n===== PERSONAGENS =====")
            for personagem in personagens:
                personagem.apresentar()
                print("-" * 30)

    elif opcao == "3":
        if len(personagens) == 0:
            print("Nenhum personagem cadastrado.")
        else:
            print("\n===== AÇÕES =====")
            for personagem in personagens:
                personagem.apresentar()

                if isinstance(personagem, CavaleiroDeBronze):
                    personagem.golpe_especial()

                if isinstance(personagem, CavaleiroDeOuro):
                    personagem.defender_casa()

                print("-" * 30)

    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")