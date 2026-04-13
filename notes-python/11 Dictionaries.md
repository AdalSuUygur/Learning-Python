
# DICTIONARIES (Sözlükler)

Sözlükleri, index yerine anahtarla tutulan listeler gibi düşünebiliriz.\
Yapısı: Value --- Key\

> **Dictionary:** _Key (Anahtar)_ ve _Value (Değer)_ çiftlerinden oluşur.

Bir kullanıcının bilgilerini Listede tutmaya çalışalım:

```py
# Liste Yöntemi
kullanici = ["Su", 29, "Data Scientist", "İstanbul"]
```

Burada "Su" ismini bulmak için `kullanici[0]` denilmesi lazım.\
Peki ya "İstanbul" kaçıncı sıradaydı? `[3]` mü `[4]` mü?\
Bulabilmek için ezberlemek zorundayız.\
Sıra karışırsa veri bozulur.\
Milyonlarca datanın var olduğu bir sistemde bu gerçekleşmesi mümkün bir senaryo mu? Hayır.\
O halde çözüm ne?

* **Çözüm:** Veriye numarayla (indeksle) değil, **ismiyle (etiketiyle)** ulaşmak.

## Sözlüklerin Anatomisi

* **Anahtar-Değer (Key-Value):** Her veri bir çifttir. Tek başına durmazlar.

* **Sırasızdır:**

> **Teknik Not:** Python 3.7'den sonra ekleme sırasını hatırlamaya başladılar ama mantıken biz onlara "sırasız" muamelesi yaparız. Çünkü veriye sıra numarasıyla (dict[0]) değil, anahtarla (dict["ad"]) ulaşırız.

* **Değiştirilebilirdir (Mutable):** İçinde CRUD (Create Read Update Delete) operasyonları yapılabilir.

* **Anahtarlar Eşsizdir (Unique Keys):** Bir sözlükte iki tane "isim" anahtarı olamaz! (Set mantığı).

* **Anahtarlar Sabittir (Immutable Keys):** Anahtar olarak sadece değiştirilemeyen tipleri kullanabilirsin (String, Integer, Tuple).

## SYNTAX

Süslü parantez `{}` kullanılır. Çiftler arasına iki nokta üst üste `:` konur.

```py
#              Anahtar : Değer
bursiyer = {
    "ad": "Adal Su",     # String key, String value
    "yas": 29,           # String key, Int value
    "mezun_mu": True,    # String key, Bool value
    "notlar": [90, 85]   # String key, Liste value (Value her şey olabilir!)
    }

    print(bursiyer["ad"]) # Çıktı: Adal Su
# Veriye ulaşmak için ise sözlük ismi ve istenilen key:
# Aslında baktığında listeyle aynı mantık sadece index yerine direkt veriyi verdik
```

> **Key (Anahtar):** Etikettir. Eşsizdir (Set gibi). Değiştirilemez (String, Sayı, Tuple olabilir).\
> **Value (Değer):** Verinin kendisidir. Her şey olabilir (Liste, başka sözlük, sayı...).

## Sözlüklerin Key (Anahtar) Mantığı nedir?

Sözlüklerde aranan değerin karşılığı key(anahtar)dır. Python, bir şeyi "Key" olarak kabul etmek için 2 katı kural koyar.

### Key Unique Olmalıdır (Eşsiz)

Bir sözlükte **aynı anahtardan iki tane olamaz.**
Mantıken düşün: Telefon rehberinde iki tane "Ahmet Yılmaz" olsa ve ikisinin de numarası farklı olsa, "Ahmet'i ara" dediğinde telefon kimi arayacağını bilemez.

* **Ne olur?** Eğer aynı key'i tekrar eklersen, Python hata vermez ama **eski veriyi siler, yenisini yazar (Overwrite).**

### Key Immutable Olmalıdır (Değiştirilemez)

Burası en çok hata yapılan yerdir.
Bir sözlükte anahtar olacak şey, **asla değişmeyecek** bir türde olmalıdır.

**Neden?**
Anahtar bir "Parmak İzi" gibidir. Eğer parmak izi sürekli değişseydi, parmak iziyle açılan bir kapıyı açabilir miydin? Açamazdın.

## Hash Mantığı (Big O Notation)

Sözlüklerin listelerden binlerce kat hızlı olmasının sebebi **Key** mantığındaki **Hashing** teknolojisidir.

Bir listede "Elma"yı ararken Python kutuları tek tek açar: "Bu mu? Hayır. Bu mu? Hayır..." (Linear Search).
Sözlükte ise durum şöyledir:

1. Sen `"isim"` anahtarını verirsin.
2. Python bu anahtarı alır, özel bir matematiksel formülden geçirir (Hash Function).
3. Bu formül ona direkt **bellek adresini** söyler: "Git, 3450. adrese bak!"
4. Python tek hamlede veriyi alır.

Bu yüzden sözlükte 3 eleman da olsa, 1 milyon eleman da olsa aradığını bulma hızı **aynıdır (O(1)).**

## Dict için Birleştirme Operatörü (`|`)

Artık iki sözlüğü `|` ile birleştirebiliyoruz (Set'lerdeki birleşim gibi).

```py
d1 = {"a": 1}
d2 = {"b": 2}
yeni = d1 | d2  # {'a': 1, 'b': 2}
```

## Dictionary Comprehension

Tek satırda sözlük üretme.
**Syntax:** Süslü parantez `{}` kullanılır ama içinde **İki Nokta üst üste (`:`)** olmak zorundadır (Key: Value yapısı).

```py
# Sayıların karesini alıp sözlük yapalım
kareler = {x: x*x for x in range(5)} 
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
```

```py
isimler = ["Ali", "Veli", "Ayşe"]

# İsimleri anahtar, uzunluklarını değer yapalım
uzunluklar = {isim: len(isim) for isim in isimler}

print(uzunluklar)
# Çıktı: {'Ali': 3, 'Veli': 4, 'Ayşe': 4}
```
