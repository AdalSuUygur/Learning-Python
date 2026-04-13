
# Koleksiyon (Collection) Nedir?

**Birden fazla veriyi, tek bir değişken isminin altında tutabilen veri yapılarıdır.** İçine birden fazla sayı, metin, hatta başka koliler koyabilirsin.

**Ortak Süper Güçleri:**
Koleksiyon olmanın şartı: **"Sayılabilir"** ve **"Gezilebilir"** olmalarıdır.

1. **Iterable (Gezilebilir):** Hepsinde `for` döngüsü ile elemanların üzerinde tek tek gezebilirsin.
2. **Sizeable (Ölçülebilir):** Hepsinin eleman sayısını `len()` fonksiyonu ile ölçebilirsin.
3. **Membership (Üyelik):** Hepsinde `in` operatörü ile "Bu eleman sende var mı?" (`if "ali" in liste`) diye sorabilirsin.

## Unboxing - Unpacking (Söz dizimi özelliği)

Bir koleksiyonun öğelerini alıp bu öğeleri ayrı ayrı değişkenlere atanması durumudur.

```py
my_family = [ #Bu listemiz
    ["Lale Selam", 29, "Analyst-Unemployed"],
    ["Aslı Meram", 33, "Guidance Counselor"],
    ["Karam Çalık", 37, "English Teacher"],
    ["Alık Balık", 61, "Retired"],
    ["Sade Kanık", 67, "Chauffeur"]
]

for item in my_family: #şimdi ailedeki her bir öğeyi dışarı çıkartıyoruz (bu da unboxing aslında)
    print(item) #Kısaca liste içindeki listenin dış listesinden kurtardık.
```

> **Not:** Unpacking yaparken karşılaması gereken valueların tam olması lazım, eksik veya fazla olursa patlar.

```py
for name, age, occupation in my_family: #myfamilyden bana gelen bilgileri öyle bir karşılayayım ki tık tık tık eşleşsin
    print(                              #Ki bu da unboxing bak
        f"Full name: {name}\n"
        f"Age: {age}\n"
        f"Occupation: {occupation}"
    )
```

## Koleksiyonlarda Kullanılan Built-in Methodlar

### `.split()` (Parçala)

Metni, belirlediğin bir "ayırıcıya" göre böler ve **LİSTE** döner.

```py
veri = "Python,Java,C++"
diller = veri.split(",") # Virgüle göre ayır
print(diller) # ['Python', 'Java', 'C++']
```

### `.join()` (Birleştir)

Listeyi alır, aralarına belirlediğin "yapıştırıcıyı" koyarak **STRING** (Metin) yapar.
> *Dikkat:* Yazımı biraz terstir. Önce yapıştırıcı yazılır.

```py
kelimeler = ["Veri", "Bilimi", "Harika"]
cumle = " ".join(kelimeler) # Boşluk ile birleştir
print(cumle) # "Veri Bilimi Harika"
```

## "Mahşerin 4 Atlısı": Koleksiyon Türleri

Python'da 4 ana koleksiyon tipi vardır.

