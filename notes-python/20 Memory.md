
# MEMORY & OOP

## Memory Management: Stack vs. Heap (Bellek Mimarisi)

Yazılım çalıştığında işletim sistemi, sürece (process) sanal bir bellek alanı tahsis eder. Bu alanın yönetimi hayati önem taşır.

### A. The Stack (Yığın) – "Execution Context"

Burası "Static Memory Allocation" (Statik Bellek Tahsisi) alanıdır. Programın çalışma akışını (execution flow) yönetir.\
**Tanım:** "Last In, First Out" (LIFO - Son giren ilk çıkar) mantığıyla çalışan, hızlı erişimli bellek bölgesidir.

**Ne tutulur?** Fonksiyon çağrıları, **lokal değişkenlerin referansları** ve programın "nerede kaldığı" bilgisi (Return Address).

### B. The Heap (Öbek) – "Dynamic Memory"

Burası "Dynamic Memory Allocation" (Dinamik Bellek Tahsisi) alanıdır. Boyutu çalışma zamanında (runtime) değişebilen veriler içindir.\
**Tanım:** Dinamik olarak yönetilen, büyük ve karmaşık veri yapıları için kullanılan bellek havuzudur.

* **Ne tutulur?** `User()`, `List`, `Dictionary` gibi nesnelerin **kendisinin (datalarının)** fiziksel olarak bulunduğu yerdir.
* **Maliyet:** Erişimi Stack'e göre daha yavaştır çünkü boş bir alan bulmak (allocation) ve temizlemek (de-allocation) maliyetlidir.

> **Özet İlişki:** Nesnenin kendisi **Heap**'te, o nesneye ulaşmamızı sağlayan adres çubuğu veya basit değerler **Stack**'te durur.

## 2. Object Lifecycle (Nesne Yaşam Döngüsü)

Bir insan doğar, bir isim alır, yaşar, çalışır ve sonunda hayatı sona erer. Yazılımda bir nesnenin (object) hikayesi de birebir böyledir.\
**Nesne Yaşam Döngüsü (Object Lifecycle)**, bir nesnenin bilgisayarın hafızasında (RAM) yaratıldığı andan, silindiği ana kadar geçen süreçtir.

### 1. Evre: Yaratılış (Creation / Allocation)

* **Kod:** `x = Araba()` yazdığın an.
* **Olay:** Henüz ortada "kırmızı" veya "hızlı" bir araba yoktur. Sadece RAM'in **Heap** bölgesinde, o arabanın sığacağı kadar boş bir arsa (bellek alanı) ayrılır.
* **Python'daki Karşılığı (`__new__`):** Pek çok kişi bilmez ama `__init__`'ten önce `__new__` metodu çalışır. Bu metod, boş objeyi (boş arsayı) yaratır ve geri döndürür.

### 2. Evre: Başlatma (Initialization)

* **Kod:** `__init__` metodunun çalıştığı an.
* **Olay:** Boş arsaya evin odaları yapılır, boyası sürülür. Yani objeye ilk değerleri (`self.renk = "Kırmızı"`, `self.model = 2023`) verilir.
* **Python'daki Karşılığı (`__init__`):** Burası "Constructor" (Yapıcı) gibi görünse de aslında "Initializer" (Başlatıcı) dır. Nesne zaten 1. evrede yaratılmıştır, burada sadece içi doldurulur.

### 3. Evre: Kullanım (Usage / Manipulation)

* **Kod:** `x.gaz_ver()`, `print(x.renk)` dediğin anlar.
* **Olay:** Nesne artık canlıdır. Programın içinde oradan oraya taşınır, fonksiyonlara parametre olarak girer, üzerindeki değerler değişir.
* **Hayatta Kalma Kuralı:** Bir nesne, **en az bir kişi** (değişken) onun ipini (referansını) tuttuğu sürece hayatta kalır.

### 4. Evre: Yok Oluş (Destruction / Finalization)

* **Kod:** `del x` dediğinde veya program bittiğinde.
* **Olay:** Nesnenin ipini tutan kimse kalmaz (Reference Count = 0). Python'un Çöpçüsü (Garbage Collector) gelir ve "Bu ev artık kullanılmıyor" diyerek arsayı temizler. Hafızayı geri alır.
* **Python'daki Karşılığı (`__del__`):** Nesne silinmeden hemen önce (son bir vasiyet gibi) bu metod çalışır. Genelde dosya kapatmak veya veritabanı bağlantısını kesmek için kullanılır.

### Garbage Collection (GC) - Çöp Toplayıcı

Garbage Collector'ın (Çöp Toplayıcı - GC) yaptığı işi en basit haliyle şöyle özetleyebiliriz: **"Kimsenin işine yaramayanı bul ve yer aç."**

* **Görevi:** Artık hiçbir referansın işaret etmediği (boşa düşmüş/kullanılmayan) nesneleri tespit edip silmek ve belleği boşaltmaktır.

