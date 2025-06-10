# So'zdagi har bir harfni orqaga o'g'rish

text = input("So'z kiriting: ")
reverse = ""

for letter in text:
    reverse = letter + reverse

print(reverse)