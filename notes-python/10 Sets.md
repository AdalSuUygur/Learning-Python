
# SETS (Kümeler)

Matematikteki kümeler mantığını hatırla; Python'daki `set()` tam olarak budur.

Set, öğelerin **sırasız** olduğu ve **eşsiz (unique)** olduğu bir koleksiyondur. Bir veriden sadece bir tane olmasını garanti eder.

## Setlerin Anatomisi

**Sırasızdır (Unordered):**
"ilk elemanı" veya "son elemanı" diye bir şey yoktur.
İçine attığın veriler rastgele durur.

* *Bu yüzden:* `set[0]` diyemezsin, Python "Sıra yok ki kardeşim neyi istiyorsun?" der (Hata verir).

**Eşsizdir (Unique - En Önemli Özellik):**
Aynı veriyi ikinci defa ekleyemezsin. İkincisi eklenilmeye çalıştığında ikinci kopyayı anında yok eder.

* *Veri Bilimi:* Binlerce satırlık verideki "tekrar eden kopyaları" temizlemek için tek çare budur.

**Değiştirilebilir (Mutable - Ama Şartlı):**
Setin içine yeni eleman atılabilir (`.add()`) veya içinden eleman çıkartılabilir (`.remove()`).

* *Fark:* Listede "2. sıradakini değiştir" diyebiliyordun. Set'te sıra olmadığı için "Şunu değiştir" diyemezsin, sadece "Eskisini çıkar, yenisini al" yapabilirsin.

**Heterojendir (Ama Seçici):**
İçine Sayı, Yazı (String), Tuple atabilirsin.

* **Kritik Not:** Set'in içine **Liste** veya **Sözlük** atamazsın! Çünkü Set'ler, içine girecek elemanların "sabit/değişmez" olmasını ister. (Listeler değişebildiği için Set'in yapısını bozar).

## SYNTAX

Setler süslü parantez `{}` ile tanımlanır.

```py
# Tanımlama
meyveler = {"elma", "muz", "elma", "portakal"}
print(meyveler) 
# Çıktı: {'muz', 'portakal', 'elma'} -> Bak, ikinci 'elma' uçtu! Sıra da değişti.

# Boş Set Tanımlarken DİKKAT:
bos_sozluk = {} # Bu bir dict (sözlük) yaratır.
bos_set = set() # Boş set sadece bu şekilde yaratılır.
```

## Set için Built-in-methods

* `.add(x)`: Eleman ekler.
* `.remove(x)`: Elemanı siler (Yoksa hata verir).
* `.discard(x)`: Elemanı siler (Yoksa hata vermez - **QA Favorisi!**).
* `.intersection()`: Kesişim.
* `.union()`: Birleşim.
* `.difference()`: Fark.

## Set'in kendine has operatörleri

### Birleşim (Union) `|`

İki kümedeki tüm elemanları birleştirir.
Matematikteki: (A ∪ B) ifadesinin karşılığı.

* **Sembol:** `|` (Pipe işareti)
* **Örnek:** `set_a | set_b`

### Kesişim (Intersection) `&`

Sadece her iki kümede de bulunan ortak elemanları alır.
Matematikteki:  ifadesinin karşılığı.

* **Sembol:** `&` (Ampersand / Ve işareti)
* **Örnek:** `set_a & set_b`

### Fark (Difference) `-`

Birinci kümede olup ikinci kümede olmayan elemanları alır.
Matematikteki: (A \ B) ifadesinin karşılığı

* **Sembol:** `-` (Eksi işareti)
* **Örnek:** `set_a - set_b`

### Simetrik Fark (Symmetric Difference) `^`

Sadece kümelerin birinde olanları alır; yani her ikisinde de ortak olanları dışarıda bırakır.
Matematikteki: (A ∆ B) ifadesinin karşılığı

Kendime not: (A ∪ B) - (A ∩ B) gibi düşün. Keşisim kümesini siliyor.

* **Sembol:** `^` (Carets / Şapka işareti)
* **Örnek:** `set_a ^ set_b`

## Set Comprehension

Tek satırda set üretmesini sağlayan kompakt yapıdır.
**Syntax:** List comprehension ile aynıdır, sadece köşeli parantez `[]` yerine süslü parantez `{}` kullanılır.

* **Özellik:** Tıpkı normal set gibi, üretirken **tekrarları siler** ve **sırasızdır**.

```py
liste = [1, 2, 2, 3, 4, 4, 5]

# Set Comprehension
kume = {x for x in liste} 

print(kume)
# Çıktı: {1, 2, 3, 4, 5} -> Tekrarlar uçtu gitti!
```
