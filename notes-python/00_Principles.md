
# Principles

## Yazılım Mimarisi ve Prensipleri (Software Architecture Principles)

### Single Responsibility Principle (SRP)

**Tanım:** Bir yazılım bileşeninin (fonksiyon, sınıf veya modül) yalnızca **tek bir** değişme sebebi olmalıdır.

**Analogy (Benzetme):** Bir restoran çalışanı hem şeflik yapıp, hem bulaşık yıkayıp hem de muhasebeye bakmamalıdır.

**Neden Önemli?** Eğer bir oyuncak robot hem şarkı söylüyor, hem yürüyor, hem de çay demliyorsa; şarkı söyleme mekanizması bozulduğunda tamir ederken yanlışlıkla çay demleme özelliğini de bozabilirsin.

**Temel Amaç:** Hata yönetimi ve bakım kolaylığı. Bir parça bozulduğunda tüm sistemin çökmesini engellemek.

### Separation of Concerns (SoC)

**Tanım:** Bir bilgisayar programının, her biri ayrı bir endişeyi veya işlevi ele alan farklı bölümlere ayrılmasıdır. SRP'nin daha geniş, sistemsel halidir.

Bir bilgisayar oyununu düşün:

1. **Rendering (Görüntü):** Karakterin nasıl göründüğü.
2. **Physics/Logic (Mantık):** Zıplama yüksekliği, çarpışma etkisi.
3. **Storage (Kayıt):** Oyunun kaydedilmesi.

* *Sonuç:* Karakterin kıyafeti değiştiğinde (Görüntü), zıplama fiziği (Mantık) bozulmaz.

## Kodlama Mentalitesi ve Disiplini

### Clean Code (Temiz Kod)

* **Tanım:** Kodun sadece bilgisayarlar tarafından değil, insanlar tarafından da kolayca okunabilir, anlaşılabilir ve bakımı yapılabilir olmasıdır.

* **Özellikleri:** Anlamlı değişken isimlendirmeleri, kısa fonksiyonlar, gereksiz yorum satırlarından arındırılmış yapı.

### Syntax & Built-in Functions

Bilgisayar programı yazmak, aslında çok büyük ve karmaşık bir LEGO kalesi yapmak gibidir. Eğer her şeyi birbirine yapıştırırsan, bir parçayı değiştirmek istediğinde tüm kale yıkılır. İşte bu kavramlar kaledeki parçaların nasıl birleşmesi gerektiğini anlatır.

* **Kural:** Nesne Tabanlı Programlamada (OOP), bir nesnenin sonuna nokta (`.`) konulduğunda, o nesnenin türüne (class) ait yerleşik fonksiyonlar (metotlar) çağrılır.

### DRY (Don't Repeat Yourself)

