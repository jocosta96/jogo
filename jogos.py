import forca
import adivinhacao
import dados

print("*********************************")
print("********Escolha seu jogo!********")
print("*********************************")

print("(1) Forca (2) Adivinhação (3) Dados")

jogo = int(input("Escolha seu jogo: "))

if(jogo == 1):
    print("Jogando Forca")
    forca.jogar()

elif(jogo == 2):
    print("Jogando Dados")
    dados.gameplay()

else:
    print("Jogando Adivinhação")
    adivinhacao.jogar()