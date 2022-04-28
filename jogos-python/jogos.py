import imp
import forca
import adivinhacao

print("********************************\n")
print("        Escolha seu Jogo\n"          )
print("*********************************\n")

print ("(1) Forca \n(2) Adivinhação")
jogo = int (input("Qual Jogo?\n"))

if(jogo == 1):
    print("Jogando Forca !\n")
    forca.jogar()
elif(jogo == 2):
    print("Jogando Adivinhação !\n")
    adivinhacao.jogar()
