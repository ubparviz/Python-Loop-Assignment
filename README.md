### 🧩 1. **Stringdagi unli harflarni sanang**

Foydalanuvchidan matn oling. `for` yordamida nechta unli harf (`a, e, i, o, u`) borligini aniqlang.
➡️ Masalan: `"hello world"` → `3`

---

### 🧩 2. **Raqamdagi raqamlar yig‘indisini hisoblang**

Foydalanuvchi `n` sonini kiritadi. Har bir raqamni ajratib, yig‘indisini toping.
➡️ Masalan: `345` → `3 + 4 + 5 = 12`

---

### 🧩 3. **So‘zdagi katta harflarni sanang**

Foydalanuvchi bir matn kiritadi. `for` orqali nechta katta harf (`A-Z`) borligini hisoblang.

---

### 🧩 4. **Random son topish o‘yini**

Kompyuter `1` dan `20` gacha tasodifiy son tanlaydi. Foydalanuvchi to‘g‘ri topmaguncha `input()` bilan qayta-qayta so‘raydi. To‘g‘ri topsa: “Topding!”
➡️ `random.randint()` ishlatilsin.

---

### 🧩 5. **So‘zdagi har bir harfni orqaga o‘girish**

Foydalanuvchi matn kiritadi. Siz uni harfma-harf teskari qilib chiqaring.
➡️ Masalan: `"salom"` → `"molas"`
(`for` yoki `while` bilan)

---

### 🧩 6. **Kiritilgan so‘zda nechta gap borligini aniqlang**

Matn kiriting: `"Men dasturchiman. Python yaxshi. Sen-chi?"`
→ 3 ta gap bor (nuqta orqali bo‘lingan).
Siz `for` bilan nechta `.` borligini sanab gaplar sonini aniqlang.

---

### 🧩 7. **Foydalanuvchidan 5 ta son olib, eng kattasini aniqlang**

Siz `for` orqali 5 marta `input()` orqali son olasiz va har safar eng kattasini tekshirib borasiz.

---

### 🧩 8. **Parol tasdiqlovchi**

Foydalanuvchidan 3 marta `input()` bilan parol so‘raysiz.
To‘g‘ri kiritmasa → “Yana urinib ko‘ring”
3 martadan keyin → “Bloklandiz”

---

### 🧠 Yangi: 9-mashq (Yangi topshiriq)

### 🔐 **PIN kod ochish o‘yini**

Kompyuter 4 xonali maxfiy raqam (PIN) yaratadi (`random.randint(1000, 9999)` bilan).
Foydalanuvchi bu raqamni topishga harakat qiladi. Har urinishda:

* Agar son **katta bo‘lsa**: “Juda katta son!”
* Agar son **kichik bo‘lsa**: “Juda kichik son!”
* Agar **to‘g‘ri topsa**: “Tabriklaymiz, topdingiz!”

Foydalanuvchiga maksimal 7 urinish beriladi.
**Ko‘nikma:** `while`, `if`, `input`, `random`, `count`, `break`, `else` — barchasi ishtirok etadi.

---

### 🧠 Yangi: 10-mashq (Yangi topshiriq)

### 🎰 **Son o‘yini: FizzBuzz varianti**

Foydalanuvchidan bir son oling (`n`).
1 dan `n` gacha bo‘lgan sonlar uchun quyidagi qoidalarni bajaring:

* Agar son 3 ga bo‘linsa: `Fizz` deb yozing.
* Agar son 5 ga bo‘linsa: `Buzz`
* Agar 3 va 5 ga bo‘linsa: `FizzBuzz`
* Aks holda — o‘zini yozing.

Masalan:

```
1  
2  
Fizz  
4  
Buzz  
Fizz  
7  
8  
Fizz  
Buzz  
11  
Fizz  
13  
14  
FizzBuzz
```

**Ko‘nikma:** `for`, `if-elif-else`, `mod (%)`, `print` — ajoyib kombinatsiya.

---

Bu ikki mashq ham:

* `loop`ni puxta o‘rganishga yordam beradi,
* shunchaki kod emas — **real hayotga o‘xshash tasklar**,
* yuqori darajadagi fikrlashga majbur qiladi,
* o‘quvchida “vau, shunday narsa qilish mumkin ekan!” degan qiziqish uyg‘otadi.

---

