#Crie um programa em Python utilizando orientação a objetos para gerenciar uma lista de produtos de um carrinho de compras. Implemente uma classe chamada Produto, com atributos privados (__nome, __preco e __quantidade) e métodos públicos para acessar e modificar esses valores de forma segura (getters e setters). Em seguida, implemente uma classe CarrinhoDeCompras, que mantém uma lista de objetos Produto e possui métodos para adicionar um produto ao carrinho, remover um produto pelo nome, calcular o valor total da compra e listar os produtos com suas quantidades e preços individuais. O programa principal deve permitir que o usuário adicione e remova produtos, visualize o conteúdo do carrinho e o total da compra. Utilize encapsulamento para proteger os dados dos produtos e boas práticas de organização orientada a objetos.

# para normalizar os textos (tirando acentos e não diferenciando maiúsculas de minúsculas)
import unicodedata
def normalizar(texto):
    texto = texto.strip().lower()
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )


class Produto:
    def __init__(self, nome, preco, quantidade):
        self.__nome = nome
        self.__preco = preco
        self.__quantidade = quantidade

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_quantidade(self):
        return self.__quantidade

    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        if preco >= 0:
            self.__preco = preco
        else:
            print("Preço inválido!")

    def set_quantidade(self, quantidade):
        if quantidade >= 0:
            self.__quantidade = quantidade
        else:
            print("Quantidade inválida!")

class CarrinhoDeCompras:
    def __init__(self):
        self.produtos = []

    def adicionar_produto(self, produto):
        self.produtos.append(produto)
        print("Produto adicionado com sucesso!")

    def remover_produto(self, nome):
        nome = normalizar(nome)
        for produto in self.produtos:
            if normalizar(produto.get_nome()) == nome:
                self.produtos.remove(produto)
                print("Produto removido com sucesso!")
                return
        print("Produto não encontrado.")

    def listar_produtos(self):
        if len(self.produtos) == 0:
            print("\nCarrinho vazio!")
            return

        print("\n===== PRODUTOS NO CARRINHO =====")
        for produto in self.produtos:
            print(f"Nome: {produto.get_nome()}")
            print(f"Preço: R$ {produto.get_preco():.2f}")
            print(f"Quantidade: {produto.get_quantidade()}")
            print("-" * 30)

    def calcular_total(self):
        total = 0
        for produto in self.produtos:
            total += produto.get_preco() * produto.get_quantidade()
        return total

carrinho = CarrinhoDeCompras()

while True:
    print("\n====== CARRINHO DE COMPRAS ======")
    print("1 - Adicionar produto")
    print("2 - Remover produto")
    print("3 - Listar produtos")
    print("4 - Mostrar valor total")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome do produto: ")
        preco = float(input("Preço: R$ "))
        quantidade = int(input("Quantidade: "))

        produto = Produto(nome, preco, quantidade)
        carrinho.adicionar_produto(produto)

    elif opcao == "2":
        nome = input("Digite o nome do produto que deseja remover: ")
        carrinho.remover_produto(nome)

    elif opcao == "3":
        carrinho.listar_produtos()

    elif opcao == "4":
        total = carrinho.calcular_total()
        print(f"\nValor total da compra: R$ {total:.2f}")

    elif opcao == "5":
        print("Programa encerrado!")
        break

    else:
        print("Opção inválida!")