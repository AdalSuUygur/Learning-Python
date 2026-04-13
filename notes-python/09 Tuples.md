
# TUPLES (Demetler)

>_En basit tanımıyla:_ **Tuple, listelerin "korumalı" (read-only) versiyonudur.**

**Tuple:** Müzedeki cam fanus içindeki eserler gibidir. İçindekileri görürsün, sırasını bilirsin ama **dokunamazsın, değiştiremezsin, ekleyip çıkaramazsın.**

**Yani:** CRUD operasyonları yapılamıyor.

## Tuple Anatomisi

**Değiştirilemez (Immutable):** Oluşturulduktan sonra eleman eklenilemez veya çıkartılamaz!!!! (`append` yok), silemezsin (`pop` yok).

>Tercih nedeni: **Veri Güvenliği (Immutability):** Örneğin Dünya'nın enlem-boylam koordinatlarını `(36.0, 42.0)` bir değişkene atandı, bu liste olsaydı yanlışlıkla değiştirilebilirdi ve bu koordinatların değiştirilmesi tüm sistemi çökertebilirdi. Ancak tuple oluşturulursa bu sabitler değiştirilemez.

**Sıralıdır (Ordered):** Tıpkı listeler gibi index mantığı vardır. `tup[0]` diyerek ilk elemanı okuyabilirsin.

**Hız:** Listelerden daha hafiftir, yapısı gereği okuma operasyonlarında daha hızlı çalışır.

Not: Liste içinde tuple, Nested tuple gibi tanımlamalar yapılabilir, buralarda veri manipülasyonu olmadığı için sorunsuz çalışacaktır.

## SYNTAX

* Listeler: Köşeli Parantez `[]`
* Tuple'lar: Normal Parantez `()`

```py
# --- LİSTE (Değiştirilebilir) ---
pilotlar_list = ["Hamilton", "Verstappen"]
pilotlar_list[0] = "Leclerc"  # ✅ Sorun yok, Hamilton gitti, Leclerc geldi.

# --- TUPLE (Değiştirilemez) ---
koordinatlar_tuple = (41.0082, 28.9784)  # İstanbul'un konumu
# koordinatlar_tuple[0] = 50.000  # ❌ HATA! Python buna izin vermez.
```

## Tuple için Built-in-methods

* `.count(x)`: `x` değerinden bu Tuple'ın içinde kaç tane var?" diye sayar.
* `.index(x)`: `x` değeri kaçıncı sırada (indekste) duruyor?" diye sorar.

> **Önemli:** Eğer aradığın elemandan birden fazla varsa, **ilk bulduğunun** indeksini verir.
> **Not:** `.index()` metodu biraz alıngandır. Eğer Tuple içinde **olmayan** bir şeyi ararsan, `.count()` gibi 0 dönmez, programı **PATLATIR!**
>
>**Özetle:** Tuplelarda sadece `index` ve `count` methodları vardır. Yapılabilecek maximum işlem ise toplama ve slicing işlemleridir.

## Tuplelarda Yapılabilecek işlemler

### Slicing ve Indexing

Listelerle birebir aynıdır. Veriyi okumak için her türlü cambazlığı yapabilirsin.
> **Önemli:** Slicing yaptığında orijinal tuple bozulmaz, sana seçtiğin parçadan oluşan **yeni** bir tuple verir.

```py
veriler = (10, 20, 30, 40, 50)

# İndeksleme (Tek eleman seçme)
print(veriler[0])    # 10
print(veriler[-1])   # 50 (Sondan seçim)

# Slicing (Dilimleme)
print(veriler[1:4])  # (20, 30, 40) -> Yeni bir TUPLE döner.
print(veriler[::-1]) # (50, 40, 30, 20, 10) -> Tersi döner.

```

### Birleştirme (`+`) ve Çoğaltma (`*`)

Tuple'lar değişmez ama **toplanabilir!**
Nasıl yani? İki taşı birbirine yapıştırıp daha büyük bir taş yapabilirsin. Bu işlem eskileri bozmaz, ortaya **yepyeni** (üçüncü) bir Tuple çıkarır.

```py
tekler = (1, 3, 5)
ciftler = (2, 4, 6)

# Toplama (Concatenation)
yeni_tuple = tekler + ciftler 
print(yeni_tuple) 
# Çıktı: (1, 3, 5, 2, 4, 6)
# Not: 'tekler' ve 'ciftler' hala eskisi gibi duruyor.

# Çoğaltma (Repetition)
tekrar = ("Su",) * 3
print(tekrar)
# Çıktı: ('Su', 'Su', 'Su')
```

> **Özetle:** Gördüğün gibi, **"İçeriğini değiştirmek"** dışındaki her şeyi (okuma, kesme, biçme, toplama) yapabilirsin. Tuple, sadece üzerine yazı yazılamayan ama her türlü işleme sokulabilen bir "Veri Bloğu"dur.

## Tuple Comprehension (BÜYÜK TUZAK)

**Yapılır mı?** HAYIR. (Teknik olarak hayır).

Eğer List Comprehension mantığıyla parantez `()` kullanırsan, Python sana bir Tuple vermez. Sana **"Generator Object"** (Jeneratör) denen özel bir yapı verir.

```py
# Tuple yapmaya çalışalım
sey = (x for x in range(3))

print(sey)
# Çıktı: <generator object <genexpr> at 0x7f...>
# Gördün mü? Tuple değil!
```

>**Peki Neden?** (Veri Bilimi İçin Kritik Bilgi)

Tuple'lar değişmez (Immutable) olduğu için Python bunları dinamik olarak "comprehension" ile üretip belleğe koymaz.
Bunun yerine **Generator** oluşturur.

* **List Comprehension:** Yemeği pişirir, tabağa koyar (Bellekte yer kaplar).
* **Generator:** Sadece tarifi verir. Sen "Ye" diyene kadar (üzerinde döngü kurana kadar) bellekte yer kaplamaz. **Milyonlarca satırlık veride RAM şişmesin diye bu kullanılır.**

> **"İlla Tuple İstiyorum!"** dersekÇ

Generator ifadesinin başına `tuple()` yazman gerekir.

```py
# Zorla Tuple Yapmak
gercek_tuple = tuple(x for x in range(3))

print(gercek_tuple)
# Çıktı: (0, 1, 2)

```
