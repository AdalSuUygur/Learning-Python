
# Data Management

## Data Management Lifecycle (Veri Yönetim Döngüsü)

Veri yönetimi, ham verinin alınıp işlenerek sunulabilir hale getirilmesi sürecidir. Bu süreç, bir restoran analojisi ile en iyi şekilde anlaşılır.

### The Cycle (Döngü Adımları)

1. **Collection (Toplama):** Verinin kaynaktan istenmesi.\
*Teknik:* HTTP Requests / API Calls.\
*Analoji:* Müşterinin garsonu çağırıp sipariş vermesi.

2. **Processing (İşleme):** Ham verinin temizlenmesi ve analizi.\
*Teknik:* Python (Pandas), Data Cleaning.\
*Analoji:* Şefin malzemeleri doğrayıp yemeği pişirmesi.

3. **Storage (Saklama):** İşlenen verinin kalıcı hale getirilmesi.\
*Teknik:* Database (SQL/NoSQL) veya Dosya Sistemleri.\
*Analoji:* Kalan yemeğin paketlenip buzdolabına konması.

4. **Presentation (Sunma):** Verinin son kullanıcıya veya başka sistemlere açılması.\
*Teknik:* API Development (Endpoint açma).\
*Analoji:* Yemeğin servis edilmesi.

**Özetle:**

* **HTTP:** Yol ve trafik kuralları.
* **API:** O yoldan gidip sana veriyi getiren kurye/tercüman.
* **Data Management:** O verinin üretiminden tüketimine kadar olan tüm yaşam döngüsü.

## JSON (JavaScript Object Notation)

