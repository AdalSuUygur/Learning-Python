
#! ## Method Overriding
#* Ata sınıftan (Parent) miras alınan bir metodun, alt sınıfta (Child) ihtiyaca göre yeniden tanımlanarak davranışının değiştirilmesi veya geliştirilmesidir.
# Keyfi nedenlerle method override edilmez.

# Parentler organize edilirken alt sınıfların ortak özelliklerini barındırır.
# Base class'ların amaçları kalıtım vermektir. Bu yüzden instanceları alınmaz. (bu amaçla kullanılmaz.)

class BaseEntity: #* İsimlendirmenin başında "Base" görünce parent olduğunu anla!
    # Parent sınıflara sadece ortak olan özellikleri yazılır!
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description
    
    def show_info(self):
        print(
            f'Name: {self.name}\n'
            f'Description: {self.description}'
        )

#region Enhance
#? Enhance (Geliştirme/Genişletme)
#* Mevcut ata fonksiyonunun yeteneğini koruyup üzerine ekleme yapma işlemidir.

class Category(BaseEntity): # #Child: Ekstra bir özelliğe ihtiyaç duymaz. Parent'taki __init__ ve show_info yeterlidir. **Override edilmez.**
    pass

class Product(BaseEntity): #Child: price ve stock gibi kendine has özelliklere sahiptir. Ürünlerin price, stock gibi kendine has özellikleri olur.
    # Kendine has olduğu için alt sınıfa yazılır, override edilir. 
    #* Parenttan gelen özellikleri çağırmak için super() fonksiyonu kullanılır.

    def __init__(self, name, description, price: float, stock: int):
        super().__init__(name, description) #Parenttaki init'i çağırdık ve üzerine ekledik, override ettik.
        self.price = price
        self.stock = stock

    def show_info(self):
        super().show_info() #Parenttaki show_info'yu çağırdık ve üzerine ekledik, override ettik.
        print(
            f'Price: {self.price}\n'
            f'Stock: {self.stock}'
        )

p1 = Product(
    name='Boxing Gloves', 
    description='Boxing Gloves', 
    price=10.999, 
    stock=100)
p1.show_info()
#endregion

#region Replace
#? 2. Replace (Geçersiz Kılma/Ezme)
#* Ata sınıftan gelen metodun tamamen yok sayılıp, yerine yepyeni bir logic yazılmasıdır.

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
        return 'Genel telefon sesi'

class Iphone(BasePhone): #Parent Class: BasePhone

    def __init__(self, airdrop: str, phone_id, model, brand, price): #airdrop yok diğer cihazlarda ondan bunu ekledik.
        super().__init__(phone_id, model, brand, price) #Parenttaki initi çağırıp override ettik.
        self.airdrop = airdrop

    def show_info(self):
        super().show_info()
        print(f'Airdrop: {self.airdrop}')

    def phone_ring_sound(self): #ezdik. iphone için farklı bir tanımlama yaptık.
        return "iPhone telefon sesi"

class Samsung(BasePhone):
    
    def __init__(self, phone_id, model, brand, price, OS: str): #Samsungun kendine has yeteneği OS olsun
        super().__init__(phone_id, model, brand, price)
        self.OS = OS

    def show_info(self):
        super().show_info()
        print(f"Operating System: {self.OS}")

    def phone_ring_sound(self):
        return "Samsung telefon sesi"
    
#* *Polymorphism Bağlantısı:* phone_ring_sound fonksiyonu: Base, iPhone ve Samsung sınıflarında aynı isme sahip olmasına rağmen üç farklı çıktı üretir. 
#* Bu durum *Polymorphism* (Çok Biçimlilik) kavramının temelidir.
#* Aynı fonksiyonun farklı sınıflarda farklı işler yapmasına *Polimorfizm (Çok Biçimlilik)* denir.

samsung_1 = Samsung(phone_id=1, model='Galaxy 20', brand='Samsung', price=120.000, OS='Android')
samsung_1.show_info()
print(samsung_1.phone_ring_sound())

iphone_1 = Iphone(phone_id=2, model='Pro 16 Max', brand='Iphone', price=200.000, airdrop='True')
iphone_1.show_info()
print(iphone_1.phone_ring_sound())

#endregion

#todo Fatura Hesaplama (Bill System)

# BaseBill (Parent)
# Attributes: bill_name, value_added_tax (KDV)
# calculate_bill(amount): Vergili tutarı hesaplar.
# create_log(): Fatura detaylarını `.txt` dosyasına yazar.
# Child Classes: WaterBill (mill object attribute), NaturalGasBill (m3 object attribute), ElectricityBill (kw object attribute)

class BaseBill:
    def __init__(self, bill_name: str, value_added_tax: float, amount: float):
        self.bill_name = bill_name
        self.value_added_tax = value_added_tax
        self.amount = amount

    def calculate_bill(self):
        return self.value_added_tax * self.amount

    def create_log(self):
        file = open(file='bill_info.txt', mode='w', encoding='utf-8') #Yaratıcı dosyaya isim verdik, mode verdik (yazma amaçlı ondan write'in w'si)
        # Burdaki encoding de TR karakterlere duyarlı olması için
        file.write(f"Bill name: {self.bill_name}"\n
                   f"Total amount: {self.amount}"\n
                   f"Payment date: {self.value_added_tax}"))
        file.close()

# Override Edilmeyen: create_log çünkü su, gaz veya elektrik faturası fark etmeksizin loglama işlemi (isim ve tutar yazma) standarttır.
# Override Edilen: __init__ ve calculate_bill
# Her faturanın birimi farklıdır. Bu birimler __init__ içinde tanımlanmalı ve hesaplama (calculate_bill) bu birimlere göre özelleştirilmelidir.

class WaterBill(BaseBill):
    def __init__(self, bill_name, value_added_tax, amount):
        super().__init__(bill_name, value_added_tax, amount)

    def calculate_bill(self, unit):
        return super().calculate_bill(unit)
