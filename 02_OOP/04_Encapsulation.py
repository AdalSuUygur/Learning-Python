
#! Encapsulation (Bilgi Gizleme)
#* Encapsulation, sınıfın bazı üyelerinin dış erişime kapanması demektir.
# Yani, sınıflarda tanımlanmış özelliklerin kendi dışında hiçbir yerden erişilemesin/değiştirilememesine denir.

# Python'da bunu yapmak için "__" (double underscore) sembolünü kullanılır.
# Başka programlama dillerinde (C#, Java) bunun için "private" anahtar kelimesi kullanılırken Python sembollerle bu işi görür.

#? SYNTAX

from uuid import uuid4
from datetime import datetime
from socket import gethostname, gethostbyname
from enum import Enum
from pprint import pprint

class BaseEntity():
    def init(self):
        self.__id = None
        self.__create_date = None
        self.__computer_name = None
        self.__ip_address = None #erişime kapatıldı
        self.status = None #erişime kapatılmadı
    
    def set_values_private_attributes(self):
        self.__id = None
        self.__create_date = None
        self.__computer_name = None
        self.__ip_address = None #erişime kapatıldı
        self.status = None #erişime kapatılmadı

# Instance alalım:
b1 = BaseEntity()
b1.__id
b1.status

# Kalıtım alan farklı bir sınıftan erişmeye çalışsak:
class Supplier(BaseEntity):
    pass #erişilemiyor.


# Peki, madem dış erişimi kapattık, bu değerlere nasıl ulaşacağız? 
# Bunlara dolaylı yolla, yani **Getter** ve **Setter** metotları üzerinden erişeceğiz.


# Bir kural doğrultusunda değer atamak istediğimizde encapsulation çok işe yarar. 
# Örneğin bir `Product` sınıfında `price` ve `stock` değerlerini private yapalım. 
# Dışarıdan bir değer girildiğinde, bu değerin sıfırdan büyük olup olmadığını kontrol eden bir `set_values` fonksiyonu yazabiliriz. 
# Eğer kullanıcı yanlışlıkla eksi bir değer girerse, sistem bunu kabul etmez. Böylelikle veri güvenliğini ve tutarlılığını sağlamış oluruz.

# Ayrıca **Enum** yapısından da bahsetmek lazım. 
# Enum, sabitlerimizi tanımladığımız bir yapıdır. 
# Değişmeyecek değerleri (örneğin fiziksel sabitler, matematiksel katsayılar) burada tutabiliriz. 
# Ancak çok sık değişen şeyleri (örneğin kullanıcı rolleri) Enum içinde tutmak mantıklı değildir; 
# çünkü her değişiklikte kodu güncelleyip yeniden "deploy" etmeniz gerekir. 
# Deployment sancılı bir iştir, o yüzden sabit olmayan şeyleri veri tabanında tutmak daha doğrudur.

# ---
