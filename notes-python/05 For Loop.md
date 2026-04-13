
# FOR LOOP

for döngüsü; bir koleksiyonun (listenin, metnin, veri setinin) üzerinden geçer. Yani, bir "iterable" (üzerinde gezilebilir) nesne içindeki her bir elemanı sırayla alır ve işler.

Türkçesi: "Bu listenin içindeki her bir eleman İÇİN şunu yap."

>*Not:* Veri biliminde milyonlarca satırlık veriler (DataFrames) işlenir. for döngüsünü anlamak, o verilerin her bir satırına nasıl dokunacağını anlamaktır.

Veri bilimi'nde milyonlarca veriyi tek tek işlemek yerine, bu işlemi otomatik olarak yapmak isteriz, tam olarak bu noktada döngüler devreye girer ve bu otomasyonu sağlar.
Döngüler ile koda **"Toplu İşlem Yapma Gücü"** (Batch Processing) kazandırılır.

>For döngüsü, veri setlerini işlemekte en çok kullanılan döngü tipidir.

## SYNTAX FOR

```py
# Koleksiyon Üzerinde İlerleme (Iteration)
isim = "Python"

# 'isim' (string) içindeki her bir harf için döngüyü çalıştır
for harf in isim:
    print(harf)
```

## `range()` Fonksiyonu (Sayı Üreticisi)

**Range Fonksiyonu:** Belirli bir sayı aralığında dönmek için kullanılır. Bu, belirli sayıda tekrar yapmak veya indeksler üzerinden ilerlemek için önemlidir.

Bazen elinde bir liste yoktur ama "Bu işlemi 50 kere yap" veya "1'den 100'e kadar sayıları topla" demek istersin. İşte o zaman `range()` devreye girer.

`range(start, stop, step)`

* **start:** Başlangıç (Dahil). (Yazmazsan 0 kabul eder).
* **stop:** Bitiş (**DAHİL DEĞİL!** - En çok karıştırılan yer).
* **step:** Adım sayısı. (Yazmazsan 1 kabul eder).

```py
# Senaryo 1: 0'dan 4'e kadar (5 dahil değil)
for i in range(5):
    print(i) # Çıktı: 0, 1, 2, 3, 4

# Senaryo 2: 2'den 10'a kadar, 2'şer atla
for sayi in range(2, 11, 2):
    print(sayi) # Çıktı: 2, 4, 6, 8, 10 (11 dahil olmadığı için 10'da durur)

```

> **ÖNEMLİ Not:** `range(5)` hafızada 0,1,2,3,4 sayılarından oluşan bir liste oluşturmaz. Sadece sırası gelince sayıyı üreten bir "kural" oluşturur. Bu yüzden hafıza dostudur (Memory Efficient).

## Stringlerde Gezinme

Python'da metinler (String), aslında karakterlerden oluşan birer dizidir. Yani: `for harf in "Python"` dediğinde her bir harfi tek tek işleyebilirsin.

```py
isim = "Su"
for harf in isim:
    print(harf)
# Çıktı:
# S
# u
```

> **Not:** Bu özellik, Doğal Dil İşleme (NLP) projelerinde metinleri analiz ederken çok işine yarayacak.
