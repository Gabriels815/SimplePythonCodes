from random import randrange as r

def adivinhaNumero():
    num = int(input("Digite um número de 1 a 10: "))
    if num < 1 or num > 10:
        print("Número fora dos limites propostos! Tente Novamente")
        adivinhaNumero()
    else:
        x = r(1,10)
        if x == num:
            print("O número que eu escolhi foi", x, ", enquanto o seu é", num, "\nConsegui adivinhar! ")
        else:
            print("O número que eu escolhi foi", x, ", enquanto o seu é", num, "\nNão consegui adivinhar! ")