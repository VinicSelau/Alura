print("*********************************")
print("       Escolha o seu jogo!       ")
print("*********************************")

print("(1) Adivinhação (2) Forca")

jogo = int(input("Qual jogo?"))

if(jogo == 1):
    print("Jogando Adivinhação")
    import adivinhacao
    adivinhacao.jogar()
elif(jogo == 2):
    print("Jogando Forca")
    import forca
    forca.jogar()
