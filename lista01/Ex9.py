# Implemente em Python um sistema para uma plataforma de cursos online que utilize herança e polimorfismo, armazenando os dados em uma lista. Crie uma classe base chamada Participante, com os atributos nome e email, e um método emitirCertificado() que retorna uma mensagem genérica. Em seguida, crie as subclasses Aluno, com o atributo curso, e Instrutor, com o atributo especialidade, ambas sobrescrevendo o método emitirCertificado() com mensagens específicas: o aluno recebe um certificado de conclusão do curso e o instrutor um certificado de participação como palestrante. O programa deve conter um menu com as opções: 1) Cadastrar participante, 2) Listar participantes, 3) Emitir certificados, e 0) Sair. O usuário deve escolher entre cadastrar um aluno ou instrutor, e os dados devem ser armazenados em uma lista de objetos do tipo Participante. O método emitirCertificado() deve ser chamado de forma polimórfica para cada participante cadastrado.

class Participante:
    def __init__(self, nome, email):
        self.__nome = nome
        self.__email = email

    def get_nome(self):
        return self.__nome

    def get_email(self):
        return self.__email

    def set_nome(self, nome):
        self.__nome = nome

    def set_email(self, email):
        self.__email = email

    def emitirCertificado(self):
        return f"Certificado emitido para {self.__nome}."


class Aluno(Participante):
    def __init__(self, nome, email, curso):
        super().__init__(nome, email)
        self.__curso = curso

    def get_curso(self):
        return self.__curso

    def set_curso(self, curso):
        self.__curso = curso

    def emitirCertificado(self):
        return f"Certificado de conclusão do curso '{self.__curso}' emitido para o aluno {self.get_nome()}."


class Instrutor(Participante):
    def __init__(self, nome, email, especialidade):
        super().__init__(nome, email)
        self.__especialidade = especialidade

    def get_especialidade(self):
        return self.__especialidade

    def set_especialidade(self, especialidade):
        self.__especialidade = especialidade

    def emitirCertificado(self):
        return f"Certificado de participação como palestrante na especialidade '{self.__especialidade}' emitido para o instrutor {self.get_nome()}."



participantes = []

while True:
    print("\n===== PLATAFORMA DE CURSOS =====")
    print("1 - Cadastrar participante")
    print("2 - Listar participantes")
    print("3 - Emitir certificados")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        print("\n1 - Aluno")
        print("2 - Instrutor")

        tipo = input("Escolha o tipo de participante: ")

        nome = input("Nome: ")
        email = input("E-mail: ")

        if tipo == "1":
            curso = input("Curso: ")
            aluno = Aluno(nome, email, curso)
            participantes.append(aluno)
            print("Aluno cadastrado com sucesso!")

        elif tipo == "2":
            especialidade = input("Especialidade: ")
            instrutor = Instrutor(nome, email, especialidade)
            participantes.append(instrutor)
            print("Instrutor cadastrado com sucesso!")

        else:
            print("Tipo inválido!")

    elif opcao == "2":
        if len(participantes) == 0:
            print("Nenhum participante cadastrado.")
        else:
            print("\n===== PARTICIPANTES =====")
            for participante in participantes:
                print(f"Nome: {participante.get_nome()}")
                print(f"E-mail: {participante.get_email()}")
                print("-" * 30)

    elif opcao == "3":
        if len(participantes) == 0:
            print("Nenhum participante cadastrado.")
        else:
            print("\n===== CERTIFICADOS =====")
            for participante in participantes:
                print(participante.emitirCertificado())

    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")