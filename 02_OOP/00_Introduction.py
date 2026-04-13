
#! Nesne Tabanlı Programlamaya Giriş (Object-Oriented Programming)(OOP)

# **Object Oriented Programming (OOP)** yani **Nesne Tabanlı Programlama** nedir?
# Nesne tabanlı programlama, bize kendi nesnelerimizi yaratma imkanı tanır.

#* Peki, nesne nedir?
# Şimdiye kadar yazdığımız kodlarda Python'da hali hazırda bulunan (built-in) nesnelerden yararlandık: int, str, dict, list.. vb.
# Bunların her birisi nesnedir, şimdi ise artık kendi nesnemizi yaratacağız.
# Nesne, özellikleri olan herhangi bir şey olabilir: bilgisayar, araba, öğretmen, öğrenci vb..

#* Neden OOP önemli?
# Projeler büyüdükçe yönetilemez boyutlara gelebiliyor, bakım ve onarım süreleri uzuyor. 
# Özellikle karmaşık sistemlerde, sadece temel programlama bilgisiyle elimiz kolumuz bağlı kalıyor. 
# Python içinde hazır olarak yer almayan fatura, rapor, mizan, öğretmen veya sanal sınıf gibi "nesnelere" ihtiyaç duyuyoruz. 

# OOP, bu artan ihtiyaçlar ve karmaşıklık doğrultusunda ortaya çıkmış bir yaklaşımdır. 
# Bize sağladığı en temel yenilik, kendi özel nesnelerimizi ve yapılarımızı yaratabilmemizdir.

#? Kendi nesnemizi yaratmak
# Kendi nesnemizi yaratmak için sınıflara (class) ihtiyacımız var. Nesne yaratmadan önce bir sınıf tanımlaması yaparız. 
# Bu sınıflar, yaratacağımız objenin özelliklerini barındıran prototipler gibidir. 
# Üretimde nasıl önce bir prototip üretilip sonra seri üretime geçiliyorsa, 
# burada da önce sınıf yaratılır, sonra bu sınıf üzerinden nesneler üretilir.

#* Class (Sınıf): Kendi nesnelerimizi yaratmak için oluşturduğumuz taslak/şablon. Özellikleri (attributes) ve yetenekleri (methods) tanımlar.
# Bu sınıflar yaratacağımız obje ve objelerin (birden fazla dict yazabiliyoruz ya, öyle düşün) özelliklerini içerlerinde barındırır.
#* Instance (Örneklem): Sınıftan türetilen, RAM'de yer kaplayan somut **Object (Nesne)**.

#todo Sınıfları `class` anahtar sözcüğü ile tanımlıyoruz. Örneğin bir `Araba` sınıfı oluşturalım:

class Araba:
    brand = "Dodge"
    model = "TRX 1500"
    door_number = 4
    engine_size = 6.2
    tork = 500
    length = 3.1
    width = 1.2
    color = "Black"


#todo Sınıfı tanımladıktan sonra ondan bir **nesne üretmek**, yani **instance (örneklem)** çıkartmak gerekir. Bunu şu şekilde yapıyoruz:
a1 = Araba() # Burada `A1` artık bir objedir ve tipi `Araba`dır. 

# Eskiden listelerin üzerine geldiğimizde "list" yazdığı gibi, şimdi `A1`in üzerine geldiğinizde "Araba" yazar. Objenin özelliklerine erişmek veya onları değiştirmek için **nokta notasyonunu** kullanırız:

print(f'Brand: {a1.brand}\nModel: {a1.model}')  # Objenin özelliğine erişim
a1.tork = 1000                                  # Özelliği değiştirme

# Aslında bugüne kadar kullandığınız listelerdeki `.append()`, `.clear()` veya sözlüklerdeki `.update()` gibi metotlar da bu nokta notasyonuna dayanır. 
# Yani kullandığımız her şey aslında birer objedir.

#? Constructor ve `__init__` Metodu

