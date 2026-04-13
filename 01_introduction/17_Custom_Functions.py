
#! Custom Functions
#* Fonksiyonlar, devamlı aynı işi yapan yapılara denir.
#* Bu kod blokları programın istenilen herhangi bir yerinde çağırılmasını sağlar ve kodlarımız lineer olarak çalışmaz.
#* Bu da fonksiyonel programming olur. Clean coding felsefesine de uygundur.

# #custom yazdığımız fonksiyonları da istediğimiz zaman istediğimiz yerde çağırıp kullanıcaz
#? SYNTAX
#* Fonksiyonu tanıtmak/define etmek için "def" anahtar sözcüğü kullanılır.

def greeting_people(): #def ile "greeting_people" adlı fonksiyonu tanıttık.
    print("Hello World!") #artık fonksiyonumuz tanımlandı ve işini yapıyor.

#* Fonksiyonu programın herhangi bir yerinde çağırmak için fonksiyonun execute edilmesi gerek.
greeting_people() #bu da execution kısmı.
# Artık bu tanımlanmış fonksiyonu istediğim yerde istediğim kadar kullanabilirim

#? Parametre alan, almayan ve default değeri olan fonksiyonlar:
def greeting_people(): # Parametre almayan fonksiyon
    print("Hello!")
greeting_people # fonksiyonu çağırmak/execute etmek.

def greeting(full_name: str): # Parametre alan fonksiyon
    print(f"Hello, {full_name}!")
greeting(full_name="Adal") # fonksiyonu çağırmak/execute etmek.
# Burada ise greeeting() yazıp bir içerik göndermezsek patlar.

def greeting_default(full_name: str = "User"): #parametre alan ve default değeri olan fonks
    print(f"Hello, {full_name}!")
greeting_default() # fonksiyonu çağırmak/execute etmek. Burda değer girilmediyse default değer gelir.
greeting_default(full_name="Adal") # Bu şekilde default değerin üzerine yazarsak da default değer ezilir ve en son yazılan gelir.

#? Fonksiyonlarda tanımlama yapmak:
#* Bunu yapabilmek için 1 autodocs extension'ı kurulumu olmalı

# 1. Adım: Fonksiyon tanımla:
def generate_docs(a: int, b:int):
    # 2. Adım: 3 kere konsol tuşuna tıkla.
    """Bu fonksiyon 2 tane tam sayı toplar.
    Args:
        a (_type_): integer tipinde tam sayı
        b (_type_): integer tipinde tam sayı
    """
    # 4. Adım: gelen Docstring'i seç.
    # 5. Adım: İçeriğini uygun şekilde doldur.
    print(a+b)

#region Examples about defining a function
#todo FullName ve DomainName olan data ile kurumsal mail adresi craft etmek
# full_name = input("Lütfen isminizi giriniz: ")

# def create_email(full_name: str, domain_name: str): #2 tane inputa ihtiyacımız var, birisi isim diğeri domain name
#     names = full_name.lower().split(" ")
#     print(f"Mail adresses: {names[0]}.{names[-1]}{domain_name}")

# create_email(full_name="adal su uygur", domain_name="@outlook.com")
# #firmanın kurumsal mail adresi sabittir.

# #default değeri olacak parametrelere tip geçtikten sonra yanına eşittir koyup değer geçebiliyoruz.
# def create_mail(full_name: str, domain_name: str = "@skilledHub.com"): #buraya default değer verdim diye bunu ezemeyeceğim anlamına gelmiyor
#     names = full_name.lower().split(" ")
#     print(f"Mail adresses: {names[0]}.{names[-1]}{domain_name}")

# #bu ezmediğimiz değerli hali
# create_mail(full_name="adal su uygur")

# #bu da ezdiğimiz değerli hali
# create_mail(full_name="adal su uygur", domain_name="@xyz.com")

#todo 3 sayıyı çarpan bir fonksiyon
#* Burdaki çıkarım: default değerlerin önemi
# def multiply(number_1: float, number_2: float, number_3: float):
#     print(number_1 * number_2 * number_3)
# multiply(12,24) # Burada eksik argüman gönderdik ve çalıştırmaya çalıştığımızda patladık.
# # Patlamasının sebebi: Missing Parameter

# def multiply(number_1: float = 1, number_2: float = 1, number_3: float = 1):
#     print(number_1 * number_2 * number_3)
# multiply(12,24) # Bu şekilde eksik argüman gönderdiğimizde program patlamasın diye default değer tanımlıyoruz

#todo dairenin alanı hesaplayan fonksiyon
#* Burdaki çıkarım: bir parametreye birden fazla tip gelebilir.

