
# BUILT-IN FUNCTIONS

Built-in Fonksiyonlar (Yerleşik Fonksiyonlar), Python programlama dilinin en
temel ve en sık kullanılan işlemler için doğrudan dilin içine gömülmüş olarak
gelen fonksiyonlardır.

Yerleşik fonksiyonlar, geliştiricilerin yaygın görevleri hızlı ve kolay bir şekilde yerine getirmesi için tasarlanmıştır.

>***ÖNEMLİ***:\
Fonksiyonlar, bir görevi yerine getiren komut gruplarıdır.\
Parantezler (`()`), Python'a bir fonksiyon çağrısı yaptığınızı gösterir.\
Parantez içine yazılan değerler (Örn: `print("Bu bir argümandır")` içindeki metin), fonksiyona gönderilen argümanlar (arguments) olarak adlandırılır.

Bu fonksiyonların olayı şudur: **Import gerekmez, kurulum gerekmez.** Python'u açtığın an emrine amadedirler.

## Veriyi Tanımak için Kullanılan Fonksiyonlar

Verinin neye benzediğini, sınırlarını ve içeriğini anlamak için kullanılırlar.

* **`len(nesne)`:** Var olan listenin uzunluğu (kaç elemanı olduğunu) verir.

* **`sum(iterable)`:** Toplama işlemi yapar. Sadece sayılarla çalışır!

> *Kritik Hata:* `sum(["a", "b"])` yaparsan `TypeError` alırsın. Stringleri toplamaz, sayıları toplar.

* **`max()` ve `min()`:** En büyük ve en küçük elemanı bulur.

> *İpucu:* Stringlerde de çalışır! Alfabetik sıraya (ASCII tablosuna) göre karar verir. ("Z" > "A").

* **`sorted(iterable)`:** Sıralama yapar.

> **Senior Farkı:** `list.sort()` listenin *kendisini* değiştirir. `sorted(list)` ise orijinal listeye dokunmaz, sana **yepyeni sıralı bir liste** verir.

* Verim kalsın, sonucunu göreyim diyorsan -> **Fonksiyon** (`sorted`)
* Verim değişsin, hafızada yer kaplamasın diyorsan -> **Metot** (`.sort`)

> **İpucu:** Tersten sıralamak için her ikisinde de `reverse=True` parametresini kullanabilirsin.
> `sorted(sayilar, reverse=True)`

* **Hafıza:** Ekstra yer kaplamaz (Memory efficient), çünkü yeni liste yaratmaz.
* **Tehlike:** Orijinal veriyi kaybedersin.

```py
sayilar = [5, 1, 9]
sayilar.sort() # Listeyi olduğu yerde değiştirdi.
print(sayilar) # Çıktı: [1, 5, 9]

# ⚠️ Sık Yapılan Hata:
# yeni_liste = sayilar.sort() -> YANLIŞ!
# sort() geriye 'None' döndürür. yeni_liste boş kalır.
```

## Fabrika İşçileri (Map & Filter)

Burası Fonksiyonel Programlamanın kalbidir.

Bu fonksiyonlar **Tembeldir (Lazy Evaluation)**. Sen onları `list()` içine alıp "Hadi çalış" diyene kadar işlemi yapmazlar, sadece bir "Bilet (Object)" üretirler.

> **Neden Önemli?** "Maliyet Tatlım!". 1 Milyon veriyi hafızaya yüklemez, sırası geldikçe işler.

### `filter(fonksiyon, liste)`

Eline bir liste verirsin, bir de kural (fonksiyon). Sadece kurala uyanları (True dönenleri) içeri alır.

* **Mantık:** `if` koşulunun fonksiyon halidir.
* **Kullanım:** `None` değerleri temizlemek, negatif sayıları atmak, belli harfle başlayanları seçmek.

`filter(str.isdigit, some_values)` -> Sadece rakam olan stringleri ayıklar.

### `map(fonksiyon, liste)`

Listedeki **HER** elemanı alır, üzerine fonksiyonu uygular ve değiştirilmiş halini verir. Eleman sayısı asla değişmez, sadece şekli değişir.

* **Mantık:** `for` döngüsünün tek satırlık halidir.
* **Kullanım:** Tüm sayıları stringe çevirmek, tüm fiyatlara KDV eklemek.

`map(str, numeric_lst)` -> Sayı listesini string listesine çevirir.

## Birleştiriciler (Zip & Enumerate)

### `zip(*iterables)` - "Fermuar"

İki veya daha fazla listeyi alır, aynı sıradaki elemanları birleştirip demet (tuple) yapar.

* **Altın Kural:** En kısa listeye göre çalışır. Uzun olanın artan kısmı **kesilip atılır.**

> **Senior Trick (Transpoz):** Bir matrisin satırlarını sütun yapmak için `zip(*matrix)` kullanılır.

### `enumerate(iterable)` - "Numaratör"

Bir listeyi gezerken "Ben kaçıncı sıradayım?" sorusunu çözer. `(index, item)` çifti verir.

> *Not:* Hem elemana hem de sırasına (indeksine) ihtiyacınız olduğunda kullanılır.

## Mantıksal Dedektifler (Any & All)

Bu ikili, listeler üzerindeki `and` ve `or` operatörleridir.

* **`any(iterable)` - "İyimser Dedektif":**
* İçinde **BİR TANE BİLE** `True` (veya dolu değer) varsa `True` döner.

> **Not:** `bos_lst = [0, False, "", [], ()]` için `False` döner çünkü hepsi Python'da "boşluk" veya "yokluk" ifade eder.

* **`all(iterable)` - "Mükemmeliyetçi Dedektif":**
* Hepsi `True` olmak zorundadır. Bir tane çürük elma varsa `False` döner.

> *Örnek:* "Şifre kurallarının **HEPSİ** sağlandı mı?" (Büyük harf, küçük harf, rakam...).

## Kimlik Kontrolü (`isinstance`)

* **`isinstance(nesne, tip)`:**
* `type(x) == int` demek yerine bunu kullanırız.
* **Neden?** Çünkü `isinstance`, kalıtım (inheritance) ilişkilerini de anlar.

> **Not:** `isinstance(x, (int, float))` diyerek tek seferde "Sayı mı?" (Tam sayı VEYA ondalıklı sayı) kontrolü yapabilirsin.

## Önemli Notlar

1. **Lambda vs Built-in:** `filter` veya `map` içinde basit bir işlem yapacaksan (örn: `str.lower` veya `str.isdigit`) lambda yazma, direkt fonksiyonun adını ver. Daha hızlıdır.

2. **Liste mi Iterator mu?:** `print(map(...))` dersen ekranda `<map object at 0x...>` görürsün. İçini görmek için `list()` veya `tuple()` ile paketlemen gerekir. Ama sadece döngüde kullanacaksan `list()`'e çevirme, bırak iterator kalsın (RAM tasarrufu).

3. **Karmaşıklık:** `map` ve `filter` döngülerin yerini tutar ama çok karmaşık işlemlerde **List Comprehension** genellikle daha okunaklıdır.
