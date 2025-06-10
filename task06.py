# Kiritilgan so‘zda nechta gap borligini aniqlang
# Siz for bilan nechta . borligini sanab gaplar sonini aniqlang.

text = input("Matn kiriting: ")
dot = "."
total = 0

for letter in text:
    if letter == dot:
        total += 1
if total == 0:
    print(f"So'z 1 ta gapdan tashkil topgan")

else:
    print(f"So'z {total} ta gapdan tashkil topgan")

# Agar foydalanuvchi gapni oxirni ... 3 nuqta bilan tugatsa buni qanday aniqlab olamiz 3 ta gap emasligini?