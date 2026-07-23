# Desenvolva um sistema para gerenciar veículos de transporte público em uma cidade inteligente. Crie uma classe abstrata VeiculoTransporte, com os atributos placa e capacidadePassageiros, e calcularCustoOperacional() que retorna o custo por quilômetro. Crie as subclasses Onibus, com o atributo consumoPorKm (litros/km), e Metro, com consumoEnergiaPorKm (kWh/km). Cada uma deve implementar o cálculo do custo com valores fictícios: R$ 6,00 por litro de diesel e R$ 0,80 por kWh. Na função principal, permita criar objetos dos dois tipos e exibir os custos operacionais usando polimorfismo. Implemente tratamento de exceções para validar os dados de entrada: placa não pode ser vazia, e os valores numéricos devem ser positivos.

from abc import ABC, abstractmethod


class VeiculoTransporte(ABC):
    def __init__(self, placa, capacidade_passageiros):
        self.__placa = placa
        self.__capacidade_passageiros = capacidade_passageiros

    def get_placa(self):
        return self.__placa

    def get_capacidade_passageiros(self):
        return self.__capacidade_passageiros

    def set_placa(self, placa):
        self.__placa = placa

    def set_capacidade_passageiros(self, capacidade):
        self.__capacidade_passageiros = capacidade

    @abstractmethod
    def calcularCustoOperacional(self):
        pass


class Onibus(VeiculoTransporte):
    def __init__(self, placa, capacidade_passageiros, consumo_por_km):
        super().__init__(placa, capacidade_passageiros)
        self.__consumo_por_km = consumo_por_km

    def calcularCustoOperacional(self):
        return self.__consumo_por_km * 6.00


class Metro(VeiculoTransporte):
    def __init__(self, placa, capacidade_passageiros, consumo_energia_por_km):
        super().__init__(placa, capacidade_passageiros)
        self.__consumo_energia_por_km = consumo_energia_por_km

    def calcularCustoOperacional(self):
        return self.__consumo_energia_por_km * 0.80



veiculos = []

while True:
    print("\n===== TRANSPORTE PÚBLICO =====")
    print("1 - Cadastrar Ônibus")
    print("2 - Cadastrar Metrô")
    print("3 - Mostrar custos operacionais")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        try:
            placa = input("Placa: ")

            if placa.strip() == "":
                raise ValueError("A placa não pode estar vazia.")

            capacidade = int(input("Capacidade de passageiros: "))

            if capacidade <= 0:
                raise ValueError("A capacidade deve ser positiva.")

            consumo = float(input("Consumo (litros/km): "))

            if consumo <= 0:
                raise ValueError("O consumo deve ser positivo.")

            onibus = Onibus(placa, capacidade, consumo)
            veiculos.append(onibus)

            print("Ônibus cadastrado com sucesso!")

        except ValueError as erro:
            print("Erro:", erro)

    elif opcao == "2":
        try:
            placa = input("Placa: ")

            if placa.strip() == "":
                raise ValueError("A placa não pode estar vazia.")

            capacidade = int(input("Capacidade de passageiros: "))

            if capacidade <= 0:
                raise ValueError("A capacidade deve ser positiva.")

            consumo = float(input("Consumo de energia (kWh/km): "))

            if consumo <= 0:
                raise ValueError("O consumo deve ser positivo.")

            metro = Metro(placa, capacidade, consumo)
            veiculos.append(metro)

            print("Metrô cadastrado com sucesso!")

        except ValueError as erro:
            print("Erro:", erro)

    elif opcao == "3":
        if len(veiculos) == 0:
            print("Nenhum veículo cadastrado.")
        else:
            print("\n===== CUSTOS OPERACIONAIS =====")
            for veiculo in veiculos:
                print(f"Placa: {veiculo.get_placa()}")
                print(f"Capacidade: {veiculo.get_capacidade_passageiros()} passageiros")
                print(f"Custo por km: R$ {veiculo.calcularCustoOperacional():.2f}")
                print("-" * 30)

    elif opcao == "0":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")