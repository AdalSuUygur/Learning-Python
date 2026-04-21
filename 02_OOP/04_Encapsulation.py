
#! Encapsulation (Bilgi Gizleme)
#* Encapsulation, sınıfın bazı üyelerinin dış erişime kapanması demektir.
# Yani, sınıflarda tanımlanmış özelliklerin kendi dışında hiçbir yerden erişilemesin/değiştirilememesine denir.

# Python'da bunu yapmak için "__" (double underscore) sembolünü kullanılır.
# Başka programlama dillerinde (C#, Java) bunun için "private" anahtar kelimesi kullanılırken Python sembollerle bu işi görür.

#? SYNTAX

from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum # Enum, sabitlerimizi tanımladığımız bir yapıdır.
from pprint import pprint

# class BaseEntity():
#     def init(self):
#         self.__id = None #erişime kapatıldı
#         self.__create_date = None #erişime kapatıldı
#         self.__computer_name = None #erişime kapatıldı
#         self.__ip_address = None #erişime kapatıldı
#         self.status = None
#     hello = 1 #bu helloya erişebiliyoruz.
    
#     def set_values_private_attributes(self):
#         self.__id = None #erişime kapatıldı
#         self.__create_date = None #erişime kapatıldı
#         self.__computer_name = None #erişime kapatıldı
#         self.__ip_address = None #erişime kapatıldı
#         self.status = None

# # Instance alalım:
# b1 = BaseEntity()
# b1.__id
# b1.status

# # Kalıtım alan farklı bir sınıftan erişmeye çalışsak:
# class Supplier(BaseEntity):
#     pass #erişilemiyor.

#? Dış erişimi kapattık, nasıl bu değerlere ulaşacağız? 
#* Bunlara dolaylı yolla, **Getter** ve **Setter** metotları üzerinden erişilir.

class Status(Enum):
    Active = 1
    Modified = 2
    Passive = 3

class BaseEntity:
    def __init__(self):
        self.__id = None
        self.__create_date = None
        self.__computer_name = None
        self.__ip_address = None
        self.__status = None

# Bunlar sınıf dışında erişilemiyor diye default değer atamalarını yaptık.
# dolaylı yolla değer atamak için yazdığımız fonksiyonun başına set yazarız.
    def set_values_private_attributes(self):
        self.__id = uuid4()
        self.__create_date = datetime.now()
        self.__computer_name = gethostname()
        self.__ip_address = gethostbyname(gethostname())
        self.__status = Status.Active

#* Bir fonksiyonu da tamamen dış erişime kapatabiliriz.
    def __hello(self):
        print("Dış erişime kapatıldı.")

class Product(BaseEntity): #çocuk sınıfı yazdık
    def __init__(self, name: str, description: str):
        super().__init__()
        self.description = description
        self.name = name
        # price ve stock değerleri encapsule olarak alınır.
        self.__price = None
        self.__stock = None

#* Olması gereken teker teker yazmak set ve getlerini yazmak.
    def set_values_product_attributes(self, price: float, stock: int):
        if price > 0 and stock > 0:
            super().set_values_private_attributes()
            self.__price = price
            self.__stock = stock
            print('Product has been created')
            pprint(self.__dict__)
        else:
            print('Invalid inputs..!\nProduct has not been created..!')

p1 = Product(name='Boxing Gloves', description='A boxing gloves')
p1.set_values_product_attributes(price=50, stock=10)
