
# CONTROL FLOW STATEMENTS

Belirli bir koşulun sağlanıp sağlanmamasına göre farklı kod bloklarının çalıştırılmasının standart yoludur.

## If-Elif-Else Kontrol Bloğu

if ifadesi, kodun hangi yoldan ilerleyeceğine karar vermesini sağlar.
Koşul doğruysa (True), doğru olan yoldaki bloğun içindeki kod çalışır.

* **if:** Eğer (Koşul doğruysa bu kapıdan gir).
* **elif (else if):** Değilse ve Eğer... (İlk kapı kapalıysa, bu koşula bak).
* **else:** Hiçbiri değilse (Yukarıdakilerin hiçbiri tutmadıysa bunu yap).

### If - Elif - Else Avantajları

* **Evrensel Kullanım:** En yaygın ve tüm programlama dillerinde benzeri bulunan, temel karar verme mekanizmasıdır.
* if - elif - else bloğunda herhangi bir şart tutarsa diğer şartlara bakılmaz. _Memory adv._
* **Karmaşık Koşullar:** Mantıksal operatörler (`and`, `or`, `not`) kullanarak birden fazla karmaşık koşulu aynı anda kontrol etmeye olanak tanır.

### If - Elif - Else SYNTAX

```py
hava_durumu = "yagmurlu"

if hava_durumu == "yagmurlu":
    print("Şemsiyeni al!")  # 4 boşluk (1 tab) içeride!
    print("Botlarını giy.") # Bu da if bloğuna ait.
    
print("İyi günler.") # Bu en dışarıda, her durumda çalışır.
```

### Mantıksal Operatörlerle Kombo

`and`, `or`, `not` gibi operatörler burada devreye girer.

**Örnek:** Dışarı çıkmak için hem paramın olması **ve** (and) hava güzel olması lazım.

```py
para = True
hava_guzel = False

if para and hava_guzel:
    print("Sinemaya gidiyoruz!")
elif para and not hava_guzel:
    print("Evde pizza söyleyelim.")
else:
    print("Bugün tasarruf günü.")

```

## Nested If (İç İçe Kararlar)

Bir koşul sağlandığında farklı koşulların ortaya çıktığı durumlarda nested if kullanılır.

Yani koşul içinde koşul durumlarında tercih edilen bir yapıdır.

```py
kullanici = "admin"
sifre = "1234"

if kullanici == "admin":
    # İlk kapı geçildi, şimdi ikinciye bakılıyor
    if sifre == "1234":
        print("Hoş geldin Yönetici!")
    else:
        print("Yanlış şifre!")
else:
    print("Tanımsız kullanıcı.")

```

## Ternary If (Tek satır if)

Python'da Ternary If (Üçlü Koşullu İfade), bir `if-else` karar mekanizmasını tek bir satırda, kısa ve öz bir şekilde yazmanızı sağlayan özel bir sözdizimidir.

* _Tek satırda if-else gibi düşün. Tek mi çift mi gibi tek şart olan durumlarda kullanılır._

```python
# **Normal:**
puan = 55
if puan > 50:
    durum = "Geçti"
else:
    durum = "Kaldı"


# **Ternary (Tek Satır):**

# Mantık: [DOĞRUYSA YAP] if [KOŞUL] else [YANLIŞSA YAP]
durum = "Geçti" if puan > 50 else "Kaldı"

```

### Ternary If Avantajları

* **Kısalık ve Kompaktlık:** Kodunuzu bir if-else bloğundan tek bir satıra indirir, bu da kodun fiziksel uzunluğunu azaltır.
* **Okunabilirlik (Basit Durumlarda):** Basit atama koşullarında (yani, sadece iki olası sonuç olduğunda) okunabilirliği artırır ve amacını net bir şekilde gösterir.
* **İfade Olarak Kullanım:** Python'da ternary if bir ifade (expression) olduğu için, doğrudan fonksiyon çağrılarının veya liste/sözlük gibi veri yapılarına atamaların içinde kullanılabilir.

