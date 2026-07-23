# Elabore um programa em Python orientado a objetos que leia
# um número n (o número de termos de uma progressão
# aritmética), a1 (o primeiro termo da progressão) e r (razão) e
# escreva todos os termos dessa progressão, bem como a
# soma dos elementos (Fórmulas da P.A.: an = a1 + r x (n – 1) e
# S = n * (a1 + an) / 2).


class ProgressãoAritmética:
    def __init__(self, n, a1, r):
        self.n = n
        self.a1 = a1
        self.r = r
    def ultimo_termo(self):
        return self.a1 + self.r * (self.n - 1)
    def exibir_termos(self):
        print("Termos da Progressão Aritmética: ")
        for i in range(self.n):
            termo = self.a1 + self.r * i 
            print(termo)
    def soma(self):
        an = self.ultimo_termo()
        return self.n * (self.a1 + an) / 2
    
n = int(input("Digite o número de termos: "))
a1 = float(input("Digite o primeiro termo: "))
r = float(input("Digite a razão: "))
pa = ProgressãoAritmética(n, a1, r)
pa.exibir_termos()
print(f"Soma dos termos: {pa.soma()}")