# Foydalanuvchidan 5 ta son olib, eng kattasini aniqlang

template = "{i}-sonni kiriting: "
max = int(input("1-Sonni kiriting: "))

for i in range(2, 6):

   b = int(input(template.format(i = i)))
   if b > max:
      max = b

print(max)