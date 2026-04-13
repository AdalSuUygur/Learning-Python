
# LISTS (Listeler)

Python'da Liste (List), birden fazla öğeyi tek bir değişken içinde tutmak için kullanılan **sıralı** ve **değiştirilebilir** (mutable) bir v**eri koleksiyonu**dur.

Listeler verileri kalıcı olarak depolamazlar. Listeler RAM'de depolanır yani geçici alanda depolanır. RAM'in heap alanında referanslar saklanır.

>_Yani: Listeler farklı veri tiplerini tek bir değişken altında tutmaya yarar._

Veri Biliminde `Pandas DataFrame` dediğimiz o devasa tabloların atası Listelerdir.

## Listenin Anatomisi

Listeleri, arkasına sonsuz sayıda vagon eklenebilen bir **Tren** gibi düşün.

* **Sıralıdır (Ordered):** Vagonların sırası bellidir. Sen değiştirmediğin sürece karışmaz.
* **Değiştirilebilir (Mutable):** (Burası çok önemli!) Stringlerin aksine, bir listenin 2. vagonundaki yükü indirip yerine başka bir şey koyabilirsin.
* **Heterojendir:** İlk vagonda **Sayı**, ikinci vagonda **Yazı**, üçüncü vagonda **Başka Bir Liste** taşıyabilirsin.

## SYNTAX

Listeler köşeli parantezler (`[]`) içinde tanımlanır ve öğeler virgülle ayrılır.

```py
# List Syntax
meyveler = ["elma", "muz", "kiraz"]
karisik_liste = [10, "Merhaba", 3.14, True]
```

## Listelerin Index (Dizin) Mantığı Nedir?

Listeler sıralı olduğu için, her öğenin sabit bir konumu vardır.
Listenin elemanlarının bulunduğu sayıya index denir.

>**Yani:** Index, bir listedeki her bir öğenin konumunu belirten sayısal etikettir.

```py
#          0        1         2        3
iller = ["İzmir", "Ankara", "İstanbul", "Van"]
#         -4       -3        -2       -1

print(iller[0])  # İzmir (Başı)
print(iller[-1]) # Van (Sonu - Uzunluğu bilmene gerek yok!)
```

### Sıfır Tabanlı İndeksleme

Python'da sayım 0'dan başlar. Listenin ilk öğesi `0` indexindedir.

### Negatif İndeksleme

Listenin sonundan başlamak için kullanılır. Son öğe `-1` indexindedir.

> **NOT:** Veri biliminde son 5 günlük veriyi çekmek istediğinde `data[-5:]` yazacaksın. Negatif indeksleme hayat kurtarır.

## Slicing (Veri Dilimleme)

Elimizde devasa bir liste var ama bize sadece bir kısmı lazım. İşte burada **Dilimleme (Slicing)** devreye girer.\
Pandas (veri analizinde de) kullanılır, çok önemli!!!!\
Mevcut bir SIRALI YAPININ belirli bir bölümünü alarak YENİ BİR YAPI oluşturma işlemidir.\
Bu dilimleme orjinal listeyi değiştirmez.

**Formül:** `liste[başlangıç : bitiş : adım]`

* **Başlangıç:** Dahil (Yazmazsan 0).
* **Bitiş:** DAHİL DEĞİL (Yazmazsan listenin sonuna kadar).
* **Adım:** Kaçar kaçar gideceği.

```py
sayilar = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print(sayilar[2:5])   # [2, 3, 4] -> 5 dahil değil!
print(sayilar[:3])    # [0, 1, 2] -> Baştan başla, 3. indekse kadar al.
print(sayilar[::2])   # [0, 2, 4, 6, 8] -> Baştan sona 2'şer atla.
print(sayilar[::-1])  # [9, 8, ... 0] -> LİSTEYİ TERS ÇEVİRİR! (Mülakat Sorusu)
```

## Matrix (İç İçe Listeler)

Excel tabloları, satranç tahtaları veya görüntü işleme (pikseller)... Hepsi aslında satır ve sütunlardan oluşur. Python'da bunu **Liste içinde Liste** (Nested Lists) ile yaparız.

Bunu bir apartman gibi düşün:

* Dış liste: Apartman
* İç listeler: Katlar
* Elemanlar: Daireler

```py
# 3 Satır, 3 Sütunlu bir matris
matris = [
    [1, 2, 3],  # 0. İndeks (Satır 0)
    [4, 5, 6],  # 1. İndeks (Satır 1)
    [7, 8, 9]   # 2. İndeks (Satır 2)
]

# Hedef: 6 sayısını çekmek (Satır 1, Sütun 2)
# Formül: matris[satir_indexi][sutun_indexi]

print(matris[1])    # Çıktı: [4, 5, 6] (Tüm satır gelir)
print(matris[1][2]) # Çıktı: 6 (Nokta atışı)
```
