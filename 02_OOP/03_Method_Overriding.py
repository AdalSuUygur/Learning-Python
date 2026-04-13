
#! ## Method Overriding
#* Definition: Ata sınıftan (Parent) miras alınan bir metodun, alt sınıfta (Child) ihtiyaca göre yeniden tanımlanarak davranışının değiştirilmesi veya geliştirilmesidir.
# Keyfi nedenlerle method override edilmez.

# Parentler organize edilirken alt sınıfların ortak özelliklerini barındırır.
# Amaçları kalıtım vermektir. Bu yüzden instanceları alınmaz.
class BaseEntity: #* İsimlendirmenin başında "Base" görünce parent olduğunu anla!
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    def show_info(self):
        print(
            f'Name: {self.name}\n'
            f'Description: {self.description}'
        )

#? 1. Enhance (Geliştirme/Genişletme)
#* Mevcut ata fonksiyonunun yeteneğini koruyup üzerine ekleme yapma işlemidir.
# * **Key Tool:** `super()` fonksiyonu.
# * **Usage:** `super().__init__(...)` ile önce atadaki kod çalıştırılır, ardından alt sınıfa özgü kodlar eklenir.

#region Case Study: E-Commerce (Product vs. Category)
#* **BaseEntity (Parent):** Tüm varlıkların ortak özellikleri olan `name` ve `description` tutulur.
#* **Category (Child):** Ekstra bir özelliğe ihtiyaç duymaz. Parent'taki `__init__` ve `show_info` yeterlidir. **Override edilmez.**

class Category(BaseEntity): # Alt sınıf
    pass

class Product(BaseEntity): # Alt sınıf
    # Ürünlerin price, stock gibi kendine has özellikleri olur.
    # Kendine has olduğu için alt sınıfa yazıyoruz.
    def __init__(self, name, description, price: float, stock: int):
        super().__init__(name, description)
        self.price = price
        self.stock = stock

#* Product yani ürün `price` ve `stock` gibi kendine has özelliklere sahiptir.
#* Parent'taki `__init__` yetersiz kalır.
#* Bu durumda `__init__` override edilir. `super()` ile isim ve açıklama alınır; fiyat ve stok manuel eklenir. 
#* `show_info` metodu da bu yeni bilgileri gösterecek şekilde güncellenir.

    def show_info(self):
        super().show_info()
        print(
            f'Price: {self.price}\n'
            f'Stock: {self.stock}'
        )

p1 = Product(name='Boxing Gloves', description='Boxing Gloves', price=10.999, stock=100)
p1.show_info()
#endregion

#? 2. Replace (Geçersiz Kılma/Ezme)
#* Ata sınıftan gelen metodun tamamen yok sayılıp, yerine yepyeni bir logic yazılmasıdır.

#region Case Study: Phones (BasePhone)
class BasePhone: #BasePhone (Parent)
    def __init__(self, phone_id: str, model: str, brand: str, price: float):
        self.phone_id = phone_id
        self.model = model
        self.brand = brand
        self.price = price
    
    def show_info(self):
        print(
            f'Id: {self.phone_id}\n'
            f'Model : {self.model}\n'
            f'Brand: {self.brand}\n'
            f'Price: {self.price}'
        )
    
    def phone_ring_sound(self) -> str: #Fonksiyonumuz
        return 'genel telefon sesi'

# class Iphone(BasePhone):
#     def __init__(self, airdrop: str, phone_id: str, model: str, brand: str, price: float):
#         super().__init__(phone_id, model, brand, price)
#         self.airdrop = airdrop
    
#     def show_info(self):
#         super().show_info()
#         print(f'Airdrop: {self.airdrop}')
    
#     def phone_ring_sound(self):
#         return 'Iphone telefon sesi'

# * **IPhone (Child):**
# * `__init__` override edilir (`super` ile) -> `Airdrop` özelliği eklenir.
# * `phone_ring_sound()` override edilir -> "iPhone telefon sesi" döndürür (Replace).

