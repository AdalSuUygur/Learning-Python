
# OPERATORS

Operatörler, bir veya daha fazla işlenen, operand adı verilen değer üzerinde belirli bir matematiksel, mantıksal veya atama eylemini gerçekleştiren mekanizmalardır.
Operatörler temelde şu amaçlarla kullanılır:

1. Hesaplama (Matematiksel İşlemler): Sayısal değerleri toplama, çıkarma, çarpma vb.
2. Atama: Bir değişkenin değerini belirleme veya güncelleme.
3. Karşılaştırma: İki değerin birbirine göre durumunu (büyük mü, küçük mü, eşit mi) kontrol etme.
4. Mantıksal İlişki Kurma: Birden fazla koşulun aynı anda doğru olup olmadığını kontrol etme.

## Aritmetik Operatörler (Sayısal İşlemler)

| Operatör | Tanım | Örnek | Sonuç | Önemi (Veri Bilimi) |
| :--- | :--- | :--- | :--- | :--- |
| `+` | Toplama | `10 + 3` | `13` | Temel agregasyon. |
| `-` | Çıkarma | `10 - 3` | `7` | Farkları hesaplama. |
| `*` | Çarpma | `10 * 3` | `30` | Skalizasyon. |
| `/` | Bölme **(Float Bölme)** | `10 / 3` | `3.333...` | Gerçek ondalıklı bölme. |
| `//` | **Tam Sayı Bölme (Floor Division)** | `10 // 3` | `3` | Bölümün tam sayı kısmını döner. |
| `%` | **Modül (Kalan Operatörü)** | `10 % 3` | `1` | Bölme işleminden kalanı döner. **(İndeksleme ve gruplama için kritik)** |
| `**` | Üs Alma | `10 ** 2` | `100` | Eşik değerleri hesaplama, maliyet fonksiyonlarında kare alma. |

## Atama Operatörleri (Assignment Operators)

Var olan bir değeri değiştirmek (güncellemek) için kullanılırlar. `x = x + 2` gibi uzun ifadeleri kısaltırlar.

Bir değişkene bir değer atamak için kullanılır. En temeli tek eşittir işaretidir.

| Operatör | Kullanım | Uzun Hali | Açıklama |
| :--- | :--- | :--- | :--- |
| `=` | `x = 5` | N/A | Sağdaki değeri soldaki değişkene atar. |
| `+=` | `x += 2` | `x = x + 2` | Değişkenin değerini artırıp yeniden atar. |
| `-=` | `x -= 2` | `x = x - 2` | Değişkenin değerini azaltıp yeniden atar. |
| `*=` | `x *= 2` | `x = x * 2` | Değişkenin değerini çarpıp yeniden atar. |
| `/=` | `x /= 2` | `x = x / 2` | Değişkenin değerini bölüp yeniden atar. |

## Karşılaştırma Operatörleri (Comparison Operators)

İki değeri karşılaştırır ve sonuç olarak her zaman **Boolean (`True` veya `False`)** değeri döner.

| Operatör | Tanım | Örnek | Sonuç |
| :--- | :--- | :--- | :--- |
| `==` | Eşit mi? | `5 == 5` | `True` |
| `!=` | Eşit değil mi? | `5 != 10` | `True` |
| `>` | Büyük mü? | `10 > 5` | `True` |
| `<` | Küçük mü? | `5 < 10` | `True` |
| `>=` | Büyük veya eşit mi? | `5 >= 5` | `True` |
| `<=` | Küçük veya eşit mi? | `10 <= 5` | `False` |

## Mantıksal Operatörler

Birden fazla koşulun mantıksal birleştirilmesi için kullanılır ve programın karar mekanizmalarında (`if` ifadeleri) hayati rol oynar.

| **Operatör** | **Anlamı** | **Örnek (Python)**     | **Sonuç**                          |
| ------------ | ---------- | ---------------------- | ---------------------------------- |
| `and`        | VE         | `(5 > 3) and (2 < 4)`  | `True` (Her iki koşul da doğruysa) |
| `or`         | VEYA       | `(5 == 5) or (10 < 1)` | `True` (Koşullardan biri doğruysa) |
| `not`        | DEĞİL      | `not (5 > 10)`         | `True` (Koşulun tersini alır)      |

## Kimlik ve Üyelik Operatörleri (Identity & Membership)

### Üyelik Operatörleri (Membership Operators)

Bir elemanın bir koleksiyonun (liste, string, set) içinde olup olmadığını kontrol eder.

* `in`: Bir elemanın koleksiyonda olup olmadığını kontrol eder.
  * Örnek: `print('s' in 'su')` $\rightarrow$ `True`
* `not in`: Bir elemanın koleksiyonda olmadığını kontrol eder.

### Kimlik Operatörleri (Identity Operators)

İki değişkenin bellekte aynı objeyi işaret edip etmediğini kontrol eder.

* `is`: İki değişkenin bellekte **aynı objeye** mi işaret ettiğini kontrol eder.
* `is not`: İki değişkenin bellekte aynı objeye işaret etmediğini kontrol eder.
    > **Not:** `==` değeri, `is` ise bellekteki **konumu (kimliği)** karşılaştırır.

## Diğer ÖNEMLİ OPERATÖRLER

Operatörler, kodlama dillerinde değerler üzerinde işlemler yapmak için kullanılan özel sembollerdir. Programlamanın temelini oluştururlar ve hemen hemen her kod satırında bir operatör kullanılır.
+, -, *, / bunları zaten herkes biliyor.
Ama bir Veri Bilimci (Data Scientist) olarak asıl sihirbazlıkların döndüğü o üç özel operatörü masaya bilmem ŞART.

### Modulus % (Kalan Bulma)

Bölme işleminden kalanı verir.

Neden önemli?\
Bir sayının tek mi çift mi olduğunu anlamak için (sayi % 2), döngülerde belli periyotlarda işlem yapmak için (her 10. veride bir kayıt al gibi) hayati önem taşır.

```py
print(10 % 3)  # Çıktı: 1 (10'un 3'e bölümünden kalan 1'dir)
print(25 % 5)  # Çıktı: 0 (Tam bölünür)
```

### Floor Division // (Tam Bölme)

Bölme sonucunun ondalık kısmını atar ve sadece tam sayıyı (tabana yuvarlanmış halini) verir.

Neden önemli?\
Diyelim ki 105 tane verin var ve her sayfada 10 veri göstereceksin. Kaç tane tam sayfa dolar? 105 // 10 = 10 sayfa.

```py
print(10 / 3)   # Çıktı: 3.33333... (Normal bölme float verir)
print(10 // 3)  # Çıktı: 3 (Sadece tam kısım, int verir)
```

### Exponentiation ** (Üs Alma)

Bir sayının kuvvetini alır.

Neden önemli?\
İstatistik, makine öğrenmesi formülleri (Varyans, Standart Sapma) hep kare alma üzerine kuruludur.

```py
print(2 ** 3)  # 2 üzeri 3 = 8
print(5 ** 2)  # 5'in karesi = 25
```

### * Eğer bir iterable'ın kaç öğe içerdiği bilinmiyor veya sadece ilk ve son öğeleri alınmak isteniyorsa kullanılır

```py
rakamlar = [1, 2, 3, 4, 5, 6]
ilk, *orta, son = rakamlar
print(ilk)  # Çıktı: 1
print(orta) # Çıktı: [2, 3, 4, 5]
print(son)  # Çıktı: 6
```
