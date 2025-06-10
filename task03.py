# So'zdagi katta harflarni sanang

text = input("Matn kiriting: ")

total = 0

for i in text:
    if i.isalpha() and i.isupper():
            total += 1

print("Unli harflar soni:", total)