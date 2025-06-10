# PIN kod ochish o‘yini

from random import randint

PIN = randint(1000, 9999)

attempts = 0

print("4 xonali maxfiy raqam yaratdi")
print("7 urunishda topib ko'ring")

while attempts < 7:
    answer = input(f"{attempts + 1}-urinish: PIN kodni kiriting: ")
    

    if not answer.isdigit() or len(answer) != 4:
        print("Faqat 4 xonali raqam kiriting.")
        continue
    
    answer = int(answer)
    attempts += 1

    if answer == PIN:
        print("Tabriklaymiz, topdingiz!")
        break
    elif answer > PIN:
        print("Juda katta son!")
    else:
        print("Juda kichik son!")

else:
    print("Topolmadiz")
    print(f"To'g'ri javob: {PIN}")
