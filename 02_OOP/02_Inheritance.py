
#! Inheritance (Kalıtım)

#* Biyolojideki kalıtım mantığının yazılıma uyarlanmış halidir. 
# Bir Parent Class (Ata sınıf) özelliklerinin (attributes) ve yeteneklerinin (methods) Child Class (Alt sınıf) tarafından devralınması işlemidir.
#* Parent Class (Base Class): Özellikleri aktaran, genel çatıyı oluşturan sınıf.
#* Child Class (Sub Class): Özellikleri devralan, gerektiğinde bunları genişleten sınıf.

#? SYNTAX
# Python'da kalıtım, sınıf tanımlanırken parantez içinde ata sınıfın belirtilmesiyle sağlanır: class Child(Parent):
#* Bir sınıfın içi boş olsa dahi, miras aldığı ata sınıfın tüm yeteneklerine (instance attributes, methods) otomatik olarak sahip olur.

class Human: # Ata sınıfı/Parent Class oluşturduk
    def __init__(self, full_name: str, weight: float, height: float):
        self.full_name = full_name
        self.weight = weight
        self.height = height

    def show_info(self):
        return self.__dict__

class FootSoldier(Human): #Bunlar da çocukları. Parent da parantez içindeki bak.
    pass

class Knight(FootSoldier): #Bunun da atası FootSoldier oldu.
    pass

# Child classlarının içi boş bile olsa parent classındaki tüm özellikleri metotları kullanabilirler.
# Bunun kanıtı: 
foot_soldier_1 = FootSoldier(full_name="burak", weight=100.03, height=1.83)
print(foot_soldier_1.show_info())

knight_1 = Knight(full_name="ali", weight=123, height=2.03)
print(knight_1.show_info())

# nokta notasyonu ile knight_1. baktığımızda, __xxx__ böyle bir şeyler görüyoruz. Neden?
#* "Python is all about object." 
# Python'da her şey objedir ve tüm sınıfların en tepedeki atası -object- sınıfıdır.
# Yani bu şekilde object sınıfındaki her metoda ulaşabiliyoruz.

#region Multiple Inheritance (Çoklu Kalıtım)
#? Multiple Inheritance (Çoklu Kalıtım)
#* Bir **Child Class**'ın birden fazla **Parent Class**'tan aynı anda miras alabilmesidir.

# Biz şimdiye kadar **Single Inheritance** yaptık; yani sınıfların sadece bir atası var.
# Python direkt olarak multiple inheritance (çoklu kalıtım) uygular.

#todo Case Study: Kuşlar
# Parent Classes:
# * YuzebilenKus: yuzebilmek() metoduna sahip.
# * YuruyenKus: `yurumek() metoduna sahip.
# * UcabilenKus: ucabilmek() metoduna sahip.

class YuzebilenKus:
    def yuzebilmek(self):
        print("Yüzebilir kuşlar")

class UcabilenKus:
    def ucabilmek(self):
        print("Uçabilen kuşlar")

class YuruyenKus:
    def yurumek(self):
        print("Yürüyebilen kuşlar")

# Child Classes:
# * Penguen -> Hem yüzme hem yürüme yeteneğini alır.
# * Kartal -> Hem uçma hem yürüme hem de yüzme yeteneğini alır.
# * Tavuk -> Sadece yürüme yeteneğini alır (Single Inheritance).

class Penguen(YuzebilenKus, YuruyenKus): # multiple inheritance
    pass

class Tavuk(YuruyenKus): # single inheritance
    pass

class Kartal(UcabilenKus, YuzebilenKus, YuruyenKus): # multiple inheritance
    pass

penguen_1 = Penguen()
penguen_1.yurumek()
penguen_1.yuzebilmek()

#endregion
