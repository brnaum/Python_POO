# Faça um programa em Python orientado a objetos que, a partir de uma string digitada pelo usuário, imprima:
# ◦ O número de caracteres da string;
# ◦ A string com todas suas letras em maiúsculo;
# ◦ A string com todas suas letras em minúsculo;
# ◦ O número de vogais da string;
# ◦ Se a substring “IFB” aparece no texto (ignorando maiúsculas/minúsculas).

class AnáliseTexto:
    def __init__(self, texto):
        self.texto = texto
    def numero_caracteres(self):
        return len(self.texto)
    def maiusculas(self):
        return self.texto.upper()
    def minusculas(self):
        return self.texto.lower()
    def vogais(self):
        vogais = "aeiouAEIOU"
        contador = 0
        for letra in self.texto:
            if letra in vogais:
                contador = contador + 1
        return contador
    def verificar_ifb(self):
        return "ifb" in self.texto.lower()
    
texto = input("Digite uma palavra: ")
analisador = AnáliseTexto(texto)
print("Número de caracteres:", analisador.numero_caracteres())
print("Texto em Maiúsculo:", analisador.maiusculas())
print("Texto em Minúsculo:", analisador.minusculas())
print("Número de vogais:", analisador.vogais())
if analisador.verificar_ifb():
    print("A Substring 'IFB' aparece no texto.")
else:
    print("A Substring 'IFB' não aparece no texto.")