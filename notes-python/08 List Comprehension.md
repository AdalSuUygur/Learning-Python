
# LIST COMPREHENSION (Tek Satırda Liste Üretimi)

Bir listeyi oluşturmak için gereken adımları (boş liste tanımlama, döngü kurma, .append() ile ekleme), tek bir sözdizimi içine yerleştirmektir. Kısaca liste oluşturmak için list comprehension kullanılır, liste oluşturma sürecinin preslenmiş halidir de denilebilir. :)

```py
# Geleneksel yöntem ile verilen listedeki verilerin karesini hesaplayan uygulama yapalım.
sayilar = [1, 2, 3, 4, 5]

kareler = []              # 1. Boş liste aç
for x in sayilar:         # 2. Döngüyü kur
    kareler.append(x * x) # 3. Hesapla ve ekle

print(kareler) # [1, 4, 9, 16, 25]

# 3 satır süren kodu, aynı şekilde list comprehension ile yapmayı deneyelim:

# Formül: [ YAPILACAK_İŞLEM  for  DEĞİŞKEN  in  LİSTE ]

kareler = [x * x for x in sayilar]
print(kareler) # [1, 4, 9, 16, 25]
```

## Syntax (Formül) Nasıl Okunur?

Bu yapıyı Türkçe bir cümle gibi okursan beynine kazınır.

Kod: `[x * x for x in sayilar]`

**Okunuşu:**

1. `for x in sayilar`: Sayılar listesindeki **HER BİR X İÇİN...**
2. `x * x`: ... git **X'İN KARESİNİ AL**...
3. `[]`: ... ve çıkan sonucu **BU LİSTENİN İÇİNE KOY.**

Özetle formül şudur:
`[ <SONUÇ NE OLSUN?> for <KİMİN İÇİN?> in <NEREDEN?> ]`

## Ne Amaçla Kullanılır?

1. **Kod Okunabilirliği:** 5 satırlık kalabalık bir kod bloğu yerine tek satırda ne yaptığın anlaşılır.

2. **Performans:** Arka planda `.append()` metodundan daha hızlı çalışır. (Büyük verilerde fark yaratır).

3. **Veri Temizliği (Data Science):**

* Mesela elinde `["  Ahmet ", "  Mehmet  "]` gibi boşluklu veriler var.
* Tek satırda: `[isim.strip() for isim in liste]` diyerek hepsini temizlersin.

## Level 1: Basit Dönüşüm (Mapping)

"Her elemanı al, bir işlem yap, listeye koy."

* **Formül:** `[ İŞLEM for ELEMAN in LİSTE ]`

```py
# --- LIST COMPREHENSION (Usta Yöntemi) ---
# Meali: "sayilar" içindeki her "x" için, "x'in karesini" al.
kareler = [x ** 2 for x in sayilar] 
# Sonuç: [1, 4, 9, 16]
```

## Level 2: Filtreleme (Filtering)

"Her elemanı alma, sadece şartı sağlayanları al."

* **Formül:** `[ İŞLEM for ELEMAN in LİSTE if KOŞUL ]`
* **Dikkat:** `if` en sona gelir!

```py
# --- LIST COMPREHENSION ---
# Meali: Eğer x çift ise, x'i listeye ekle.
ciftler = [x for x in sayilar if x % 2 == 0]
# Sonuç: [2, 4, 6]
```

## Level 3: Karar Verme (If-Else Logic)

"Eleman şuysa böyle yap, değilse şöyle yap."

* **Formül:** `[ (DURUM_1 if KOŞUL else DURUM_2) for ELEMAN in LİSTE ]`
* **Dikkat:** `if-else` varsa, `for` döngüsünün **BAŞINA** gelir!

```py
# --- LIST COMPREHENSION ---
# Meali: x çift ise "Çift" yaz, yoksa "Tek" yaz.
sonuc = ["Çift" if x % 2 == 0 else "Tek" for x in sayilar]
# Sonuç: ['Tek', 'Çift', 'Tek']
```
