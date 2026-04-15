
# VARIABLES, DATA TYPES AND MEMORY

Bilgisayar Nasıl "Hatırlar"?
Bilgisayar beyni = CPU _yani işlem yapma gücü_
Bilgisayarın herhangi bir bilgiyi aklında tutması için Random Access Memory (RAM) denilen "kısa süreli hafızasına" ihtiyacı vardır.

Bilgisayarın beyni (CPU) işlem yapar ama hafızası yoktur. Bir şeyi aklında tutması için RAM (Random Access Memory) dediğimiz, bilgisayarın "kısa süreli hafızasına" ihtiyacı vardır.

Biz kod yazarken, elimizdeki verileri (sayılar, isimler) belli adreslere koyuyoruz.
Ancak, her seferinde "Git ABC adresindeki veriyi getir" demek imkansızdır. İşte burada devreye **Değişkenler** girer.

## Variables (Değişkenler)

Python'da bir değişken yarattığında aslında bilgisayara şunu söylersin: "Bana bellekte bir yer ayır, içine bu veriyi koy ve bu yere ulaşmam için bana 'x' isminde bir etiket ver."

> **Önemli Not:** Programlama dillerinde, değişken (variable), verileri geçici olarak saklamak için kullanılan, isimlendirilmiş bir bellek alanıdır. Kodlamadaki her şeyin temelidir.

Değişkenler, genellikle bilgisayarın RAM'inde tutulur ve program çalıştığı sürece o veriyi barındırır.\
Değişkenin adı, programda runtime'da çalıştırılır.

### Değişkenlerin Kullanım Şekilleri

* Atama: Bir değişken tanımlandığında, ona bir değer (value) atanır (Örn: `x = 10`).
* Çağırma: Programın herhangi bir anında, o değişkene atanan değeri kullanmak için adını çağırırız.

Değişkenler, bir programın dinamik olmasını sağlayan temel araçtır. Bir değişken şu durumlarda kullanılır:

1. _Veriyi Saklamak:_ Kullanıcıdan alınan girdiyi (isim, yaş), bir hesaplama sonucunu veya bir dosyanın içeriğini saklamak için.
2. _Veriyi İşlemek:_ Saklanan değerler üzerinde matematiksel işlemler yapmak veya metinleri düzenlemek için.
3. _Tekrar Kullanılabilirlik:_ Aynı değeri kodun birden fazla yerinde kullanmak gerektiğinde, o değeri tekrar tekrar yazmak yerine değişkenin adını kullanmak için.
4. _Mantıksal Karar Verme:_ `True` veya `False` gibi boolean değerler tutarak (`is_active = True`), programın `if/else` blokları ile hangi yolu seçeceğine karar vermek için.

```py
yas = 25
isim = "Deniz"
#Burada yas bir etikettir ve bellekte 25 sayısının durduğu yeri işaret eder.
```

### Değişken Tanımlarken Dikkat Edilecek Hususlar (Kurallar)

| **Husus** | **Açıklama** | **Örnek** |
| --------- | --------- | --------- |
| DO NOT start with a number | Değişlen ismi asla rakam (sayı) ile başlayamaz. Ancak, rakamlar değişkenin içinde veya sonunda kullanılabilir. | ❌ 1sayi</p> ❌ 3boyut</p> ✅ sayi1</p> ✅ boyut3</p> |
| Boşluk yerine Ayırıcı (Best Practice) | Değişken isimleri boşluk içeremez. Birden fazla kelimeden oluşan isimlerde Python'da alt çizgi (_) tercih edilir (snake_case).</p> | ❌ kullanici adi</p> ✅ kullanici_adi</p> ✅ toplam_fiyat</p> |
| Türkçe Karakter | Türkçe karakterler (`ç, ğ, ı, ö, ş, ü`) kullanılması kesinlikle önerilmez. Evrensel uyumluluk için İngilizce karakterler kullanılmalıdır. | ❌ sipariş_no</p> ✅ siparis_no</p> |
| Anahtar Kelimeler | Python'ın yerleşik anahtar kelimeleri (`if`, `for`, `while`, `print`, `type` vb.) değişken adı olarak kullanılamaz. | ❌ `def`, ❌ `class` |

## Data Types (Veri Tipleri)

_Kutunun İçinde Ne Var?_

Python, kutunun (değişkenin) içine ne koyduğuna çok önem verir.
Çünkü bir sayıyla matematik yapabilirsin ama bir isimle çarpma işlemi yapamazsın (en azından matematiksel olarak).

Değişkenlerin bellekte tuttuğu verinin **doğası ve türüdür**. Python'da her değerin bir tipi vardır. Veri biliminde doğru sonuçları elde etmek için verinin tipini (sayı mı, metin mi, liste mi) bilmek hayati önem taşır. `type()` Built-in Function'ı, bir değişkenin tipini kontrol etmek için kullanılır.

| Tip Adı | Açıklama | Örnek | Veri Bilimi Önemi |
| :--- | :--- | :--- | :--- |
| **Integer (`int`)** | Tam sayılar (pozitif, negatif, sıfır). | `yas = 30` | Sayma, diskret (kesikli) değişkenler (Örn: ürün adedi). |
| **Float (`float`)** | Ondalıklı sayılar. | `ortalama = 4.25` | Sürekli değişkenler (Örn: sıcaklık, fiyat), Makine Öğrenimi hesaplamalarının çoğu (Örn: $3.14159$). |
| **String (`str`)** | Metinler ve karakter dizileri (tırnak içinde). | `isim = "Su"` | Kategorik veriler, doğal dil işleme (NLP). |
| **Boolean (`bool`)** | Mantıksal doğruluk değeri (`True` veya `False`). | `is_active = True` | Kontrol akışı (`if/else`), veri filtreleme. |