| Koleksiyon | Sembol | Sıralı mı? (Ordered) | Değişir mi? (Mutable) | Tekrar Eder mi? (Duplicates) | Gerçek Hayat Analojisi |
| --- | --- | --- | --- | --- | --- |
| **List** | `[]` | ✅ Evet | ✅ Evet | ✅ Evet | **Alışveriş Listesi.** Sırası önemlidir, ekleme çıkarma yapabilirsin, aynı sütten 2 tane yazabilirsin. |
| **Tuple** | `()` | ✅ Evet | ❌ Hayır | ✅ Evet | **Kimlik Kartı.** Bilgiler sırayla bellidir ama TC kimlik numaranı sonradan değiştiremezsin (Immutable). |
| **Set** | `{}` | ❌ Hayır | ✅ Evet | ❌ Hayır | **Davetli Listesi.** Ali'yi iki kere yazsan da bir kişi sayılır (Unique). İçeride sıra yoktur. |
| **Dictionary** | `{k:v}` | ⚠️ Kısmen* | ✅ Evet | ❌ (Key'ler Unique) | **Telefon Rehberi.** Sıranın önemi yoktur, isme (key) bakarak numarayı (value) bulursun. |

**Not: Python 3.7 sonrası Sözlükler ekleme sırasını korur ama biz mantıken onlara "sırasız erişim" (anahtarla erişim) gözüyle bakarız.*

>Neden Hepsini Liste Yapmıyoruz?

Çünkü programlamada her koleksiyonun bir **amacı** ve **maliyeti** vardır.

1. **List:** "Ben her işe gelirim, esneğim" der. Ama bu esneklik **bellek (memory)** maliyeti yaratır.
2. **Tuple:** "Ben sabitim, beni değiştiremezsin" der. Bu yüzden Listeden daha **hafiftir** ve daha **hızlı** çalışır. Yanlışlıkla verinin değiştirilmesini önler (Güvenlik).
3. **Set:** "Bende tekrar olmaz" der. Matematiksel kümeler (kesişim, birleşim) yapmak için veya bir listedeki kopyaları temizlemek için kullanılır. İçinde arama yapmak Listeden çok daha **hızlıdır**.
4. **Dictionary:** "Veriyi etiketlerim" der. İlişkisel verileri (Öğrenci Adı -> Notu) tutmak için mecburuz.

```python
# 1. LIST: Sıralı, Değişir, Tekrarlı
alisveris = ["Süt", "Ekmek", "Süt"] 
alisveris.append("Yumurta") 
# ["Süt", "Ekmek", "Süt", "Yumurta"]

# 2. TUPLE: Sıralı, Değişmez (Korumalı)
koordinat = (34.5, 42.1)
# koordinat[0] = 50.0  -> HATA! Değiştiremezsin.

# 3. SET: Sırasız, Eşsiz (Unique)
davetliler = {"Ali", "Veli", "Ali"} 
# {"Ali", "Veli"} -> İkinci Ali otomatik silinir.

# 4. DICTIONARY: Anahtar-Değer
rehber = {"Ali": 5551234, "Veli": 5559876}
# rehber["Ali"] -> 5551234

```

### Mahşeerin 4 atlısı comprehension tablosu

| Yapı | Syntax | Sonuç |
| --- | --- | --- |
| **List Comp.** | `[x for x in data]` | `[1, 2, 3]` (Liste) |
| **Set Comp.** | `{x for x in data}` | `{1, 2, 3}` (Küme - Tekrarsız) |
| **Dict Comp.** | `{k:v for k,v in data}` | `{'a':1, 'b':2}` (Sözlük) |
| **Generator** | `(x for x in data)` | `<generator object>` (**Tuple Değil!**) |
| **Tuple Comp.** | `tuple(x for ...)` | `(1, 2, 3)` (Ancak böyle olur) |

## Python'un **"Özel Kuvvetleri"**

Bunlar, standart 4'lünün yetmediği veya hantal kaldığı durumlar için üretilmiş, **`collections`** adında özel bir kütüphanede (modülde) saklanan gelişmiş veri yapılarıdır.

### `Counter` (Veri Bilimcinin En İyi Dostu)

Bir listedeki elemanları saymak istiyorsun diyelim.

* **Standart Yol:** Bir sözlük açarsın, döngü kurarsın, `if` ile "varsa artır yoksa 1 yap" dersin... Ameleliktir.
* **Counter Yolu:** Tek satırda halleder.

```py
from collections import Counter

veriler = ["elma", "armut", "elma", "elma", "muz", "armut"]

# Tek satırda analiz!
sayac = Counter(veriler)

print(sayac)
# Çıktı: Counter({'elma': 3, 'armut': 2, 'muz': 1})

print(sayac.most_common(1)) 
# Çıktı: [('elma', 3)] -> En çok geçen 1 elemanı ver.

```

> **Not:** Doğal Dil İşleme (NLP) yaparken "Bu metinde hangi kelime kaç kere geçmiş?" sorusunun cevabı direkt budur.

---

### `defaultdict` (Hata Önleyici Sözlük)

Standart sözlükte olmayan bir anahtarı çağırırsan program "PATLAR" (`KeyError`) demiştik.
`defaultdict`, "Anahtar yoksa patlama, benim belirlediğim varsayılan bir değer ver" der.

```py
from collections import defaultdict

# "Eğer anahtar yoksa otomatik olarak 0 değeri ver" diyoruz (int)
stok = defaultdict(int)

stok["kalem"] += 1 
# Normal sözlük olsa burada PATLARDI (çünkü "kalem" yok).
# Ama defaultdict önce "kalem": 0 yapıyor, sonra 1 ekliyor.

print(stok["kalem"]) # Çıktı: 1
```

### `namedtuple` (Okunabilir Demetler)

Tuple'lar hızlıdır ama `koordinat[0]` neydi, `koordinat[1]` neydi hatırlamak zordur.
`namedtuple`, elemanlara isim vermeni sağlar.

```py
from collections import namedtuple

# Şablon oluşturuyoruz
Ogrenci = namedtuple('Ogrenci', ['isim', 'notu', 'bolumu'])

# Veri giriyoruz
ogr1 = Ogrenci("Su", 95, "Veri Bilimi")

# Artık indekse mahkum değiliz!
print(ogr1.isim)  # Çıktı: Su (ogr1[0] demek yerine)
print(ogr1.notu)  # Çıktı: 95
```

## List vs Tuple vs Set

| Özellik | List `[]` | Tuple `()` | Set `{}` |
| --- | --- | --- | --- |
| **Sıralama** | Sıralıdır (Index vardır) | Sıralıdır (Index vardır) | **Sırasızdır** (Index yoktur!) |
| **Değiştirilebilirlik** | Mutable (Değişebilir) | Immutable (Değişmez) | **Mutable** (Eleman eklenip çıkarılabilir) |
| **Tekrar Eden Veri** | İzin verir | İzin verir | **İZİN VERMEZ!** (Duplicate yasak) |
| **Hız** | Orta | Hızlı (Okuma) | **Çok Hızlı** (Arama/Varlık kontrolü) |

## 1. CRUD Nedir?

**CRUD**, herhangi bir kalıcı veri sisteminin (Veritabanı, API, Excel Dosyası vb.) yapması gereken **4 temel işlemin** baş harfleridir.

Bir uygulamanın (Instagram, LinkedIn, E-Ticaret sitesi) "yaşayabilmesi" için bu 4 şeyi yapabilmesi gerekir:

| Harf | İngilizce | Türkçe | Anlamı | QA/Veri Bilimi Karşılığı |
| --- | --- | --- | --- | --- |
| **C** | **Create** | Oluştur | Sisteme yeni veri eklemek. | Yeni kullanıcı kaydı açmak. |
| **R** | **Read** | Oku | Var olan veriyi görüntülemek. | Kullanıcı profilini görüntülemek. |
| **U** | **Update** | Güncelle | Var olan veriyi değiştirmek. | Şifre değiştirmek, adres güncellemek. |
| **D** | **Delete** | Sil | Veriyi sistemden kaldırmak. | Hesabı kapatmak. |

---

> **Neden Önemli?** (QA ve Veri Bilimi Gözüyle)

### Veri Temizliği (Data Cleaning)

* Gelen verilerde bozuk datalar olacaktır.
* Yeni özellikler (sütunlar) ekleme -> **Create**
* Gelen dataları okumak -> **Read**
* Eksik verileri doldurma -> **Update**
* Hatalı satırları silmek -> **Delete**

### Koleksiyonlarda CRUD

| Veri Yapısı | Create (Ekle) | Read (Oku) | Update (Güncelle) | Delete (Sil) |
| --- | --- | --- | --- | --- |
| **LIST** `[]` | ✅ (`append`) | ✅ (`[index]`) | ✅ (`[i]=yeni`) | ✅ (`pop`, `remove`) |
| **DICT** `{}` | ✅ (`[key]=val`) | ✅ (`[key]`) | ✅ (`[key]=yeni`) | ✅ (`pop`) |
| **SET** `{}` | ✅ (`add`) | ❌ *(İndeks yok)* | ❌ *(İndeks yok)* | ✅ (`remove`) |
| **TUPLE** `()` | ⚠️ *(Baştan)* | ✅ (`[index]`) | ❌ **(Immutable)** | ❌ **(Immutable)** |

**Tam anlamıyla CRUD yapabileceğimiz** sadece iki yapı var: **Listeler** ve **Sözlükler.**
