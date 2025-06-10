# Foydalanuvchidan 3 marta input() bilan parol so‘raysiz. 
# To‘g‘ri kiritmasa → “Yana urinib ko‘ring” 3 martadan keyin → “Bloklandiz

parol = "12345678"

attempt = 0

while attempt < 3:

    user_input = input("Parolni kiriting: ")

    if user_input == parol:
        print("Xush kelibsiz!")
        break

    else:
        attempt += 1
        if attempt < 3:
            print("Yana urinib ko‘ring")
            
        else:
            print("Bloklandiz")