# Bir sınıftan nesne türetilirken arka tarafta bir fonksiyon tetiklenir. Tüm yazılım dillerinde buna **constructor (yapıcı fonksiyon)** denir. Python'da bu fonksiyonun adı `__init__` olarak belirlenmiştir; bu isim "initialization" (başlatma) kelimesinden gelir.

#* **`__init__` Method:** Nesne yaratılırken (instantiation) arka planda otomatik tetiklenen fonksiyon (Constructor).
#* **Görevi 1:** Objeyi yaratıp RAM'e çıkarmak.
#* **Görevi 2:** Dışarıdan gelen argümanları (Örn: `name`, `id`) alıp objenin özelliklerine (attribute) atamak.

# Siz yazsanız da yazmasanız da bu fonksiyon her nesne yaratılışında çalışır ve sınıfı RAM'e çıkartır. Ancak bazı özellikleri nesne yaratılırken zorunlu tutmak istiyorsak, bu fonksiyonu **customize** ederiz (özelleştiririz).


# ### Student Sınıfı Örneği

# ```python
# class Student:
#     taken_courses = [] # Class Attribute

#     def __init__(self, full_name, student_id):
#         # Object Attributes
#         self.tamat = full_name
#         self.ogrenci_id = student_id
# ```

# `__init__` fonksiyonunun üç temel görevi vardır:
# 1. Sınıfı başlatmak (initialize etmek).
# 2. Nesnenin belirli özelliklerle (örneğin isim ve ID) yaratılmasını zorunlu tutmak.
# 3. Dışarıdan gelen bu değerleri nesneye ait özellikler olarak atamak.

# Buradaki `self` ifadesi, yaratılan objenin kendisini temsil eder. Sınıfın içine doğrudan yazdığımız özelliklere **Class Attribute**, `__init__` içinde `self` ile tanımladıklarımıza ise **Object Attribute** diyoruz. Class attribute'lar sınıf yaratıldığı anda mevcuttur; ancak object attribute'lar sadece nesne üretildiği anda (*run-time*) oluşur.

# ---

# ### Yazılım Prensipleri ve Gelecek Planları

# Önümüzdeki haftalarda bizi yoğun bir program bekliyor. Bol bol `init`, **inheritance** (kalıtım), **method overriding**, **encapsulation**, **polymorphism** (çok biçimlilik) ve en önemlisi **abstraction** (soyutlama) konularını işleyeceğiz. Soyutlama konusu, ileri seviye kod yazmanın kapısını aralar; tasarım desenleri ve yazılım prensiplerine giriş yapmamızı sağlar.

# Python camiasında iki görüş vardır: Bir grup, hızlı uygulama geliştirmek için OOP prensiplerine ve tasarım desenlerine pek uymadan fonksiyonel takılır. Diğer grup (benim de dahil olduğum) ise belirli prensiplere sadık kalarak yazmayı savunur. Prensipli yazılan kodlar daha sürdürülebilir (*maintainable*) olur ve ekipteki diğer yazılımcılar tarafından daha rahat anlaşılır.

# Kod yazmanın değerinin her geçen gün azaldığı, yapay zekanın küçük taskları hızlıca hallettiği günümüzde, **System Design** (sistem tasarımı) çok daha kritik bir hale geldi. Artık sadece kod yazmak değil; sistemi kurgulayabilmek, **ML Ops** süreçlerini yönetebilmek, modelleri monitör etmek ve hata anında doğru müdahaleyi yapabilmek sizi öne çıkaracaktır.

# Hafta sonu bu temel kavramlara çalışın, pazartesi günü üzerine koyarak devam edeceğiz. İyi hafta sonları!

#! PyCharm ve OOP  Temelleri
# Bu bölüm, PyCharm IDE'sinin **OOP** prensiplerini görselleştirmede sağladığı avantajları ve **Inheritance** (Kalıtım) mekanizmasının teknik detaylarını kapsar.

