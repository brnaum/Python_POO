# Faça um programa em Python orientado a objetos que receba
# uma frase dada pelo usuário e a criptografe. A criptografia
# consistirá na troca das vogais da frase por um número
# correspondente: A – 4, E – 3, I – 1, O – 0, U – 8.

class Criptografia: 
    def __init__(self, frase):
        self.frase = frase 
    def criptografar(self):
        texto = self.frase
        texto = texto.replace("A", "4").replace("a", "4")
        texto = texto.replace("E", "3").replace("e", "3")
        texto = texto.replace("I", "1").replace("i", "1")
        texto = texto.replace("O", "0").replace("o", "0")
        texto = texto.replace("U", "8").replace("u", "8")
        return texto

texto = input("Digite uma frase: ")
cripto = Criptografia(texto)
print("Frase Criptografada:")
print(cripto.criptografar())