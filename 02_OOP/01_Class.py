
#! Object Oriented Programming (OOP)

#? Class SYNTAX

class Araba: # Araba nesnesinin özelliklerini için 
    door_number = 0
    engine_size = 5.6
    torque = 500
    lenght = 3.1
    width = 1.2
    color = "papaya"
    brand = "Dodge"
    model = "TRX 1500"

#* Sınıfı tanımladıktan sonra o sınıftan nesne üretmeye **instance** (örneklem) çıkartmak denir.
a1 = Araba() # a1'in tipi Araba oldu.

# Nokta notasyonu ile a1 üzerinden fonksiyonlarına erişebiliyoruz artık.
# Tıpkı liste veya sözlüklerin kendi sınıflarına ait olması gibi, bizim yarattığımız nesneler de kendi tanımladığımız sınıflara ait olur. 
# İstediğimiz yerde, istediğimiz kadar nesne üretebiliriz.
a1.color = "pink"
print(f"Color: {a1.color}")
#* built in objelerle custom objeler arasında hiçbir fark yok!

#todo kendi class yaratma örneğim
class F1_Driver:
    name = "Oscar Jack Piastri"
    birth_year = 2001
    nationality = "Australian"
    team = "McLaren"
    car_number = 81
    wins = 9
    podiums = 27

favori_driver = F1_Driver()
favori_driver.name = "Carlos Sainz Jr."
# favori_driver.birth_year = 1994
# favori_driver.nationality = "Spanish"
# favori_driver.team = "Atlassian Williams"
# favori_driver.car_number = 55
# favori_driver.wins = 4
# favori_driver.podiums = 29

print(favori_driver.name)

# Special fonksiyonlar tüm sınıflarda ortak olarak bulunmaktadır.

#? Constructor (Yapıcı Fonksiyon): `__init__`
#* Nesne türetilirken arka planda otomatik olarak çalışan özel bir fonksiyon vardır. 
#* Diğer programlama dillerinde buna **Constructor** (yapıcı fonksiyon) denir.

# 1. **Sınıfı Başlatmak (Initialize):** Nesneyi RAM'e çıkartır ve hazırlar.
# 2. **Zorunlu Özellikler Belirlemek:** Nesne yaratılırken girilmesi zorunlu olan bilgileri (parametreleri) tanımlar.
# 3. **Atama Yapmak:** Dışarıdan gelen değerleri alıp, objenin kendi özelliklerine (attribute) atar.

#? SYNTAX YAPISI
# Bazı özellikler sınıf yaratılırken zorunlu olarak yaratılsınlar. Bu durumda: 
# __init__'i yazıyor ve zorunlu parametreleri ekliyoruz.

class Student:
    def __init__(self, full_name: str, student_id: str): # artık "Student" nesnesi yaratılırken full_name ve student_id zorunlu olarak eklenmeli.
        self.tam_ad = full_name
        self.ogrenci_id = student_id

#* test: s1 = Student() #burası patlıyor, neden? bak zorunlu parametreleri girmedik

s1 = Student(full_name="adal su uygur", student_id="12345")
print(s1.__dict__) #sözlük olarak yazdırmamızı sağlıyor.

#? Attributes: Class vs. Object Attributes
# OOP yapısında verilerin nerede tutulduğu kritiktir. İki tür özellik tanımlaması mevcuttur:
#* Class Attribute: Sınıf seviyesinde tanımlanır. O sınıftan türetilen **tüm** objeler tarafından ortaklaşa paylaşılır.
#* Object Attribute (Instance Attribute): `__init__` içinde `self` ile tanımlanır. Her objenin kendine has, benzersiz değeridir.

# Bir nesne üzerinden çağırdığımızda hem sınıfın genel özelliklerini hem de nesneye özel yaratılmış özellikleri görebiliriz.

class Ogrenci:
    # bu class attribute
    taken_courses = ["History", "Algorithm"]
    
    def __init__(self, full_name: str, student_id: str):
        self.tam_ad = full_name
        self.ogrenci_id = student_id #bunlar da object attributes

