# Raqamdagi raqamlar yig'indisini hisoblang

number = int(input("Raqam kiriting: "))

number = str(number)
total = 0

for n in number:
    total += int(n)

print(total)