* **DRY (Don't Repeat Yourself):** "Kendini Tekrar Etme."\
Bir kuralı veya veriyi tek bir yerde tanımla, her yerden oraya referans ver.
**Özet:** Bir şeyi bir kere yap, her yerde kullan.

* **DRY'a uymayan yöntem:** Her kapının içine tek tek "Gıcırrr sesi çıkar" kodunu yazarsın. 10 kapı için 10 kere aynı şeyi yazmış olursun.
* **Sorun ne?** Yarın bir gün "Gıcırrr" sesini "Tak" sesiyle değiştirmek istersen, 10 kapıyı da tek tek bulup kodu değiştirmen gerekir. Birini unutursan oyunun bozulur.
* **DRY (Doğru) Yöntem:** Bir tane "KapıSesi" kutusu yaparsın. Tüm kapılara "Ses çıkaracağın zaman şu kutuya bak" dersin. Sesi değiştirmek istersen sadece o tek kutuyu değiştirirsin, tüm kapılar bir anda düzelir.

**Motto:** "Kopyala-yapıştır yapıyorsan, muhtemelen bir hata yapıyorsun!"

### WET (Write Everything Twice)

**Özet:** DRY prensibinin tam tersidir ve genellikle kaçınmamız gereken bir durumdur.

WET'in açılımı aslında biraz iğneleyicidir: **"Write Everything Twice"** (Her şeyi iki kere yaz) veya **"We Enjoy Typing"** (Yazmaktan keyif alıyoruz/vaktimiz bol) anlamlarına gelir.

* **WET durumunda:** Kodun içinde aynı hesaplamayı veya aynı cümleyi defalarca görürsün. Kodun "ıslak" (WET) ve dağınıktır.
* **Neden kötü?** Kodun çok uzar, okuması zorlaşır ve en önemlisi **hata yapma ihtimalin çok artar.** Bir yeri düzeltirsin ama kopyaladığın diğer 5 yer hatalı kalmaya devam eder.

## Web İletişimi ve Veri Transferi (Web Communication)

### HTTP (Hypertext Transfer Protocol)

**Tanım:** İnternet üzerindeki veri alışverişinin kurallarını belirleyen protokoldür (İnternetin Postacısı).
Sen bir internet sitesinin adresini yazıp "Enter"a bastığında, aslında görünmez bir postacıya bir zarf veriyorsun.

* **Zarfın üstünde:** "Bana şu videoyu getir" yazar (Buna **GET** isteği denir).
* **Postacı (HTTP):** Gider o videonun olduğu bilgisayarı bulur.
* **Cevap:** O bilgisayar da bir zarf gönderir. İçinde ya video vardır ya da "Üzgünüm, video silinmiş" notu.

HTTP, bu postacının hangi yoldan gideceğini ve kapıyı nasıl çalacağını belirleyen kurallar bütünüdür.

### 2. API (Application Programming Interface)

**Tanım:** İki farklı yazılımın birbiriyle konuşmasını sağlayan arayüzdür.

* **Analogy (Benzetme):** Restorandaki **Garson**. Müşteri (Senin uygulaman) mutfağa (Veri sunucusu) girmez; siparişi garsona (API) verir, garson yemeği getirir.

Bir hava durumu uygulaman olduğunu hayal et. Uygulamanın dünyadaki tüm bulutları ve rüzgarları takip etmesi imkansız, değil mi? O zaman bu bilgiyi profesyonel bir yerden (Meteoroloji Genel Müdürlüğü gibi) alması lazım.

İşte **API**, o profesyonel merkezin dışarıya açtığı küçük bir "sipariş penceresi"dir.

1. Senin uygulaman o pencereye gider.
2. "İstanbul'da hava nasıl?" diye bir not bırakır.
3. API, içerideki karmaşık sistemlere hiç bulaşmadan sana sonucu verir: "15 derece, Güneşli."

### 3. Python `requests` Module

Python öğrenirken kod yazarak internetten bir veri çekmek istersen, kendi başına bir postacı (HTTP) yaratamazsın. Çok zordur. Ama birisi senin için **`requests`** adında bir alet çantası hazırlamış.

**Tanım:** Python'da HTTP isteklerini (GET, POST vb.) kolayca yapmak için kullanılan kütüphane/araçtır.

* **İşlevi:** Postacı görevini (HTTP) kod içinde otomatikleştirir.
* **Kullanım:** `requests.get("url")` komutuyla siteye gidip veriyi alıp koda getirir.

## Modern Kodlama Yaklaşımı: Vibe Coding

Eskiden kod yazmak; her virgülün, her parantezin yerini ezbere bilmek ve saatlerce klavyede "tık tık tık" yazı yazmak demekti. **Vibe Coding** ise; kodun teknik detaylarıyla (parantezlerle, noktalı virgüllerle) uğraşmak yerine, **yapay zekaya (AI) ne yapmak istediğini anlatarak** uygulama geliştirme tarzıdır.

**Tanım:** Kodun teknik detaylarından (syntax, noktalı virgül) ziyade, **iş mantığına ve vizyona** odaklanarak, Yapay Zeka (AI) araçlarıyla hızlı uygulama geliştirme yöntemidir.

* **Araçlar:** Cursor, Replit Agent, Claude.
* **Farkı:**
* *Eski:* "For döngüsü nasıl kurulur?" diye düşünmek.
* *Vibe Coding:* "Bana mor renkli, yemek tarifi veren bir uygulama yap" diye prompt girmek.
* **Gereklilik:** Temel kavramları (SRP, API, DRY) bilmek hala şarttır; çünkü AI'yı (orkestrayı) yöneten şef sensin.

## Algoritmik Karmaşıklık ve Performans (Big O Notation)

**Tanım:** Bir algoritmanın verimliliğini; girdi boyutu () arttıkça, işlem süresinin veya hafıza kullanımının nasıl arttığını ölçen birimdir. **Saniye değil, adım sayısı ölçer.**

Düşün ki bir kütüphanedesin ve bir kitap arıyorsun.

* **O(1) - Sabit Zaman:** Kitabın tam olarak hangi rafta olduğunu biliyorsun. Gidip şak diye alıyorsun. Kütüphanede 10 kitap da olsa, 1 milyon kitap da olsa senin harcadığın süre aynıdır. Bu en hızlısıdır.
* **O(n) - Doğrusal Zaman:** Kitabın yerini bilmiyorsun. İlk kitaptan başlayıp tek tek bakıyorsun. 10 kitap varsa 10 adım, 1 milyon kitap varsa 1 milyon adım atarsın. Kitap sayısı arttıkça işin de aynı oranda uzar.
* **O(n²) - Karesel Zaman:** En yavaşıdır. Şöyle düşün: Her kitabın içine bakıyorsun ve o kitaptaki bir kelimeyi kütüphanedeki diğer tüm kitaplarla karşılaştırıyorsun. Kütüphane biraz büyürse bu iş asla bitmez!

### Big O Complexity Classes (Hızlıdan Yavaşa)

1. Constant Time (Sabit Zaman): Veri boyutu ne olursa olsun süre değişmez.\
*Örnek:* Bir listenin ilk elemanına erişmek.

2. Logarithmic Time (Logaritmik Zaman): Veri arttıkça süre çok az artar. Her adımda seçenekler yarıya iner.\
*Örnek:* Binary Search (İkili Arama), Kütüphanedeki kitabı raf aralıklarını daraltarak bulmak.

3. Linear Time (Doğrusal Zaman): Veri arttıkça süre aynı oranda artar.\
*Örnek:* Linear Search (Tüm listeyi tek tek gezmek).

4. Linearithmic Time: En verimli sıralama algoritmaları.\
*Örnek:* Merge Sort, Quick Sort.

5. Quadratic Time (Karesel Zaman): Veri boyutu karesi kadar işlem. Genellikle **iç içe döngüler** buna sebep olur. Performans katilidir.\
*Örnek:* Bubble Sort (İç içe her sayıyı diğeriyle kıyaslamak).

6. Exponential Time (Üstel Zaman): Her adımda iş yükü ikiye katlanır.\
*Örnek:* Naive Recursive Fibonacci.

7. Factorial Time (Faktöriyel Zaman): Tüm permütasyonları denemek.\
*Örnek:* Travelling Salesman Problem (Gezgin Satıcı Problemi) - Brute Force çözümü.

### Optimizasyon İpuçları

**İç İçe Döngülerden Kaçın (O(n²) tuzağı):** Yeni başlayanların en çok yaptığı hata, bir listenin içinde gezerken başka bir liste açıp içinde tekrar gezmektir.

* **Kötü Kod:** Bir listedeki sayıların birbirinin aynısı olup olmadığını bulmak için her sayıyı diğer her sayıyla tek tek karşılaştırmak. (Her eleman için tüm listeyi tekrar dönmek).
* **İyi Kod:** Sayıları önce bir "sözlük" (Dictionary/Set) içine atıp, orada var mı diye bakmak. (Böylece listeyi sadece bir kere gezmiş olursun).

**Gereksiz Veri Yapılarını Temizle:** Bazen bir bilgiyi bulmak için koca bir listeyi taramak yerine, o bilgiyi bir "anahtar" ile çağırmak çok daha hızlıdır. Listede arama yapmak yerine **Hash Map / Dictionary ()** kullan.

**"Hemen Bitir" Mantığı:** Eğer aradığın şeyi listenin başında bulduysan, listenin sonuna kadar bakmaya devam etme! `break` kullanarak gereksiz döngüleri sonlandır.

## İleri Algoritma Teknikleri (Advanced Algorithms)

Bu teknikler "Hız", "Hafıza Tasarrufu" ve "Zeka"yı birleştirir.

### Divide and Conquer (Parçala ve Fethet)

* **Mantık:** Büyük bir sorunu, çözebileceğin kadar küçük parçalara ayır, sonra birleştir.

* **Örnek:** 1000 parçalık devasa bir puzzle yapman gerekiyor.
* **Basit Yol:** Her parçayı tek tek dene. (Çok uzun sürer!)
* **İleri Yol:** Önce kenarları ayır, sonra renklerine göre grupla. Her grubu kendi içinde bitir ve sonra grupları birleştir.
* **Algoritma Dünyasında:** "Merge Sort" (Sıralama Algoritması) buna en iyi örnektir.

### Dynamic Programming (Dinamik Programlama)

* **Mantık:** "Geçmişi unutma!" Bir şeyi bir kez hesapladıysan, onu bir kenara yaz ve ihtiyacın olduğunda oradan bak.\
**Örnek1 :** Fibonacci dizisinde önceki sayıları cache'lemek (Memoization).

**Örnek2 :**\ Bir matematik sorusu çözüyorsun: sonucu nedir? Saydın ve 25 buldun. Peki, yanına bir tane daha 5 eklersem ne olur?
**Basit Yol:** Baştan başlayıp tekrar 5, 10, 15... diye saymak.
**İleri Yol (Dinamik):** "Az önce 25 bulmuştum, sadece bir 5 daha eklerim ve 30 olur" demek.
**Neden Önemli?** Bilgisayarın aynı şeyi milyonlarca kez tekrar hesaplamasını engelleyerek inanılmaz hız kazandırır.

### Greedy Algorithms (Açgözlü Algoritmalar)

* **Tanım:** Bir problemin çözümünde, her adımda "yerel olarak" (o an için) en iyi seçimi yaparak "küresel" (genel toplamda) en iyi sonuca ulaşmayı uman yöntemdir.

**Çalışma Prensibi:**

1. Seçenekleri incele.
2. Şu an en kârlı olanı seç.
3. Seçtiğini listeye ekle.
4. Asla geriye dönme ve kararını değiştirme (**Backtracking yapmaz**).

**Avantajı:**\
Çok hızlıdır ve kodlaması basittir.

**Dezavantajı:**\
Her zaman en iyi sonucu vermez (Lokal optimum tuzağına düşebilir).

**Nerede Kullanılır?**\
Dijkstra Algoritması (Haritada en kısa yolu bulurken).\
Sıkıştırma Algoritmaları (Huffman Coding - Dosya boyutunu küçültürken).\
Minimum Spanning Tree (İnternet kablolarını en az maliyetle döşerken).

**Başarılı Örnek:**\
Greedy algoritmalar her zaman hata yapmaz. Özellikle Türk Lirası, Dolar veya Euro gibi para birimlerinde "en az sayıda banknotla para üstü verme" işini mükemmel yapar.

**Görev:** Müşteriye **67 TL** para üstü vereceksin. En az sayıda banknot kullanmalısın.
**Kasa:** 50 TL, 20 TL, 10 TL, 5 TL, 1 TL.

**Greedy Algoritmanın Adımları:**

1. **Bakış:** 67 TL'ye en yakın en büyük para ne? -> **50 TL**.\
(Aldım)\
*Kalan:* 17 TL.

2. **Bakış:** 17 TL'ye en yakın en büyük para ne? 20 TL büyük gelir. O zaman -> **10 TL**.\
(Aldım)\
*Kalan:* 7 TL.

3. **Bakış:** 7 TL için en büyük para ne? -> **5 TL**. \
(Aldım)\
*Kalan:* 2 TL.

4. **Bakış:** 2 TL için en büyük para ne? -> **1 TL**. \
(Aldım)\
*Kalan:* 1 TL.

5. **Son Adım:** Kalan 1 TL için -> **1 TL**. \
(Aldım)\
**Sonuç:** 50 + 10 + 5 + 1 + 1 = Toplam 5 banknot. Bu en verimli çözümdür. Greedy burada işe yaradı!

**Başarısız Örnek:**\
Şimdi kuralları değiştirelim ve **"Saçma Bir Para Birimi"** icat edelim.\
**Banknotlar:** 1 TL, 3 TL, 4 TL.\
**Hedef:** **6 TL** oluşturmak.

**Greedy Yaklaşımı:**

1. 6 TL'ye en yakın en büyük sayı ne? -> **4 TL**. (Aldı). *Kalan:* 2 TL.

2. 2 TL'ye en yakın en büyük sayı ne? (3 büyük gelir) -> **1 TL**. (Aldı). *Kalan:* 1 TL.

3. Kalan 1 TL için -> **1 TL**. (Aldı).

> **Greedy Sonucu:** 4 + 1 + 1 = **3 Banknot**.

**Mantıklı (Optimal) Yaklaşım:**

* Hiç 4 TL'ye bulaşma. İki tane 3 TL al.
* 3 + 3 = 6 TL.
* **Optimal Sonuç:** **2 Banknot**.

**Özet:** Greedy, gözünün önündeki büyük lokmaya (4 TL) atladığı için, daha basit olan çözümü (3+3) kaçırdı.

### Graph Algorithms (Graf Algoritmaları)

* **Mantık:** Düğümler (node) arasındaki ilişkileri ve yolları analiz etmek. Birbirine bağlı noktalar arasındaki en iyi yolu bulmak.

* **Örnek:** Instagram'daki arkadaşlık ağı veya Google Haritalar'daki yollar.
* **Problem:** Evden okula gitmek için binlerce sokak var. En kısa hangisi?
* **Çözüm:** "Dijkstra Algoritması" gibi ileri algoritmalar, tüm yolları taramak yerine matematiksel bir mantıkla en hızlı yolu saniyeler içinde bulur.

## Performans Ölçümü (Performance Measurement)

* **Decorators:** Python'da bir fonksiyonun çalışma süresini, CPU ve RAM kullanımını ölçmek için fonksiyonu "saran" yardımcı kod bloklarıdır.

* **Makine Öğrenmesi İlişkisi:** KMeans veya KNN gibi algoritmalar büyük veri setleriyle çalışır. Big O analizi yapılmamış, verimsiz bir kod bu algoritmaların günlerce sürmesine neden olabilir.