s2 = Ogrenci(full_name="ali veli", student_id="1234")
print(s2.__dict__)

# print(
#     f'Student Name: {s2.tam_ad}\n'
#     f'Student Id: {s2.ogrenci_id}\n'
#     f'Taken Courses: {s2.taken_courses}'
# )

# print(dir(Student))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
# '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
# '__str__', '__subclasshook__', '__weakref__', 'taken_courses']
#* Bunlar class attributes

# print(dir(s1))
# ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', 
# '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', 
# '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', 
# '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', 
# '__str__', '__subclasshook__', '__weakref__', 'ogrenci_id', 'taken_courses', 'tam_ad']
#* Bunlar da object attributes, farkları ne? bak classta sadece taken_courses varken burda alayı var.

#? Self Anahtar Kelimesi
# `__init__` veya sınıf içindeki diğer fonksiyonlarda kullandığımız `self` Keyword: Sınıf içerisinde, yaratılacak olan o anki **objeyi temsil eder**.
# O an işlem yapılan nesne ne ise `self` odur. 
# Başka isimler verilebilir ancak "best practice" (en iyi uygulama) olarak `self` kullanılması önerilir.
# Neden Kullanılır? Sınıfın yeteneklerine (methods) ve özelliklerine (attributes) erişmek için kullanılır.

#todo `Circle` Classı ve üretilen objeleri

#* Attribute Ayrımı: `Pi` sayısı sabittir, `Class Attribute` yapılır. `radius` (yarıçap) değişkendir, `Object Attribute` yapılır.
#* Erişim: Obje, sınıfın tüm özelliklerine sahiptir. `self.Pi` diyerek de sınıf özelliğine erişilebilir.

class Circle:
    pi = 3.14

    def __init__(self, r: int): #dışarıdan bir r değeri gelcek
        """buraya da dökümantasyon yapılabilir
        """
        self.radius = r #self yaratılan objeyi temsil eder

#circle sınıfına 2 tane daha kabiliyet verelim: 
    def calculate_area(self):
        return self.pi * self.radius **2
    
    def calculate_perimeter(self):
        return 2 * self.pi * self.radius

c1 = Circle(r = 1.02) #instance alıyoruz yani obje yaratıyoruz ve bu bizden bir yarıçap bekliyor.
print(c1.calculate_area()) #bunlara nokta notasyonu ile eriştik.


# #region Examples

# #todo Kendi sınıf tanımlamam:
# class Character:
#     age = 29
#     skin_tone = "Yellow"
#     hair = 0
#     accesories = "earrings"

# cagirma_nesnem = Character() #sınıftan örneklem çıkartıyoruz
# cagirma_nesnem.age = 86 #nokta notasyonu ile obje üzerinden sınıfın özelliklerine erişiyoruz
# print(cagirma_nesnem.age)


# #todo Department Example (Sayaç Mantığı) Bir departmandaki çalışan sayısını takip etmek için yapılan hata ve doğru kullanım
# # 1. Senaryo: `Department` sınıfı her örneklendiğinde çalışan sayısını artırmak istiyoruz.
# # 2. Hatalı Kullanım (`self` ile Erişim):
# #* `self.employee_count += 1` derseniz, her yeni obje için `employee_count` değeri sıfırlanıp 1 olur. Çünkü `self` o anki yeni, taze objeyi (fresh instance) temsil eder.
# # 3. **Doğru Kullanım (`Class Name` ile Erişim):**
# #* `Department.employee_count += 1` kullanılmalıdır. Bu sayede RAM'de tek bir yerde tutulan ortak sınıf özelliğine erişilir ve sayaç kümülatif olarak (1, 2, 3...) artar.

# class Department:

#     #Bunlar class attributes üretir
#     department_name = ""
#     employee_count = 0
    