---

### String Repetition (String Tekrarı)

Çarpma (*): Bir kelimeyi 3 ile çarpmak demek, mantıken o kelimeyi "3 katına çıkarmak" yani tekrarlamak demektir. Burada belirsizlik yok. Bu yüzden matematiksel ifadelerde çarpma operatörü çalışır.

```py
print("-" * 20) 
# Çıktı: --------------------
# (Genelde konsolda ayırıcı çizgi çekmek için çok kullanırız)
```

### Integer Immutability

**Immutability**, Türkçe karşılığıyla **"Değişmezlik"** demektir.

Python'da "Integer'lar (Tam sayılar) immutable'dır" dediğimizde şunu kastediyoruz:

> **Bir sayı nesnesi (örneğin `5`) bellekte bir kez oluşturulduğunda, onun içeriğini ASLA değiştiremezsin.**

```py
x = 10
x = x + 1
```

Normalde insan mantığı şöyle düşünür:\
"x kutusunun içindeki 10'u sildim, yerine 11 yazdım."\
**AMA PYTHON'DA OLAN ŞUDUR:**

1. **`x = 10`**: Python bellekte bir adreste (örneğin Adres A) **`10`** nesnesini oluşturur. `x` etiketini oraya yapıştırır.
2. **`x + 1` işlemi**: Python bakar, `x` 10'u gösteriyor. 10 ile 1'i toplar ve sonuç **`11`** olur.
3. **Kritik An:** Python, Adres A'daki `10` sayısını `11`'e dönüştürmez! (Çünkü Integer imutabledır, değişmez).
4. **Yeni Nesne:** Python gider, belleğin bambaşka bir yerinde (Adres B) yepyeni bir **`11`** nesnesi oluşturur.
5. **Etiket Taşıma:** Sonra `x` etiketini Adres A'dan söker, Adres B'deki `11`'e yapıştırır.
6. **Eski Sayı:** Adres A'daki `10` artık etiketsiz kalır (eğer başka bir değişken onu göstermiyorsa) ve Çöp Toplayıcı (Garbage Collector) tarafından temizlenir.

#### Avantajları

1. **Güvenlik:** Sayıların değişmeyeceğinden emin olduğun için, programın farklı yerlerinde aynı `5` sayısını güvenle kullanabilirsin. Kimse o `5`'i gizlice `6` yapamaz.

2. **Hız (Small Integer Caching):** Python, en sık kullanılan küçük sayıları (genellikle -5 ile 256 arası) program açılır açılmaz bellekte hazır tutar (önbellekler). Sen `a = 5` dediğinde yeni bir 5 yaratmaz, zaten rafta hazır duran `5`'e etiket yapıştırır. Bu da muazzam bir hız kazandırır.

>**Özetle:** Integer Immutability, "Bir sayıyı değiştirmek istediğinde aslında yenisini yaratırsın" kuralıdır.

### Duck Typing

Python özelinde ise _değişkenler içerisine atılan değerin tipine bürünürler, önceden tanımlama gerektirmezler._ Buna _**duck typing**_ denir.

Python'ın dinamik tiplendirmesinin bir uzantısıdır.\
Temel felsefesi şudur:

* _"Eğer bir şey ördek gibi yürüyorsa ve ördek gibi vaklıyorsa, onun ne olduğunun önemi yok, o bir ördektir."_

```python
x = 10 #integer
y = 3.14 #float
is_active = True #boolean
isim = "Su" #string
```

## Memory (Bellek)

Sen veri bilimci olacaksın, işin hafıza (memory) kısmını iyi anlamalısın!!

Diğer bazı dillerde (C, Java gibi) değişken gerçekten bir kutudur. İçine 5 koyarsın, sonra 10 koyarsın. Python'da ise değişken bir "Etiket"tir.

Şu senaryoya bakalım:

```python
a = 10
b = a
a = 20
```

Adım Adım Bellekte Ne Oluyor?

1. a = 10: Python bellekte bir yerde "10" nesnesi oluşturur. a etiketi oraya yapışır.

2. b = a: b etiketi, a'nın gösterdiği yere (yani "10" nesnesine) yapışır. Şu an hem a hem b aynı "10"u gösteriyor.

3. a = 20: Python bellekte YENİ bir "20" nesnesi oluşturur. a etiketini "10"dan söküp "20"ye yapıştırır.

**Soru:** b şu an kaçtır?

**Cevap:** b hala "10"u gösteriyor. Çünkü biz b'yi değiştirmedik, sadece a'nın etiketini başka yere taşıdık.

> **Öğretmen Notu:** Veri biliminde bu hatayı en çok dosya okurken alacaksın. Excel'den veri çekeceksin, sayı gibi görünen sütunlar aslında "string" olarak gelecek. Onları int() veya float() ile çevirmeden analiz yapamayacaksın.

## Modülden Fonksiyon Çağırma

```python
from random import randint
```

Bu fonksiyon python içinde tanımlıdır ancak direkt kullanılamaz, kullanılmak istenildiğinde import edilmeli.

> **import random** -> olduğu gibi modülü importlar.
> **from random import randint** -> burada ise random modülünden sadece randint fonksiyonu impotlanır, yani daha az maliyetli.

* Bir modülden 1-2 fonksiyon çağırılacaksa spesifik olarak fonksiyonları çağırmak daha doğru çünkü daha az maliyetli.
* Bir modülden 10 tane fonksiyon çağırılacaksa direkt modülün çağırılması daha doğru çünkü daha az iş gücü.
