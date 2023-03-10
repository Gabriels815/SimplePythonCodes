from random import randrange as r

cartas = {0 : "Ás", 1 : "Um", 2 : "Dois", 3 : "Três", 4 : "Quatro", 5 : "Cinco", 6 : "Seis", 7 : "Sete", 8 : "Oito", 9 : "Nove",
           10 : "Dez", 11 : "Valete", 12 : "Rainha", 13 : "Rei"} 

naipes = {1 : "Paus", 2 : "Corações", 3 : "Espadas", 4 : "Ouros"}

def cartaRandom():
    cartaRandom = r(0, 14)
    nomeCarta = cartas.get(cartaRandom)
    return nomeCarta

def naipeRandom():
    naipeRandom = r(1, 5)
    nomeNaipe = naipes.get(naipeRandom)
    return nomeNaipe

def verSorte():
    entrada = input("Você quer saber qual sua carta da sorte! | [n] - não [s] - sim \n")
    if entrada == "n":
        print("Que bom, porque o destino é você quem faz! \n")
    elif entrada == "s":
        print("Sua carta é", cartaRandom(), "do naipe de", naipeRandom(), "\n")
    else:
        print("Não entendi sua resposta! \n")
    print("Nada disso importa, apenas viva sua vida!")

verSorte()