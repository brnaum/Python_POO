#  Desenvolva um sistema em Python para representar personagens de um jogo de RPG. Crie uma classe base chamada Personagem, com os atributos nome e nivel, e um método atacar() que imprime uma mensagem genérica de ataque. Em seguida, crie as subclasses Guerreiro e Mago. A classe Guerreiro deve possuir o atributo adicional forca e sobrescrever o método atacar() para exibir uma mensagem de ataque físico, enquanto a classe Mago deve ter o atributo mana e sobrescrever o método atacar() para representar um ataque mágico. Na classe principal, crie instâncias das três classes e invoque o método atacar() para demonstrar o uso de herança e polimorfismo em tempo de execução.

class Personagem:
    def __init__(self, nome, nivel):
        self.__nome = nome
        self.__nivel = nivel

    def get_nome(self):
        return self.__nome

    def get_nivel(self):
        return self.__nivel

    def set_nome(self, nome):
        self.__nome = nome

    def set_nivel(self, nivel):
        self.__nivel = nivel

    def atacar(self):
        print(f"{self.__nome} realizou um ataque.")


class Guerreiro(Personagem):
    def __init__(self, nome, nivel, forca):
        super().__init__(nome, nivel)
        self.__forca = forca

    def get_forca(self):
        return self.__forca

    def set_forca(self, forca):
        self.__forca = forca

    def atacar(self):
        print(f"{self.get_nome()} atacou com sua espada! Força: {self.__forca}")


class Mago(Personagem):
    def __init__(self, nome, nivel, mana):
        super().__init__(nome, nivel)
        self.__mana = mana

    def get_mana(self):
        return self.__mana

    def set_mana(self, mana):
        self.__mana = mana

    def atacar(self):
        print(f"{self.get_nome()} lançou uma magia! Mana: {self.__mana}")


personagem = Personagem("Aventureiro", 1)
guerreiro = Guerreiro("Thor", 10, 80)
mago = Mago("Merlin", 15, 150)

print("===== ATAQUES DOS PERSONAGENS =====")
personagem.atacar()
guerreiro.atacar()
mago.atacar()