# def calculate_area_disk(radius: int | float, pi = 3.1415): #radius değeri hem int olabilir hem de float olabilir.
#     """
#     Docstring for calculate_area_disk
    
#     :param radius: Description
#     :type radius: int | float
#     :param pi: Description
#     """
#     print(radius**2 * pi)
# calculate_area_disk(3)
#endregion

#? Returnable (Değer Döndüren) Fonksiyonlar
#* Fonksiyon çalışacak, ve çalışması tamamlandığında bir değer dönecek.
#* Dev ile bu değeri alıp farklı bir yerde kullanacak.

def pow_number(x: int = 1, pow: int = 1) -> int: # -> int demek bu fonksiyon integer olarak dönecek demektir.
    """Bir tam sayının kuvvetini hesaplayan fonksiyon
    Args:
        x(int): Kuvveti alınacak sayı, integer
        pow(int): kuvvet değeri, integer
    Returns:
        int: sonuç
    """
    return x ** pow # x üzeri pow değeri dönecektir.
#return altında kalan kodlar çalıştırılmaz.

#Burada built-in fonksiyon yapılarındaki gibi, return edilen değeri bir değişkene atamamız lazım.
result = pow_number(x=2,pow=9)
print(result)

#* Not: Inputlar fonksiyonun içinde olmaz, neden? Çünkü değerler dışarıdan geliyor, içerde tanımlanmıyor gibi düşün.

#* Neden fonksiyon yazılır? Daha kaliteli, okunabilir ve debug edilebilir kod yazmak için.
#* Fonksiyon yazarken iki ana ilkemiz var: 
# Single Responsibility Principle (SRP): Bir fonksiyonun sadece bir görevi olur. Neden?
# Çünkü birden fazla görevi olan fonksiyonlarda bir görevi fixlerken diğerini bozabilirsin. Yani maintaince için sürekli değiştirmek zorunda kalmamak için.
#* böl parçala yönet :D

#* ve Seperation of concern (SOC): Evindeki odaların ayrılması gibidir; mutfakta yemek pişer, banyoda duş alınır.

#region Examples about functions that returns a value

#todo Kullanıcıdan alınan 3 adet sayıyı toplayan fonksiyon

# def addition(x: int = 0, y: int= 0, z:int= 0) -> int:
#     return x+y+z
# toplam = addition(
#     x= int(input("İlk sayi: ")),
#     y= int(input("İkinci sayi: ")),
#     z= int(input("Üçüncü sayi: "))) #diye burada da istenebilir değerler
# print(toplam)

#todo Verilen cümleden tekrar eden kelimelerden arındırarak string formatında çıktı veren fonksiyon
sample_input = "merhaba ben adal adal ben merhaba merhaba adal adal adal"

def remove_duplicate_word(sentence: str) -> str:
    #* Path I - junior çözümü
    # lst = [] #geçici liste
    # for item in sentence.split():
    #     #kelime kelime dolaşır
    #     if item not in lst:
    #         lst.append(item)
    
    # str_output = " ".join(lst)
    # return str_output

    #* Path II - Senior çözümü
    # lst_1 = [item for item in sentence.split()]
    # lst_2 = set(lst_1)
    # str_output = " ".join(lst_2)
    # return str_output

    #* Path III - Cool jojuq çözümü
    return " ".join(set([item for item in sentence.split()]))

result = remove_duplicate_word(sample_input)
print(result)

#todo Rastgele üretim aralığı verilen sayıları verilen miktarda ürettiren fonksiyon
# from random import randint

# def number_generator(amount: int, start_point: int, end_point: int) -> list:
#     return [randint(a=start_point, b=end_point) for _ in range(amount)]

# def find_even_odd(number_lst: list[int]):
#     even_lst = []
#     odd_lst = []
#     for number in number_lst:
#         if number % 2 == 0:
#             even_lst.append(number)
#         else:
#             odd_lst.append(number)
#     return even_lst, odd_lst

# no_generator = number_generator(amount=10, start_point=0, end_point=9)
# print(no_generator)
# even_list, odd_list = find_even_odd(number_lst=no_generator)
# print(even_list)
# print(odd_list)

#todo Ödev (22 Aralık Ödevi-1): Rakamlardan oluşan bir liste içerisinde bulunan rakamların geçme sıklığını bulan fonksiyonları main() fonksiyonu ile execute eden uygulama
#* Çıktısı aşağıdaki formatta olmalı:
{
    1: 10, #1den 10 tane üretti
    2: 30, #2den 30 tane üretti
    #... böyle tüm rakamları saydıran
}

