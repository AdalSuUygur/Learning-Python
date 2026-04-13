
# CUSTOM FUNCTIONS

Yazılımda **DRY (Don't Repeat Yourself - Kendini Tekrar Etme)** diye kutsal bir kural vardır.
Eğer bir kodu kopyalayıp yapıştırıyorsan, orada bir hata yapıyorsun demektir.
Fonksiyonlar, bizi bu amelelikten kurtaran sihirli kutulardır.

## Fonksiyon Yazmanın Avantajları

**SRP (Single Responsibility Principle)**
**SoC (Separation of Concern)** kavramları işin felsefesidir.
> Eğer bir oyuncak robot hem şarkı söylüyor, hem yürüyor, hem de çay demliyorsa; şarkı söyleme mekanizması bozulduğunda tamir ederken yanlışlıkla çay demleme özelliğini de bozabilirsin.

* **Tekrarı Önler (DRY):** Mail adresi oluşturma kodunu 50 farklı yere kopyalamak yerine, bir fonksiyon yazarsın, 50 yerde onu çağırırsın.

* **Bakımı Kolaylaştırır:** Yarın patron geldi, "Mail adresleri artık `@outlook.com` değil `@company.com` olacak" dedi.
* *Fonksiyonsuz:* 50 dosyayı açıp tek tek değiştirmen lazım.
* *Fonksiyonlu:* Sadece fonksiyonun içindeki tek satırı değiştirirsin, her yer güncellenir.
* **Böl, Parçala, Yönet:** 1000 satırlık dev bir kod bloğunu kimse okuyamaz. Ama bunu 10 tane küçük fonksiyona bölersen (Veri Al, Hesapla, Kaydet vb.), kod şiir gibi okunur.

## SYNTAX

Python'da fonksiyon tanımlamak (define), bilgisiyara yeni bir kelime öğretmek gibidir.

```py
#(1)     (2)               (3)
def mail_olustur(isim: str, soyisim: str):
    """
    (4) Docstring: Bu fonksiyon isim ve soyisimden mail oluşturur.
    """
    # (5) Body (Gövde)
    mail = f"{isim}.{soyisim}@sirket.com".lower()
    
    # (6) Return (Çıktı)
    return mail
```

1. **`def`:** "Define" (Tanımla) kelimesinin kısaltması. Python'a "Bak şimdi sana yeni bir komut öğretiyorum" demektir.
2. **`mail_olustur` (Fonksiyon Adı):** Fonksiyonun ismi. `snake_case` (küçük harf ve alt tire) kullanılır. Yaptığı işi anlatmalıdır (`x`, `y` gibi isimler verilmez).
3. **`(isim, soyisim)` (Parametreler):** Fonksiyonun çalışmak için ihtiyaç duyduğu hammaddeler.
4. **`Docstring`:** Fonksiyonun kullanma kılavuzudur. Notlarında `"""..."""` içinde gördüğün kısım. (Autodocs eklentisi burada devreye girer).
5. **Body (Gövde):** Asıl işin yapıldığı, girintili (indented) alan.
6. **`return`:** Fonksiyonun sonucu dışarı fırlattığı yer. (Buna aşağıda detaylı değineceğim).

> **Type Hinting (Tip İpuçları):** `def sum_two_number(a: int, b: int):`
> Python'da zorunlu değildir ama "Senior" alışkanlığıdır. `a`'nın integer olması gerektiğini okuyan kişiye (ve editöre) söyler. Kodun kalitesini artırır.

## Parametre vs Argüman

* **Parametre (Parameter):** Fonksiyonu **yazarken** parantez içine koyduğun değişken isimleridir (Boş koltuklar).

> `def topla(a, b):` -> Burada `a` ve `b` parametredir.

* **Argüman (Argument):** Fonksiyonu **çağırırken** o boş koltuklara oturttuğun gerçek değerlerdir.

> `topla(5, 10)` -> Burada `5` ve `10` argümandır.

## Default (Varsayılan) Değer

Buna "Opsiyonel Parametre" de denir. Kullanıcı değer vermezse, bizim belirlediğimiz "B Planı" devreye girer.

```py
# domain verilmezse otomatik olarak "gmail.com" kabul eder.
def create_mail(name, domain="gmail.com"): 
    print(f"{name}@{domain}")

create_mail("su")                  # Çıktı: su@gmail.com (Default çalıştı)
create_mail("su", "yahoo.com")     # Çıktı: su@yahoo.com (Bizimki ezildi)
```

> **Kritik Kural:** Default değeri olan parametreler, **EN SONA** yazılmalıdır.
> `def islem(a=1, b):` ❌ YANLIŞ!
> `def islem(b, a=1):` ✅ DOĞRU!

## Return vs Unreturnable

* **`print()`:** Sadece ekrana yazı yazar. O veriyi alıp matematikte kullanamazsın. ATM'nin ekranında bakiyeni görmek gibidir.

* **`return`:** Fonksiyon sonucu sana fiziksel olarak geri verir (döndürür). ATM'nin parayı sana vermesi gibidir. O parayla (veriyle) gidip başka şeyler alabilirsin.

```py
def topla_print(a, b):
    print(a + b)  # Sadece gösterir

def topla_return(a, b):
    return a + b  # Değeri verir

# Senaryo: Sonucu 2 ile çarpmak istiyorum.
x = topla_print(3, 5) # Ekrana 8 yazar ama x'in içi BOŞTUR (None).
# print(x * 2) -> HATA VERİR! (None ile sayı çarpılmaz)

y = topla_return(3, 5) # y'nin değeri artık 8'dir.
print(y * 2) # Çıktı: 16 (İşte return gücü!)
```

## *args ve **kwargs

>**`*args`** ve **`**kwargs`** operatörleri fonksiyonlara **"Esneklik"** kazandıran süper güçlerdir.

### `*args`: Positional Arguments Packing (Konum Bazlı Paketleme)

Fonksiyonu tanımlarken parametrenin başına `*` koyduğunda Python'a şunu söylersin:
*"Bu fonksiyona, tanımladığım standart parametrelerden sonra gelen tüm **isimsiz (positional)** argümanları topla ve onları tek bir **TUPLE** haline getir."*

**Neden List değil de Tuple?**
Çünkü Python, fonksiyon çağrıldığında gönderilen argümanların güvenliğini sağlamak ister. Tuple'lar **immutable** (değiştirilemez) olduğu için, `args` içine giren verilerin fonksiyon içinde kazara değiştirilmesini (append/remove) engeller. Bu, bellek yönetimi açısından daha hafiftir.

>**Mantığı:** "Kaç tane değer geleceğini bilmiyorum, ne gelirse hepsini bir torbaya (Tuple) doldur."
>**Sembolü:** Tek Yıldız (`*`). Asıl işi yapan budur. `args` sadece bir isim geleneğidir, istersen `*sayilar` da diyebilirsin.

**Örnek (Hesap Makinesi):**
Eskiden olsa 3 sayı için ayrı, 5 sayı için ayrı fonksiyon yazardın. Şimdi:

```py
def hepsini_topla(*sayilar):
    print(f"Gelen veri tipi: {type(sayilar)}") # Tuple olduğunu görelim
    print(f"Gelen veriler: {sayilar}")
    
    toplam = 0
    for sayi in sayilar:
        toplam += sayi
    return toplam

# İstediğin kadar argüman gönder!
print(hepsini_topla(10, 20))           # Çıktı: 30
print(hepsini_topla(1, 2, 3, 4, 5))    # Çıktı: 15
```

### `**kwargs`: Keyword Arguments Packing (Anahtar Kelime Bazlı Paketleme)

Fonksiyon tanımında `**` kullandığında Python'a şunu dersin:
*"Standart parametrelerle eşleşmeyen, ama `key=value` formatında gönderilen tüm argümanları topla ve bir **DICTIONARY (Sözlük)** haline getir."*

Burada veri yapısı **Dictionary** olmak zorundadır çünkü verinin bir etiketi (key) ve bir değeri (value) vardır.

>**Mantığı:** "Kaç tane özellik geleceğini bilmiyorum. Kullanıcı `anahtar=değer` şeklinde ne gönderirse hepsini bir kutuya (Dictionary) doldur."
>**Sembolü:** Çift Yıldız (`**`).

**Örnek (Kullanıcı Profili):**
Her kullanıcının farklı bilgileri olabilir.

```py
def profil_olustur(**bilgiler):
    print(f"Gelen veri tipi: {type(bilgiler)}") # Dict olduğunu görelim
    print(f"Gelen veriler: {bilgiler}")
    
    # Sözlük olduğu için .get() ile veriyi çekebiliriz
    if 'isim' in bilgiler:
        print(f"Merhaba {bilgiler['isim']}!")

# 1. Kullanıcı: Sadece isim ve yaş
profil_olustur(isim="Su", yas=29) 
# Çıktı: {'isim': 'Su', 'yas': 29}

# 2. Kullanıcı: İsim, meslek, şehir, medeni durum...
profil_olustur(isim="Ali", meslek="Mühendis", sehir="İstanbul", evli_mi=True)
# Çıktı: {'isim': 'Ali', 'meslek': 'Mühendis', 'sehir': 'İstanbul', 'evli_mi': True}

```

### Altın Kural

Eğer bir fonksiyonda hem normal parametre, hem `*args`, hem de `**kwargs` kullanacaksan sıra **ASLA** değişmez:

1. Normal Parametreler (Standart)
2. `*args` (Tuple toplayıcı)
3. `**kwargs` (Sözlük toplayıcı)

```py
# DOĞRU SIRALAMA ✅
def islem(baslik, *sayilar, **ayarlar):
    print(baslik)   # Normal
    print(sayilar)  # Tuple
    print(ayarlar)  # Dict

islem("Test", 10, 20, 30, renk="kırmızı", mod="hızlı")

```

**Neden?** Çünkü Python okumaya soldan başlar.

1. İlk geleni `baslik`'a atar.
2. Geriye kalan isimsiz sayıları `*sayilar` torbasına atar.
3. En sonda `isim=değer` şeklinde olanları `**ayarlar` kutusuna koyar.

### Kim Operatör, Kim Değil?

>**Not:** Yıldız sembolleri (`*` ve `**`) birer operatördür. Ancak burada küçük bir nüans var. Kelimeler (`args`, `kwargs`) operatör değildir, başlarındaki **semboller** operatördür.

* **`*` (Yıldız):** Bu bir operatördür. Python literatüründe buna **"Unpacking Operator"** (Paket Açma Operatörü) denir.
* **`**` (Çift Yıldız):** Bu da bir operatördür. Buna da **"Dictionary Unpacking Operator"** denir.
* **`args` / `kwargs`:** Bunlar operatör **DEĞİLDİR**. Bunlar sadece senin o pakete verdiğin **değişken isimleridir** (Identifier). İstersen `*kutu` veya `**cantam` da diyebilirdin.

### Bukalemun Operatörler

Bu operatörler "Bağlama Duyarlıdır" (Context Sensitive). Yani nerede durduklarına göre kimlik değiştirirler.

**A. Matematik Sahnesinde (Arithmetic Operator)**
Sayıların arasındaysa matematik yapar.

* `3 * 5` -> Çarpma Operatörü.
* `3 ** 5` -> Üs Alma (Kuvvet) Operatörü.

**B. Koleksiyon Sahnesinde (Unpacking Operator)**
Listenin veya fonksiyonun başındaysa **Paketleme/Dağıtma** yapar.

* `*args` -> Toplama/Paketleme Operatörü.
