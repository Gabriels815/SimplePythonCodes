from random import randrange as r

def jogarMoeda():
    x = r(1,3)
    if x == 1:
        print("Cara!")
        return True
    else:
        print("Coroa!")
        return False

def testeDaVerdade():
    moeda1 = jogarMoeda()
    moeda2 = jogarMoeda()
    moeda3 = jogarMoeda()
    if moeda1 == True and moeda2 == True and moeda3 == True:
        print("Sorte Grande! ")
    else:
        print("Azar, azar!")