# def main():
#     from random import randint

#     def random_figure_generator(count: int = 100) -> list:
#         """Verilen sayı kadar rastgele rakam üreten fonksiyon
#         :param count: Üretilecek sayı miktarı
#         :type count: int
#         :return: Üretilen sayıların geri dönüşü
#         :rtype: list
#         """
#         return [randint(a= 0, b=9) for _ in range(count)]

#     def number_counter(number_list: list = []) -> dict:
#         """Verilen listedeki sayıları sayan fonksiyon

#         :param number_list: Integer sayılardan oluşan bir liste.
#         :type number_list: list
#         :return: Keylerin sayıları ve valueların kaç kere döndürdüğünü veren blok.
#         :rtype: dict
#         """
#     # Path III: Pythonic yol?
#         counter = {}
#         for n in number_list: counter[n] = counter.get(n, 0) + 1
#         return counter
#     # Path II: Bence daha amatörce yol:
#     # for number in number_list:
#     #     if number in counter:
#     #         counter[number] += 1
#     #     else:
#     #         counter[number] = 1
#     # pprint(f"In list {number_list} ve have {counter}")
#     # Path I:
#     # (counter[number] += 1 if number in counter else counter[number] = 1 for number in number_list)
#     # bu kodum çalışmyıor çünkü generator bir işlem yapmıyor bu da syntax hatası veriyor. Ayrıca dict comprehensiona da uygun değil
#     # yine işlem sonucunda ekleme yapmak yerine sözlüğe ekleme yaptığım için list comprehension falan da yapamıyorum.

#     def print_dict(input_dict: dict = None):
#         if input_dict is None:
#             input_dict = {}
#         print("{") 
#         for key in sorted(input_dict.keys()): #Tüm keyleri çekiyoruz, ve sıralı şekilde yazdırmak istiyoruz.
#             value = input_dict[key]
#             print(f"  {key}: {value}") # Her satırın başına boşluk (indent) ekleyerek daha düzenli yapıyoruz
#         print("}")

#     print_dict(number_counter(random_figure_generator(100)))

# #pprint ile çıktıyı güzelleştirebilirdik.
# #Counter ile saydırabilirdik.
# #Muhtemelen random sayı üreten de bir fonksiyon vardır ama biz kendimiz yazdık hepsini.
# main()

#todo Ödev (22 Aralık Ödevi-2): Girilen bilgilerin doğruluğunu check eden fonksiyon yapılarıyla kurulmuş uygulama
#* Sign in ve Sign up
#* Sign up işleminde kullanıcının girdiği password valid mi, user_name unique mi? e_mail valid mi?
#* Kurallardan geçerse üyelik işlemi tamamlanacak
#* Sign in'da password doğru mu, e-mail ve password doğruysa giriş yap
#* Tüm bu problem main() fonksiyonu içinde çalışacak

# users = {
#     "adal@skilledhub.com": "Adal.123",
#     "su@outlook.com": "Su.123",
#     "ahmet@gmaiwindowslive.com": "Ahmet.123",
#     "mehmet@skilledhub.com": "Mehmet.123",
#     "kerim@hotmail.com": "Kerim.123",
#     "kemal@yahoo.com": "Kemal.123",
#     'xyz.xyz@skilledhub.com': 'pwd',
#     'qwe.qwe@skilledhub.com': '987'
#     }

# import string

# #region Doğrulayıcılar

# def is_valid_password(password: str) -> bool: #uygunsa true, değilse false olarak döner
#     min_character = 6
#     if len(password) <= min_character:
#         return False
#     if any(ch.isspace() for ch in password): #burda da boşluk var mı yok mu
#         return False
    
# # gelen passwordu setten geçireceğiz ama neden?
#     ch_set = set(password)
# # kontrol etmek için döngüye sokmadan önce performans sağlamak için.

#     checks = [
#     any(ch.islower() for ch in ch_set),
#     any(ch.isupper() for ch in ch_set),
#     any(ch.isdigit() for ch in ch_set),
#     any(ch for ch in ch_set if ch in string.punctuation)
#             ]
#     return all(checks)

# def is_valid_email(mail_adresses: str) -> bool: #bool ihtiyacımız oldu aşağıdaki sign up kısmı için ondan sildik
#     try:
#         if "@" not in mail_adresses:
#             raise TypeError("The mail adress must contain the @ symbol.")
#         if mail_adresses in users.keys():
#             raise ValueError("This mail adress has already taken.")
#         return True #iflerden geçerse true dönecek
    