Bir restoranda çalıştığını düşün. Masalar (RAM) sınırlı. Müşteriler (Objeler) masalara oturuyor. Sen (Garbage Collector) garson şefisin. Senin görevin, müşterisi kalkıp gitmiş masaları tespit edip, üzerindeki kirli tabakları toplayıp masayı **yeni gelecek müşteriler için boşaltmaktır.**

### 1. Takip Etme (Monitoring / Reference Counting)

Python'da GC'nin en temel silahı **"Referans Sayma" (Reference Counting)** yöntemidir. GC, her objenin sırtına görünmez bir numaratör yapıştırır.

* Kodunda `a = Araba()` dedin.
* **GC:** "Hımm, bu Araba objesini 'a' değişkeni tutuyor. Numaratör: **1**."

* Sonra `b = a` dedin.
* **GC:** "Şimdi 'b' de tutuyor. Numaratör: **2**."

* Sonra `del a` dedin (veya fonksiyon bitti, `a` silindi).
* **GC:** "'a' gitti. Numaratör: **1**." (Hala silmez, çünkü `b` tutuyor.)

### 2. Tespit Etme (Detection)

GC'nin "Harekete Geçtiği" an, o numaratörün **0 (Sıfır)** olduğu andır.

* En son `b = None` dedin.
* **GC:** "Numaratör: **0**! Tamamdır, bu Araba objesini artık programda hiç kimse tutmuyor. Bu bir ÇÖP."

* **Kritik Sorun: Tight Coupling (Sıkı Bağlılık):**
* Eğer nesneler birbirine çok sıkı ve karmaşık bağlarla bağlıysa, GC hangisinin silineceğine karar vermekte zorlanır.
* **Sonuç:** Memory Leak (Bellek Sızıntısı) riski artar. Nesnelerin yaşam döngüsünü doğru yönetmek yazılımcının sorumluluğundadır.

### 3. Geri Kazanma (Reclaiming Memory)

Numaratör 0 olduğu milisaniyede GC şunları yapar:

1. **Vasiyeti Yerine Getir:** Eğer objenin içinde `__del__` metodu varsa onu son kez çalıştırır (Dosyayı kapat, bağlantıyı kes vs.).
2. **Yıkım:** Objenin RAM'deki (Heap alanındaki) kaydını siler.
3. **İade:** O boşalan bellek alanını işletim sistemine veya Python'un boş havuzuna geri verir. Artık oraya yeni bir obje (mesela yeni bir `Ucak` objesi) kurulabilir.

## Function Execution Context: Stack ve Frame Yapısı

Python'da bir fonksiyon çağrıldığında işlemci seviyesindeki Stack ile Python yorumlayıcısının (CPython) yönettiği Stack kavramlarını ayırt etmek gerekir. Python bir sanal makine (Virtual Machine) üzerinde çalışır ve kendi yığın yapısını (call stack) yönetir.

* **Frame (Çerçeve):** Her fonksiyon çağrısı bellekte yeni bir "Frame" oluşturur. Bu frame, o fonksiyonun çalışması için gereken tüm yerel bağlamı (context) tutar.
* **PyFrameObject:** CPython tarafında her frame aslında bir C yapısıdır (`struct`). İçinde şunlar bulunur:
* **Code Object:** Fonksiyonun bytecode'ları (derlenmiş kod).
* **Local Variables:** Fonksiyon içindeki değişkenler (`f_locals`).
* **Global Context:** Global değişkenlere referanslar (`f_globals`).
* **Instruction Pointer (IP):** O an hangi bytecode satırının çalıştırıldığı.
* **Caller Reference:** Bu fonksiyonu çağıran bir önceki frame'e (back pointer) olan bağlantı.

**Stack Akışı:**
Fonksiyon çağrıldığında frame yığına (Stack) "push" edilir. `return` görüldüğünde veya fonksiyon bittiğinde frame "pop" edilir ve kontrol bir önceki frame'e geçer. Stack boyutu sınırlıdır (Recursion Limit), bu sınır aşılırsa `RecursionError` alırsın.

**Mid-Level İpucu:** `inspect` modülü ile bu frame'leri canlı inceleyebilirsin:

## Data Types in Memory: Immutable vs. Mutable

Python'da her şey bir nesnedir (Everything is an Object). C seviyesinde hepsi `PyObject` yapısından türemiştir. Bellekteki davranışları "Değişmezlik" (Immutability) kavramına göre ikiye ayrılır.

**A. Immutable (Değiştirilemez) Tipler: `int`, `str`, `tuple`, `bool**`
Bu tiplerdeki bir nesne oluşturulduğunda, içeriği bellekte asla değiştirilemez.

