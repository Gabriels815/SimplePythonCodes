import random

characters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
              'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 
              'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 
              'W', 'X', 'Y', 'Z', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0', '@', '!', 
              '#', '$', '%', '&']

def gerarSenha():
    password = ""
    num = int(input("Digite o tamanho de caracteres de sua senha (min 8, max 16): "))
    if num < 8 or num > 16:
        print("Número fora dos limites! \nTente Novamente! ")
    else:
        print("Digito não identificado!")
    if num >= 8 or num <= 16:
        for x in range(num):
            password = password + random.choices(characters)[0]
        print("Sua senha gerada aleatoriamente: ", password)
    return password

gerarSenha()
