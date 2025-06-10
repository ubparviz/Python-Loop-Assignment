# Random son topish o'yini 1 dn 20 gacha

from random import randint


number = randint(1, 20)
print(number)

attemtp = int(input("Sonni toping (1-20): "))

while attemtp != number:
    print("Xato")
    attemtp = int(input("Yana urunib ko'ring: "))

if attemtp == number:
    print("Topdingiz")