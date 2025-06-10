# Foydalanuvchidan bir son oling (n). 1 dan n gacha bo‘lgan sonlar uchun quyidagi qoidalarni bajaring:

# Agar son 3 ga bo‘linsa: Fizz deb yozing.
# Agar son 5 ga bo‘linsa: Buzz
# Agar 3 va 5 ga bo‘linsa: FizzBuzz
# Aks holda — o‘zini yozing.


number = int(input("Son kiriting: "))

if number <= 1:
    print("Iltimos 1 dan katta son kiriting")

else:
    for son in range(1, number+1):
        if son % 5 == 0 and son % 3 == 0:
            print("FizzBuzz")

        elif son % 3 == 0:
            print("Fizz")

        elif son % 5 == 0:
            print("Buzz")
    
        else:
            print(son)