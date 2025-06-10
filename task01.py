# Stringdagi unli harflarni sanang

text = input("Matn kiriting: ")

letter = "aeiouAEIOU"
total = 0

for i in text:
    if i.isalpha():
        if i in letter:
            total += 1

print("Unli harflar soni:", total)