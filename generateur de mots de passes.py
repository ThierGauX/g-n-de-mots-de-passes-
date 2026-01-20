from random import randint

min = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
maj = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
chiffres = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
cara = ['!', '#', '$', '%', '&', '*', '+', ',', '-', '.', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~']

mot_de_passe = "" 

for i in range(16):
    n = randint(1, 4)
    if n == 1:
        mot_de_passe += min[randint(0, 25)]
    elif n == 2:
        mot_de_passe += maj[randint(0, 25)]
    elif n == 3:
        mot_de_passe += chiffres[randint(0, 9)]
    elif n == 4:
        mot_de_passe += cara[randint(0, len(cara) - 1)]

print(mot_de_passe)  
