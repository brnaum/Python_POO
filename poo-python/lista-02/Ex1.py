# Implemente um sistema de gerenciamento de cursos e alunos em Python, utilizando orientação a objetos. O sistema deve funcionar por meio de um menu interativo e permitir as seguintes operações:
# Listar todos os alunos cadastrados.
# Listar todos os cursos cadastrados.
# Matricular um aluno em um curso.
# Exibir em quais cursos um aluno está matriculado. Encerrar o programa.
# Os alunos e cursos já devem estar previamente cadastrados no início do programa. O usuário poderá escolher as opções pelo menu, realizar matrículas e consultar as informações desejadas. Cada aluno pode se matricular em vários cursos, e cada curso pode ter vários alunos.

class Aluno:
    def __init__(self, nome):
        self.__nome = nome
        self.__cursos = []

    def get_nome(self):
        return self.__nome

    def get_cursos(self):
        return self.__cursos

    def matricular(self, curso):
        if curso not in self.__cursos:
            self.__cursos.append(curso)


class Curso:
    def __init__(self, nome):
        self.__nome = nome
        self.__alunos = []

    def get_nome(self):
        return self.__nome

    def get_alunos(self):
        return self.__alunos

    def adicionar_aluno(self, aluno):
        if aluno not in self.__alunos:
            self.__alunos.append(aluno)


alunos = [
    Aluno("Bruno"),
    Aluno("Diego"),
    Aluno("Laura")
]

cursos = [
    Curso("Python"),
    Curso("Java"),
    Curso("Php")
]


while True:

    print("\n===== SISTEMA DE CURSOS =====")
    print("1 - Listar alunos")
    print("2 - Listar cursos")
    print("3 - Matricular aluno em um curso")
    print("4 - Mostrar cursos de um aluno")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":

        print("\n===== ALUNOS =====")
        for i in range(len(alunos)):
            print(f"{i+1} - {alunos[i].get_nome()}")

    elif opcao == "2":

        print("\n===== CURSOS =====")
        for i in range(len(cursos)):
            print(f"{i+1} - {cursos[i].get_nome()}")

    elif opcao == "3":

        print("\nEscolha um aluno:")

        for i in range(len(alunos)):
            print(f"{i+1} - {alunos[i].get_nome()}")

        indice_aluno = int(input("Aluno: ")) - 1

        print("\nEscolha um curso:")

        for i in range(len(cursos)):
            print(f"{i+1} - {cursos[i].get_nome()}")

        indice_curso = int(input("Curso: ")) - 1

        if (0 <= indice_aluno < len(alunos)) and (0 <= indice_curso < len(cursos)):

            aluno = alunos[indice_aluno]
            curso = cursos[indice_curso]

            aluno.matricular(curso)
            curso.adicionar_aluno(aluno)

            print("Matrícula realizada com sucesso!")

        else:
            print("Opção inválida!")

    elif opcao == "4":

        print("\nEscolha um aluno:")

        for i in range(len(alunos)):
            print(f"{i+1} - {alunos[i].get_nome()}")

        indice = int(input("Aluno: ")) - 1

        if 0 <= indice < len(alunos):

            aluno = alunos[indice]

            print(f"\nCursos de {aluno.get_nome()}:")

            if len(aluno.get_cursos()) == 0:
                print("O aluno não está matriculado em nenhum curso.")

            else:
                for curso in aluno.get_cursos():
                    print(curso.get_nome())

        else:
            print("Aluno inválido!")

    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")