#? PyCharm Visual Indicators (Görsel İşaretçiler)
# PyCharm, kodun okunabilirliğini artırmak için **Base Class** (Ata Sınıf) ve **Child Class** (Alt Sınıf) arasındaki ilişkiyi sembollerle gösterir:

#* **Is overridden in [ChildClass]:** Ata sınıftaki bir metodun yanında, aşağı yönlü bir ok bulunur. Bu, metodun alt sınıfta yeniden yazıldığını gösterir.
#* **Overrides method in [BaseClass]:** Alt sınıftaki metodun yanında, yukarı yönlü (genellikle kırmızı/mavi) bir ok bulunur. 
# Bu, metodun atadan miras alındığını ve değiştirildiğini belirtir.

#? Method Overriding ve `__init__` Yönetimi

# Method Overriding, ata sınıftan gelen bir metodun alt sınıfta ihtiyaca göre yeniden tanımlanmasıdır.

#* **Override Zorunluluğu:** Teknik olarak zorunlu değildir. Alt sınıf, ata sınıfın metodunu aynen kullanabilir. Ancak özelleştirme gerekiyorsa override edilir.
#* **`super().__init__` Kullanımı:**
#* Eğer bir **Child Class** içinde `__init__` fonksiyonu tanımlanırsa, Python ata sınıfın `__init__` fonksiyonunu otomatik olarak **çağırmaz**.
#* **BaseEntity** (Ata) içindeki özelliklerin (attributes) de yüklenmesi için `super().__init__()` (veya `BaseClass.__init__`) çağrısı **zorunludur**.
#* *Uyarı:* IDE (Örn: PyCharm), ata sınıfın `__init__`'i çağrılmadığında "Call to init of super class is missed" uyarısı verir.

# **Önemli Not:** Bir sınıfta `__init__` fonksiyonu override edildiğinde, var olan fonksiyonu "genişletmiş" (extend) olursunuz. Ancak aynı scope içinde `__init__` iki kere tanımlanamaz; bu "Redeclared defined above" hatasına yol açar.


#todo ## Case Study: Phone Architecture (Extend vs. Replace)

# `BasePhone` (Ata Sınıf) üzerinden `iPhone` ve `Samsung` (Alt Sınıflar) türetilmesi örneği.

# 1. **Extend (Genişletme):** `iPhone` sınıfı, `BasePhone`'dan gelen özelliklere ek olarak `AirDrop` özelliğine sahiptir. Bu nedenle `__init__` override edilir ve `super()` çağrılır.
# 2. **Replace (Geçersiz Kılma):** `phone_ring_sound` (Zil sesi) metodu. Her telefonun sesi farklıdır. Ata sınıftaki genel ses **tamamen** iptal edilir ve yeni ses tanımlanır.
# 3. **Enhance (İyileştirme):** `show_info` fonksiyonu, yeni eklenen özellikleri de gösterecek şekilde güncellenir.


#todo ## Case Study: Fatura Sistemi (Inheritance & Polymorphism)

# Gerçek hayat senaryosu: Farklı fatura tiplerini (Su, Elektrik, Doğalgaz) yöneten bir sistem tasarımı.

# ### Class Structure (Sınıf Yapısı)

# * **BaseBill (Ata Sınıf):**
# * **Attributes:** `bill_name`, `value_added_tax` (KDV), `amount`.
# * **Methods:**
# * `calculate_bill`: `tax * amount` işlemini yapar.
# * `create_log`: Fatura bilgilerini `.txt` dosyasına yazar.




# * **WaterBill (Child Class):**
# * **Extra Attribute:** `mill` (Sayaç dönme miktarı).



# ### Critical Logic: Override Kararları

# Bu senaryoda hangi fonksiyonun override edileceği, iş mantığına (Business Logic) göre belirlenir.

# 1. **`calculate_bill` Metodu:**
# * **Durum:** **Override Edilmeli.**
# * **Sebep:** Standart hesaplama (Vergi * Tutar) su faturası için yeterli değildir. İşin içine `mill` (sayaç) çarpanı girmektedir.
# * **Yöntem:** Ata sınıfın hesaplaması kullanılabilir (`super().calculate_bill() * self.mill`) veya formül tamamen yeniden yazılabilir.