#     def __init__(self, name: str, age: int):
#         self.adi = name # türkçe obje attribute'u, ingilizce dışardan gelen attribute.
#         # yani bu sınıftan örneklem aldığımda bunlar yaratılacak (runtime olarak)
#         self.yasi = age
#         # self.employee_count += 1 
#         # burda self ile çağırdığımızda hep her seferinde 0dan başlatıldığı için çıktı olarak 1 1 1 olarak verdi

#         # Department'ın employee count'ını çağırdığımızda:
#         Department.employee_count += 1
#         # Çıktı +1 olarak artarak ilerler.

#     def show_info(self):
#         print(
#             f"Name: {self.adi}\n"
#             f"Age: {self.yasi}\n"
#             f"Department Name: {self.department_name}"
#         )

#     #her instance alındığında (obje çağrıldığında/yaratıldığında) employee sayısını bir artırmış olduk.

#     def show_employee_count(self):
#         print(f"Total emplotee: {self.employee_count}")

# d1 = Department("Adal", 29)
# d1.department_name = "YZTA"
# d1.show_info()
# d1.show_employee_count()

# d2 = Department("Yasemin", 34)
# d2.department_name = "Teacher"
# d2.show_info()
# d2.show_employee_count()

# d3 = Department("Habiba", 36)
# d3.department_name = "Teacher"
# d3.show_info()
# d3.show_employee_count()


# #todo SoftwareDeveloper Class Challenge: Bir yazılımcı sınıfı oluştururken "Bildiği Diller" listesinin yönetimi üzerine vaka analizi.
# # Sınıfın: first_name, last_name object attibuteleri olsun
# # knowledge_languages adlı bir liste class attribute'u olsun
# #challenge şu, bildiği dilleri bu listeye yazıcaz.
# #add_new_language() adlı bir fonksiyon olacak.
# #sample input --- "python, c#, go" veya "python" olarak gelebilir. Buna göre parçalayıp her biri bir item olarak listeye eklenecek.

# #* Problem: `knowledge_languages` listesi Class Attribute mu yoksa Object Attribute mu olmalı?

# class SoftwareDeveloper():
#     knowledge_languages = [] #class attribute olarak yarattık.
    
#     def __init__(self, first_name: str, last_name: str): #bunları obje attribute'u olarak.
#         self.first_name = first_name
#         self.last_name = last_name

#     def add_new_language(self, input_language: str):
#         language_lst = input_language.split(',') #language bize string olarak geliyor ancak bunu bölmemiz gerek.

# # Veri İşleme (String Parsing):
# # Kullanıcıdan gelen "Python, C#, Go" şeklindeki string veriyi işlemek için:

# # 1. **Split:** `input_string.split(",")` ile veriyi virgülden bölerek listeye çevir.
# # 2. **Strip:** Boşlukları temizlemek için `.strip()` kullan.
# # 3. **Logic:** Tek eleman gelirse direkt ekle, çoklu gelirse döngü ile ekle.

#         for item in language_lst:
#             if item not in self.knowledge_languages:
#                 self.knowledge_languages.append(item)
#         return "Language has been added."


#     def show_info(self):
#         print(
#             f"Full Name: {self.first_name} {self.last_name}\n"
#             f"Known Languages: {self.knowledge_languages}" #burda neden bu şekilde eriştik? çünkü herkesin bildiği dil kendisine
#         )

# s1 = SoftwareDeveloper("Adal", "Uygur")
# print(s1.add_new_language("python, c#, c++, java, vb.net"))
# s1.show_info()

# #* Yanlış Yaklaşım (Class Attribute): Eğer liste sınıf seviyesinde tanımlanırsa (`knowledge_languages = []`), `append` yapılan her dil tüm yazılımcı objelerine eklenir. 
# # Ali'nin bildiği dili Veli de biliyor gözükür.
# #* Doğru Yaklaşım (Object Attribute): Her yazılımcının yetkinliği kendine özgü olmalıdır. Bu yüzden `__init__` içinde `self.knowledge_languages = []` olarak tanımlanmalı 
# # ve her obje için RAM'de taze/boş bir liste açılmalıdır.
# #endregion
