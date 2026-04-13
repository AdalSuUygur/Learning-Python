
#! Inheritance (Kalıtım)

#* Biyolojideki kalıtım mantığının yazılıma uyarlanmış halidir. 
# Bir Parent Class (Ata sınıf) özelliklerinin (attributes) ve yeteneklerinin (methods);
# Child Class (Alt sınıf) tarafından devralınması işlemidir.
#* Parent Class (Base Class): Özellikleri aktaran, genel çatıyı oluşturan sınıf.
#* Child Class (Sub Class): Özellikleri devralan, gerektiğinde bunları genişleten sınıf.

#? SYNTAX
# Python'da kalıtım, sınıf tanımlanırken parantez içinde ata sınıfın belirtilmesiyle sağlanır: `class Child(Parent):`.
#* Bir sınıfın içi boş olsa dahi, miras aldığı ata sınıfın tüm yeteneklerine (instance attributes, methods) otomatik olarak sahip olur.

class Human: #Ata sınıfı oluşturduk
    def __init__(self, full_name: str, weight: float, height: float):
        self.full_name = full_name
        self.weight = weight
        self.height = height

    def show_info(self):
        return self.__dict__

class FootSoldier(Human): #Bunlar da çocukları.
    pass

class Knight(Human):
    pass

# `FootSoldier` ve `Knight` sınıflarının içi boş (`pass`) olsa bile, `Human` sınıfındaki tüm özellikleri ve `show_info` metodunu kullanabilirler.
# Bunun kanıtı: 
fs1 = FootSoldier(full_name="burak", weight=100.03, height=1.83)
print(fs1.show_info())

#* "Python is all about object." Python'da her şey objedir ve tüm sınıfların en tepedeki atası **`object`** sınıfıdır.

#? Multiple Inheritance (Çoklu Kalıtım)
#* Implicit Inheritance: Python 3.x'te bir sınıf oluşturulduğunda (örn: `class Human:`), biz belirtmesek bile arka planda `class Human(object):` şeklinde çalışır.
#* Yani aslında python direkt olarak multiple inheritance (çoklu kalıtım) uygular.
#* Magic Methods: `__doc__`, `__dir__`, `__format__` gibi çift alt çizgili (underscore) metotlar, bu `object` sınıfından gelir.

# Bir **Child Class**'ın birden fazla **Parent Class**'tan aynı anda miras alabilmesidir.

#todo Case Study: Birds (Kuşlar)
# 1. Parent Classes:
# * `YuzebilenKus`: `yuzebilmek()` metoduna sahip.
# * `YuruyenKus`: `yurumek()` metoduna sahip.
# * `UcabilenKus`: `ucabilmek()` metoduna sahip.

class YuzebilenKus:
    def yuzebilmek(self):
        print("Yüzebilir kuşlar")

class UcabilenKus:
    def ucabilmek(self):
        print("Uçabilen kuşlar")

class YuruyenKus:
    def yurumek(self):
        print("Yürüyebilen kuşlar")

# 2. Child Classes:
# * Penguen: `class Penguen(YuzebilenKus, YuruyenKus)` -> Hem yüzme hem yürüme yeteneğini alır.
# * Kartal: `class Kartal(UcabilenKus, YuruyenKus, YuzebilenKus)` -> Hem uçma hem yürüme hem de yüzme yeteneğini alır.
# * Tavuk: `class Tavuk(YuruyenKus)` -> Sadece yürüme yeteneğini alır (Single Inheritance).

class Penguen(YuzebilenKus, YuruyenKus): #multiple inheritance
    pass

class Tavuk(YuruyenKus): #single inheritance
    pass

class Kartal(UcabilenKus, YuzebilenKus, YuruyenKus): #multiple inheritance
    pass

