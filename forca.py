#Funções
import random

#Para adicionar palavras ao jogo
# adc_palavra = open("palavras.txt", "a")
# adc_palavra.write("limao \n")

#Código 
file = open('palavras.txt', 'r')
palavras = []

for linha in file:
    linha = linha.strip()
    palavras.append(linha)

file.close()
numero = random.randrange(0, len(palavras))
palavra_secreta = palavras[numero].upper()
letras_chutadas = []
chances = len(palavra_secreta)
ganhou = False


while True:
    for letra in palavra_secreta:
        if letra in letras_chutadas:
            print(letra, end= " ")
        else:
            print('_', end=" ")
    print(f"Você tem {chances} chances")
    print("")
    chute = input("Escolha uma letra: ")
    chute = chute.strip().upper()
    letras_chutadas.append(chute)    
    if chute not in palavra_secreta:
        chances -= 1
    ganhou = True
    for letra in palavra_secreta:
        if letra not in letras_chutadas:
            ganhou = False
    if chances == 0 or ganhou:
        break
if ganhou:
    print(f"Parabéns você ganhou! A palavra era {palavra_secreta}")
else:
    print(f"Você perdeu, a palavra era {palavra_secreta}")