# 2. **`create_log` Metodu:**
# * **Durum:** **Override Edilmemeli.**
# * **Sebep:** Loglama işlemi (dosyaya yazma) su, elektrik veya doğalgaz fark etmeksizin aynıdır.
# * **Polymorphism Triği:** `create_log` içinde `self.calculate_bill()` çağrılır. Burada `self`, o anki objeyi (örneğin `WaterBill` objesini) temsil ettiği için, `BaseBill`'deki değil, `WaterBill` içinde override edilmiş hesaplama metodu çalışır.



# ### Architecture & Maintainability (Sürdürülebilirlik)

# * **Eski Yöntem (Hard Coding):** Her yeni kurum (Örn: BEDAŞ, İSKİ) için kodu kopyala-yapıştır yapmak.
# * **Doğru Mimari (OOP):** `BaseBill` yapısı kurulduktan sonra sisteme yeni bir fatura tipi (Örn: Elektrik) eklemek, sadece yeni bir sınıf oluşturup parametreleri girmekten ibarettir.
# * **Sonuç:** Geliştirme süresi (Development Time) ve Bakım maliyeti (Maintenance Cost) minimize edilir.

# ---

# ## Encapsulation (Kapsülleme / Bilgi Gizleme)

# Sınıfın hassas verilerinin dış dünyadan (diğer sınıflardan veya dosyalardan) doğrudan erişime kapatılmasıdır.

# * **Syntax:** Değişken adının başına iki alt çizgi (`__`) getirilir. (Örn: `__status`, `__ip_addresses`).
# * **Access Rule (Erişim Kuralı):**
# * `object.__attribute` şeklinde dışarıdan erişilemez.
# * Sınıf içindeki metotlar (`self.__attribute`) erişebilir.



# ### Setters & Getters (Erişim Yöntemleri)

# Private (gizli) değişkenleri yönetmek için aracı fonksiyonlar kullanılır.

# 1. **Setter (Değer Atama):** Dışarıdan gelen veriyi kontrol ederek (Validation) private değişkene atar.
# * *Örnek:* `Product` sınıfında `price` ve `stock` bilgisi dışarıdan alınır. Setter fonksiyonu, bu değerlerin **0'dan büyük** olup olmadığını kontrol eder. Büyükse atama yapar, değilse işlemi reddeder.


# 2. **Getter (Değer Okuma):** Private değişkenin değerini güvenli bir şekilde dışarıya döner.

# ---

# ## Enum & Constants (Sabitler)

# * **Tanım:** Değişmesi beklenmeyen sabit değerlerin tutulduğu yapıdır. `Enum` sınıfından kalıtım alınarak oluşturulur.
# * **Best Practice:**
# * Sık değişen veriler (Örn: Kullanıcı Rolleri, Dinamik Statüler) için **KULLANILMAMALIDIR**.
# * Bir veriyi değiştirmek için kodun tekrar **Deploy** (Canlıya alınması) edilmesini gerektirir.


# * **Deployment Riski:** Canlıya alma işlemleri (Deployment) genellikle mesai dışı saatlerde (Cuma akşamı, hafta sonu) yapılır ve risklidir. Kod değişikliği gerektiren yapılar bu riski artırır.

# ---

# ## Future Roadmap: Data Science & AI

# Eğitimin bundan sonraki aşamalarında kod yazma yoğunluğu azalacak, analitik düşünme artacaktır.

# ### 1. Pandas (Veri Analizi)

# * SQL benzeri bir yapıdır ancak daha yeteneklidir.
# * **Fonksiyonlar:** Eksik veri saptama (Missing Data), İstatistiksel analiz, Veri Çarpıklığı (Skewness), Normalizasyon/Scaling.

# ### 2. Machine Learning (Scikit-Learn)