# * **Samsung (Child):**
# * `__init__` override edilir (`super` ile) -> `Operating System` özelliği eklenir.
# * `phone_ring_sound()` override edilir -> "Samsung telefon sesi" döndürür (Replace).



# class Samsung(BasePhone):
#     def __init__(self, phone_id, model, brand, price, os: str):
#         super().__init__(phone_id, model, brand, price)
#         self.os = os

#     def show_info(self):
#         super().show_info()
#         print(f'Operating System: {self.os}')
    
#     def phone_ring_sound(self):
#         return 'samsung telefon sesi'
    
# samsung_1 = Samsung(phone_id=1, model='Galaxy 20', brand='Samsung', price=120.000, os='Android')
# samsung_1.show_info()
# print(samsung_1.phone_ring_sound())

# iphone_1 = Iphone(phone_id=2, model='Pro 16 Max', brand='Iphone', price=200.000, airdrop='True')
# iphone_1.show_info()
# print(iphone_1.phone_ring_sound())

#endregion

# > **Polymorphism Bağlantısı:** `phone_ring_sound` metodu; Base, iPhone ve Samsung sınıflarında aynı isme sahip olmasına rağmen üç farklı çıktı üretir. Bu durum **Polymorphism** (Çok Biçimlilik) kavramının temelidir.

# ---

#todo ## Uygulama: Fatura Hesaplama (Bill System)

# Verilen ödev/pratik senaryosunun analizi:

# ### Class Structure

# 1. **BaseBill (Parent):**
# * **Attributes:** `bill_name`, `value_added_tax` (KDV).
# * **Methods:**
# * `calculate_bill(amount)`: Vergili tutarı hesaplar.
# * `create_log()`: Fatura detaylarını `.txt` dosyasına yazar.




# 2. **Child Classes:** `WaterBill`, `NaturalGas`, `Electricity`.

# ### Logic Analysis

# * **Override Edilmeyenler:** `create_log`. Çünkü su, gaz veya elektrik faturası fark etmeksizin loglama işlemi (isim ve tutar yazma) standarttır.
# * **Override Edilenler:** `__init__` ve `calculate_bill`.
# * Her faturanın birimi farklıdır (`mill`, `m3`, `kw`).
# * Bu birimler `__init__` içinde tanımlanmalı ve hesaplama (`calculate_bill`) bu birimlere göre özelleştirilmelidir.



# ---

# ## Kariyer ve ML Ops Tavsiyeleri

# Eğitmenin sektör deneyimlerine dayalı kritik tavsiyeler:

# ### Essential Skill Set (Olmazsa Olmazlar)

# Sadece kod yazmak veya algoritma bilmek yeterli değildir. İK filtrelerini geçmek ve mülakatlarda ayrışmak için şu teknolojiler "cephaneliğe" eklenmelidir:

# * **ML Ops:** Modeli canlıya aldıktan sonra izleme (monitoring), uyarı sistemleri (alerting) ve takip (tracking). Mülakatlarda en ayırt edici noktadır.
# * **Containerization:** **Docker**.
# * **Database:**
# * SQL: **PostgreSQL**.
# * NoSQL: **MongoDB**.


# * **Cloud Providers:** AWS, Google Cloud, Azure (İlanların çoğunda bulunur).

# ### Öğrenme Stratejisi

# * **GitBook:** Okunanları kendi cümlelerinizle not alın. ("Kendi yazdığınız bilgi, en hızlı hatırladığınız bilgidir.")
# * **GitHub:** Sadece kod depolamak için değil, teknik yetkinliği kanıtlamak için repolar oluşturun (OOP, AI, ML projeleri).
# * **Keywords:** LinkedIn profilinde ve CV'de RAG, LLM, Fine Tuning, PyTorch, Transformer gibi teknik terimlerin geçmesi, İK algoritmalarına takılmamak için kritiktir.