* `x = 10` dedin.
* `x = x + 1` dediğinde, Python 10 değerini 11 yapmaz.
* **Ne olur?** Bellekte yeni bir `11` nesnesi oluşturulur ve `x` etiketi artık bu yeni adresi gösterir. Eski `10` nesnesi sahipsiz kalır (eğer başka referans yoksa GC temizler).

**B. Mutable (Değiştirilebilir) Tipler: `list`, `dict`, `set**`
Bu nesneler "yerinde" (in-place) değiştirilebilir.

* `liste = [1, 2]` dedin.
* `liste.append(3)` dediğinde, `liste` değişkeninin bellek adresi (pointer) değişmez.
* **Ne olur?** Bellekteki listenin *içeriği* güncellenir.

**Kritik Fark (Interning):**
Python, performans için küçük tamsayıları (-5 ile 256 arası) ve bazı stringleri önbelleğe alır (Interning).

## Reference Types: "Call by Object Reference"

Bu konu en çok kafa karıştıran kısımdır. Python ne "Pass by Value" (Değer ile) ne de tam olarak C++'taki gibi "Pass by Reference" (Referans ile) kullanır. Python'un kullandığı yöntem: **Call by Object Reference** (veya *Call by Assignment*).

Mantık şudur: Fonksiyona değişkenin kendisi değil, değişkenin işaret ettiği **nesnenin referansı** kopyalanarak gönderilir.

**Senaryo 1: Immutable Nesne Göndermek**
Eğer fonksiyona bir tamsayı (int) gönderip içeride değiştirirsen, dışarıdaki değişken etkilenmez. Çünkü `int` immutable'dır; içerideki atama işlemi yeni bir nesne yaratır, sadece içerideki yerel değişkenin yönünü değiştirir.

**Senaryo 2: Mutable Nesne Göndermek**
Eğer fonksiyona bir liste gönderirsen ve `.append()` gibi metotlar kullanırsan, dışarıdaki liste de **değişir**. Çünkü referans aynıdır ve nesne yerinde değiştirilebilir.

### 4. Garbage Collector Algorithms

Python bellek yönetimini otomatize eder. Bunu sağlamak için iki ana mekanizma birlikte çalışır:

#### A. Reference Counting (Referans Sayma) - Ana Mekanizma

Python'daki her nesnenin (C struct seviyesinde `ob_refcnt`) bir sayacı vardır.

* Bir değişkene atandığında sayaç +1 artar.
* Bir listeye eklendiğinde +1 artar.
* `del` ile silindiğinde veya kapsam (scope) dışına çıkıldığında -1 azalır.
* **Sayaç 0 olduğunda:** Python bellek yöneticisi o nesneyi *anında* yok eder ve belleği iade eder.

#### B. Generational Garbage Collection (Nesilsel Çöp Toplama) - Yardımcı Mekanizma

Referans saymanın çözemediği tek bir sorun vardır: **Cyclic References (Döngüsel Referanslar)**.
Örnek: `A` nesnesi `B`'yi, `B` nesnesi `A`'yı gösteriyor. İkisi de silinse bile birbirlerini tuttukları için referans sayıları asla 0 olmaz (Memory Leak).

Bunu çözmek için "Generational GC" devreye girer. Python nesneleri 3 nesile ayırır:

1. **Generation 0 (Gençler):** Yeni oluşturulan tüm nesneler buraya girer. GC en sık burayı tarar.
2. **Generation 1 (Orta Yaş):** Gen 0 taramasından sağ kurtulanlar buraya terfi eder.
3. **Generation 2 (Yaşlılar):** Gen 1'den sağ kurtulanlar buradadır. GC burayı çok nadir tarar.

**Mantık (The Generational Hypothesis):** "Çoğu nesne oluşturulduktan hemen sonra ölür." Bu yüzden GC, sürekli tüm belleği taramak yerine, sadece "Genç" nesilleri sık sık kontrol eder. Döngüsel referanslar bu taramalar sırasında tespit edilip temizlenir.

**Kontrol Sende:**

```python
import gc
# GC'yi manuel tetiklemek (Genellikle gerekmez ama sunucu optimizasyonunda kullanılır)
gc.collect()

# Referans sayısını görmek (sys.getrefcount kendisi de +1 ekler)
import sys
x = []
print(sys.getrefcount(x)) 

```

---

### Özet Tablo

| Özellik | Açıklama |
| --- | --- |
| **Stack** | Fonksiyon çağrıları ve yerel değişken referanslarını tutar. Hızlıdır, otomatiktir. |
| **Heap** | Nesnelerin (int, str, list vb.) asıl verisinin tutulduğu yerdir. |
| **Immutable** | Değiştirilemez (int, str, tuple). Değişiklik yeni nesne yaratır. |
| **Mutable** | Değiştirilebilir (list, dict). Değişiklik aynı adreste yapılır. |
| **GC** | Temel olarak Reference Counting kullanır; döngüler için Generational GC devreye girer. |

---