# * **Regresyon Modelleri:** Tahminleme.
# * **Evaluation Metrics (Değerlendirme):** R2 Score, Mean Squared Error (MSE).
# * **Algoritmalar:** KNN, Decision Tree, Logistic Regression.

# ### 3. Deep Learning (PyTorch)

# * Google'ın TensorFlow'u yerine, Hugging Face ve modern AI projelerinde yaygın olduğu için **PyTorch** kullanılacaktır.
# * **Konular:** Transformers, RAG (Retrieval-Augmented Generation), Fine-Tuning.

# ---

# ## Kariyer ve Başvuru Tavsiyeleri

# ### "Blacklist" Riski

# * Eğitim biter bitmez, hazır olmadan iş ilanlarına başvurmak stratejik bir hatadır.
# * İK (İnsan Kaynakları), yetersiz görülen bir adayı veritabanında işaretleyebilir (üstünü çizebilir). Gelişim gösterseniz bile aynı firmaya tekrar başvurmanız zorlaşır.

# ### Hazırlık Süreci (Checklist)

# Başvurudan önce tamamlanması gerekenler:

# 1. **GitHub Portföyü:** Kurstaki projelere benzer, özgün projeler eklenmeli.
# 2. **MLOps & Docker:** Modellerin deploy edilmesi süreçleri öğrenilmeli.
# 3. **Database:** En az birer tane SQL ve NoSQL projesi eklenmeli.

# > **Eğitmen Desteği:** Kod debug etme (hata ayıklama) talepleri karşılanmaz (ChatGPT bu konuda daha iyidir). Ancak proje vizyonu, mimari kararlar ve "nasıl daha iyi olur?" soruları için danışmanlık verilir.























# ## OOP, Method Overriding ve Encapsulation (PyCharm Rehberliğinde)

# Bu ders notu, **PyCharm IDE**'sinin sağladığı görsel rehberlik araçlarını kullanarak **Object-Oriented Programming (OOP)** prensiplerini, özellikle **Method Overriding**, **Inheritance** ve **Encapsulation** kavramlarını somut örneklerle ele almaktadır.

# ---

# ## 1. Method Overriding ve PyCharm Desteği

# **Method Overriding**, bir alt sınıfın (**Child Class**), miras aldığı üst sınıftaki (**Parent/Base Class**) bir fonksiyonu kendi ihtiyaçlarına göre yeniden tanımlamasıdır.

# * **PyCharm Symbols:** PyCharm, overriding durumunu anlamamız için editörün yan tarafında semboller gösterir:
# * **Mavi Ok (Aşağı Bakıyor):** "Is overridden in..." - Bu metodun alt sınıflar tarafından geçersiz kılındığını (override edildiğini) gösterir.
# * **Kırmızı Ok (Yukarı Bakıyor):** "Overrides method in..." - Bu metodun bir ata sınıftan alındığını ve burada yeniden yazıldığını gösterir.


# * **Super() Call:** Bir metot override edildiğinde, ata sınıftaki temel işlevleri kaybetmemek için `super().__init__(...)` veya `super().method_name()` kullanımı tercih edilir.

# > **Önemli Not:** PyCharm, `__init__` fonksiyonu override edildiğinde eğer `super()` çağrısı yapılmazsa *"Call to init of super class is missed"* uyarısı vererek geliştiriciyi uyarır.

# ---

# ## 2. Inheritance ve Feature Enhancement (Özellik Genişletilmesi)

# Kalıtım, sınıfların ortak özelliklerini bir **Base Class** altında toplayarak kod tekrarını önler.

# * **Enhance (Genişletme):** Alt sınıf, ata sınıfın metodunu çağırır (`super()`) ve üzerine kendi spesifik özelliklerini ekler.
# * **Total Override (Tamamen Geçersiz Kılma):** Ata sınıftan gelen yetenek tamamen iptal edilir ve sınıf kendine has yeni bir yetenek kazanır.

# ### Case Study: Phone Classes