#     except (TypeError, ValueError) as err:
#         print(err) #bu da kendimize log gibi düşün
#         return False

# #region işlemler
# def sign_up(mail_adresses: str, password: str) -> str:
#     if is_valid_password(password=password) and is_valid_email(mail_adresses=mail_adresses):
#         users[mail_adresses] = password
#         return "Your membership has been completed!"
#     else:
#         return "Invalid credentials."

# def sign_in(mail_adresses: str, password: str) -> str:
#     for key, values in users.items():
#         if key == mail_adresses and values == password:
#             return f"Welcome to the jungle"
#     return "Invalid credentials."

# def main():
#     while True:
#         process = input("Type a process: ")

#         match process:
#             case "sign in":
#                 sign_in(
#                     mail_adresses= input("Mail adress: "),
#                     password= input("Password: ")
#                 )

#             case "sign up":
#                 sign_up(
#                     mail_adresses= input("Mail adress: "),
#                     password= input("Password: ")
#                 )
#                 print(users) #kendimize backdoor
#             case _:
#                 print("Type a valid process name.")

# main()









#endregion

#! *args vs **kwargs
#? args ve keywords and their operators
# fonksiyonumuza gelecek değerlerin sayısını yönetemediğimiz/bilemediğimiz durumlarda kullandığımız iki yapı.
# Fonksiyonlara gelen değerleri argümanlarla karşılıyorduk.

#* Burada önemli olan "*" ve "**" operatörleridir. args ve kwargs kısmı isimlendirmedir.
#* *args gelen parametreleri tuple olarak; **kwargs ise dict olarak tutar.

#region Examples about *args and **kwargs

#todo: *args kullanımının örneği:
# def total(*args): #fonksiyon tanımı
#     return sum(args)

# print(total(1, 2, 3)) #Çıktısı: 6
# print(total(9, 8, 12, 45, 23)) #Çıktısı: 97
# print(total()) #Çıktısı: 0

#todo *args kullanımının string üzerindeki örneği:
# def concat_str(*args, seperator: str = " "): #dinamik şekilde gelecek string ifadeleri
#     return seperator.join(args) #birleştiriyoruz

# print(concat_str("burak", 'yılmaz', '36')) #Çıktısı: "burak yılmaz 36"
# print(concat_str("bugün", 'sınıf', 'mevcudu', 'çok', 'az')) #Çıktısı: bugün sınıf mevcudu çok az

#todo *args kullanımı 
from datetime import datetime

# def system_log(*args): #Kaç tane mesaj geliyosa onu yazdıracağımız bir fonksiyon
#     for msg in args:
#         print(f"System log: {msg}\n"
#               f"Log Date: {datetime.now()}") #datetime.now() Şu anı veriyor.

# system_log('Status Code --> 200', 'DB Connection has been lost', 'Passive')

# """ Çıktısı: 
# Log Date: 2026-01-03 21:11:54.248049
# System log: DB Connection has been lost
# Log Date: 2026-01-03 21:11:54.248049
# System log: Passive
# Log Date: 2026-01-03 21:11:54.248049
# """

#todo: **kwargs arguments örneği
# # Parametreler sözlük olarak gittiği için değerlere erişimimiz hashmap mantığı.
# def get_info(**kwargs):
#     return (
#         f'Full Name: {kwargs.get("full_name")}\n'
#         f'Occupation: {kwargs.get("occupation")}\n'
#         f'Alias: {kwargs.get("alias")}'
#     )

# print(get_info(full_name='Burak Yılmaz'))
# print(get_info(full_name='Hakan Yılmaz', occupation='Chemist'))
# print(get_info(full_name='İpek Yılmaz', occupation='Art Historian', alias='keko'))

# """ Çıktısı:
# Full Name: Burak Yılmaz
# Occupation: None
# Alias: None
# Full Name: Hakan Yılmaz
# Occupation: Chemist
# Alias: None
# Full Name: İpek Yılmaz
# Occupation: Art Historian
# Alias: keko
# """

#todo makine bilgilerine kwargs ile erişme uygulaması
from socket import gethostname, gethostbyname

# def log(*args, **kwargs):
#     return (
#         f'Message: {kwargs.get("msg")}\n'
#         f'IP Address: {kwargs.get("ip_address")}\n'
#         f'Machine Name: {kwargs.get("machine_name")}\n'
#         f'Exception Date: {kwargs.get("exception_date")}\n'
#     )

# print(
#     log(
#         msg='Internal Gateway', 
#         ip_address=gethostbyname(gethostname()), 
#         machine_name=gethostname(), 
#         exception_date=datetime.now()
#     )
# )