## Match-case Bloğu (Yapısal Eşleştirme)

* if else'e alternatif olarak gelen bir yapı. (C ailesindeki switch-case) match-case status kontrolü için sıklıkla tercih edilir ancak case'de and/or kullanmak daha zor.

* Genel olarak birebir uyum (==) sağlandığında case ifadesi daha tercih edilir.

* Ancak match-case ifadelerinde and/or kullanmak if bloklarına göre daha zordur.

### Match - Case Avantajları

* **Okunabilirlik (Temiz Kod):** Bir değişkenin birden fazla olası değerini kontrol ederken, çok sayıda `elif` kullanmaktan daha temiz ve okunaklıdır.
* **Gelişmiş Kalıp Eşleştirme:** Sadece değerleri değil, aynı zamanda veri yapılarının (listeler, sözlükler, sınıflar) yapısını da eşleştirebilir. Bu, özellikle karmaşık verilerle çalışırken güçlüdür.

### Match - Case SYNTAX

```py
http_kodu = 404

match http_kodu:
    case 200:
        print("Başarılı")
    case 404:
        print("Bulunamadı")
    case 500:
        print("Sunucu Hatası")
    case _:
        print("Bilinmeyen Durum") # else'in karşılığı (Wildcard)
```

> **Önemli Not:** `_` (alt çizgi) karakteri burada "Yukarıdakilerin hiçbiri değilse" (wildcard) anlamına gelir. Tıpkı `else` gibi çalışır.

### Match-Case'in Gizli Gücü: "Pipe" (|) ve "Guard"

#### Çoklu Kontrol (| - Veya)

```py
gun = "Pazar"

match gun:
    case "Cumartesi" | "Pazar": # Cumartesi VEYA Pazar ise
        print("Hafta sonu tatili!")
    case "Pazartesi":
        print("Sendrom günü.")
    case _:
        print("Hafta içi çalışmaya devam.")

```

#### Guard (If ile Koruma)

Match-case içinde `if` de kullanabilirsin! Buna "Guard" denir.

```py
sayi = 15

match sayi:
    case x if x % 2 == 0: # Eğer x çift sayıysa bu case'e gir
        print(f"{x} çift sayıdır.")
    case x:
        print(f"{x} tek sayıdır.")

```

## If-Elif-Else ve Match-Case Karşılaştırılması

| **Özellik** | **if-elif-else** | **match-case** |
| --------- | --------- | --------- |
| Kullanım Amacı | Her türlü koşulun (True/False) kontrol edilmesi (sayısal, mantıksal, karşılaştırma). | Bir değişkenin değerinin veya veri yapısının kalıplarla eşleştirilmesi. |
| Temel İşleyiş | Koşullar sırayla test edilir, ilk doğru (True) olan çalışır. | Veri, tanımlanan kalıplarla sırayla eşleştirilir (match), ilk eşleşen çalışır. |
| Kod Okunabilirliği | Çok sayıda `elif` olduğunda karmaşıklaşabilir. | Aynı değişkene ait çoklu değer kontrolünde daha temiz ve kompakt. |
| Python Versiyonu | Tüm versiyonlar. | Python 3.10 ve sonrası. |
| Varsayılan Durum | `else` bloğu. | `case _` bloğu. |
| **En İyi Kullanım** | Aralıklar (Ranges) ve Karmaşık Mantıklar | Belirli, Net Değerler ve Veri Yapıları |
| **Örnek Durum** | `if not < 50` veya `if x > 10 and y < 5` | `status == "active"` veya `role == "admin"` |
| **Esneklik** | Çok yüksektir. Her türlü bool ifadeyi yutar. | Daha yapısaldır. Veri tiplerini ve desenleri kontrol eder. |
| **Okunabilirlik** | Karışık koşullarda okunması zordur. | Çok temiz ve dikey okunabilirliği yüksektir. |
| **Hız** | Genelde standarttır. | Python 3.10+ optimize ettiği için desen eşlemede çok hızlıdır. |

---