# * **BasePhone:** `__init__`, `show_info`, `phone_ring_sound` metodlarına sahiptir.
# * **iPhone (Child):** `Airdrop` özelliği eklendiği için hem `__init__` hem de `show_info` metotları **enhance** edilmiştir. `phone_ring_sound` ise her telefonda farklı olduğu için **override** edilerek değiştirilmiştir.
# * **Samsung (Child):** iPhone ile benzer şekilde kendine has özellikleri için aynı metotları override eder.

# ---

# ## 3. Fatura Hesaplama Sistemi (Uygulamalı Örnek)

# Bu senaryoda, farklı fatura türlerinin (Su, Elektrik, Doğalgaz) ortak bir yapıdan türetilmesi ve hesaplama mantığındaki farklılıklar işlenmiştir.

# ### BaseBill (Ata Sınıf)

# * **Attributes:** `BillName`, `ValueAtTask`, `Amount`
# * **Calculate_bill():** Temel çarpma işlemi yapar: .
# * **Create_log():** Fatura bilgilerini bir `.txt` dosyasına kaydeder.

# ### WaterBill (Alt Sınıf)

# * **Special Attribute:** `mil` (Sayaç dönme miktarı).
# * **Calculation Logic:** Su faturasında hesaplama farklı olduğu için `calculate_bill` metodu override edilmiştir.
# * *Yöntem:* `super().calculate_bill() * self.mil` (Atadaki sonucu al ve mil ile çarp).


# * **Logging:** `create_log` metodu override **edilmemiştir.** Çünkü `self.calculate_bill()` çağrısı yapıldığında Python, objenin türüne göre (WaterBill ise onun içindeki) doğru fonksiyonu otomatik bulur.

# ---

# ## 4. Encapsulation (Kapsülleme)

# **Encapsulation**, bir sınıfın içerisindeki bazı özelliklerin veya metotların dış dünyadan (instance üzerinden doğrudan erişimden) saklanmasıdır.

# * **Private Members:** Python'da bir değişkenin başına çift alt çizgi (`__`) eklenerek (Örn: `__amount`) o veri dış erişime kapatılır.
# * **Neden Kullanılır?**
# * Verinin doğrudan ve kontrolsüz değiştirilmesini engellemek.
# * Hatalı değer atamalarının önüne geçmek (Örn: Fiyatın negatif girilmesi).
# * Sadece sınıf içinde çalışması gereken log veya IP gibi teknik bilgileri gizlemek.



# ---

# ## 5. Getter ve Setter Mantığı

# Kapsüllenmiş (Private) alanlara güvenli bir şekilde erişmek ve değer atamak için kullanılan fonksiyonlardır.

# * **Setter (Ayarla):** Veri atanırken kontrol mekanizması sağlar.
# * *Örnek:* Bir ürünün stoğu (`stock`) set edilirken `if stock < 0:` kontrolü yapılarak hatalı giriş engellenir.


# * **Getter (Al):** Gizlenmiş veriyi dışarıya güvenli bir şekilde sunar.

# ---

# ## 6. Enum Yapısı

# **Enum**, değişmeyen sabit değerleri (matematiksel sabitler, durum kodları vb.) tanımlamak için kullanılır.

# * **Önemli Uyarı:** Sık değişen yapılar (Örn: Türkiye'deki kullanıcı rolleri, vergi oranları) Enum içinde tutulmamalıdır. Çünkü her değişiklikte sistemin yeniden **deploy** edilmesi gerekir. Bu tür dinamik veriler **Database (Veri Tabanı)** üzerinde tutulmalıdır.

# ---

# **Bir sonraki adım:** Bu mantığı pekiştirmek adına; kendi belirlediğiniz bir senaryo (Araba, Sporcu, Kütüphane vb.) üzerinden, içinde en az iki tane private (kapsüllenmiş) alan barındıran ve bu alanlara kural ile değer atayan bir sınıf yapısı oluşturmamı ister misiniz?