> **Açılımı:** **J**ava**S**cript **O**bject **N**otation\
> **Türkçesi:** JavaScript Nesne Gösterimi\
> **Definition:** Sistemler arası veri taşıma için kullanılan, insan tarafından okunabilir (human-readable) ve hafif bir veri formatıdır. Farklı programlama dilleri (Python, Java, C#) arasındaki **"Esperanto"** (Ortak Dil) olarak görev yapar.

### Serialization Process (Serileştirme Süreci)

Verinin transfer edilebilir formata dönüştürülmesi işlemidir.

1. **Input:** Python Dictionary veya Object.
-> Veriyi al\
2. **Serialize:** JSON formatına (String) çevirme (Paketleme).
-> Veriyi JSON'a çevir (paketle)\
3. **Transfer:** Ağ üzerinden gönderme.
-> Veriyi gönder\
4. **Deserialize:** Karşı tarafın paketi açıp kendi diline (örn. Java Object) çevirmesi.
-> Paketi aç\
-> Paketi kendi diline çevir.

**Key Advantages (Avantajlar):**

* **Lightweight:** Düşük bant genişliği kullanır, hızlıdır.
* **Language Independent:** Her modern dil tarafından native olarak desteklenir.
* **Structure:** Sadece `List []` ve `Dictionary {}` yapılarından oluşur.

## HTTP Protocol (HyperText Transfer Protocol)

**Concept:** İnternet üzerindeki Client (İstemci) ve Server (Sunucu) arasındaki iletişim kuralları bütünüdür. Bir **Request** (İstek) ve **Response** (Cevap) döngüsüne dayanır.

**Özet:** İnternetteki bilgisayarların birbirleriyle konuşurken kullandığı nezaket kuralları ve dilidir.

### HTTP Methods & CRUD Operations

Veritabanı işlemleri (CRUD) ile HTTP metodlarının teknik eşleşmesi ve özellikleri:

| HTTP Method | CRUD Operation | Description (Açıklama) | Idempotency (Tekrarlanabilirlik) |
| --- | --- | --- | --- |
| **GET** | **Read** (Oku) | Kaynaktan veri çeker. Sunucuda değişiklik yapmaz. | **Idempotent:** Güvenlidir. 100 kere de atılsa sunucu durumu değişmez. |
| **POST** | **Create** (Oluştur) | Sunucuya yeni veri ekler. Veri `Payload` (Gövde) içinde gider. | **NOT Idempotent:** Aynı istek 2 kere atılırsa 2 mükerrer kayıt oluşur. |
| **PUT** | **Update** (Güncelle) | Mevcut bir kaydı **tamamen** değiştirir/üzerine yazar. | **Idempotent:** Aynı güncelleme defalarca yapılsa da sonuç aynı kalır. |
| **DELETE** | **Delete** (Sil) | Belirtilen kaynağı yok eder. | **Idempotent:** Silinen dosyayı tekrar silmeye çalışmak sonucu (yokluk) değiştirmez. |

> **Critical Concept: Idempotency**
> Bir işlemin birden fazla kez uygulanması, işlemin sonucunu değiştirmiyorsa o işlem **Idempotent**'tir. (Örn: Asansör çağırma düğmesine 1 kere basmakla 50 kere basmak aynıdır).

## API (Application Programming Interface) (Uygulama Programlama Arayüzü)

> **API (Application Programming Interface):** İki yazılımın birbiriyle konuşmasını sağlayan **soyutlama katmanı (abstraction layer)** ve **sözleşmedir (contract)**.

Bir restorana gittiğini hayal et.

* **Sen (Client/İstemci):** Masada oturuyorsun, karnın aç (Veri istiyorsun).
* **Mutfak (Server/Sunucu):** Yemeklerin yapıldığı, malzemelerin durduğu yer (Veritabanı).

**Sorun:** Sen doğrudan mutfağa girip aşçıya "Bana az pişmiş bonfile ver" diyemezsin. Orası tehlikeli, karışık ve yasaktır. Senin mutfakla konuşmanı sağlayacak bir "aracıya" ihtiyacın var.

**Çözüm: Garson (API)**:

1. **Menü (Dokümantasyon):** Garson sana bir menü getirir. Menüde ne varsa onu isteyebilirsin. (API'nin sana izin verdiği işlemler).
2. **Sipariş (Request):** Sen garsona "Köfte istiyorum" dersin.
3. **İletim:** Garson mutfağa gider, siparişi şefe iletir.
4. **Servis (Response):** Garson mutfaktan yemeği alır ve sana getirir.

> **Özet:** **API (Garson)**, senin (Uygulama/Kullanıcı) ile Mutfak (Sunucu/Veritabanı) arasındaki iletişim köprüsüdür. Sen mutfağın nasıl çalıştığını bilmezsin, sadece garsona söylersin, o getirir.

### Monolith Mimari (Eski Usul - Mahalle Bakkalı)

* **Yapısı:** Tüm modüller (Search, Payment, User Auth) tek bir kod tabanı ve sunucudadır.
* **Risk (Single Point of Failure):** "Search" modülündeki bir hata tüm uygulamayı (Payment dahil) çökertir.
* **Deploy:** Küçük bir değişiklik için tüm devasa yapının yeniden başlatılması gerekir.

> **Yazılımda:** Üye girişi kısmı bozulursa, ödeme sistemi de çalışmaz. Çünkü hepsi tek bir kod yumağının içindedir.

### Microservices Mimari (Modern Usul - AVM)

* **Yapısı:** Kasap ayrı bir dükkan, Manav ayrı bir dükkan, Eczane ayrı bir dükkan. Her birinin kendi kapısı, kendi elektriği, kendi çalışanı var.
* **Avantajı (İzolasyon):** Manav dükkanında yangın çıksa ne olur? Sadece manav kapanır. Sen yan taraftaki Eczane'den ilacını almaya devam edebilirsin. AVM hayatına devam eder.
* **Büyüme Kolaylığı:** Eczane çok kalabalıksa, sadece Eczane'yi büyütürsün veya yanına bir Eczane daha açarsın. Manavı ellemezsin.

> **Yazılımda:** "Sepet" servisi bozulsa bile, kullanıcılar ürünleri "Arama" yapmaya ve gezmeye devam edebilir. Site tamamen çökmez.

### API ve Microservices İlişkisi

Şimdi bu iki kavramı birleştirelim.

Microservices mimarisinde (AVM örneğinde), dükkanlar birbirleriyle nasıl konuşur?

* Manavın bozuk parası bitti, Eczane'den bozukluk isteyecek.
* Duvarı delip bağırmazlar.
* Manavın çırağı (API), Eczane'ye gider ve "Bozuk para var mı?" (Request) der.
* Eczane verir (Response).

**Sonuç:**
**Microservices**, sistemin küçük parçalara bölünmüş halidir (Manav, Kasap, Eczane).
**API**, bu parçaların birbiriyle ve seninle konuşmasını sağlayan dildir/kablodur.

## Tools & Frameworks

### Python `requests` Module

* **Function:** Python ile HTTP istekleri (GET, POST vs.) atmayı sağlayan kütüphanedir.
* **Usage:** Manuel olarak HTTP paketi hazırlamak yerine `requests.get(url)` komutuyla tarayıcı simülasyonu yapar.

### Python Web Frameworks (Comparison)

API geliştirmek için kullanılan iskelet yapılardır.

1. **Django:** "Villayı eşyalı kiralamak."\
Her şey dahil gelir (Admin panel, Auth, DB yönetimi). Ağır ve kapsamlıdır.

2. **Flask:** "Boş bir oda kiralamak."\
Sadece temel yapı vardır. İçini (Auth, DB) ihtiyacına göre sen döşersin.

3. **FastAPI:** "Modern prefabrik ev."\
Güncel standart (Asynchronous), çok hızlı ve otomatik dokümantasyon sağlar. Sektör standardı haline gelmektedir.
