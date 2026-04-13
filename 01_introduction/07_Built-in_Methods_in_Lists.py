
#! Listelerde Yerleşik Metodlar (Built-in Method)
#* Bu metotlar, liste adından sonra nokta (.) (Bu duruma nokta notasyonu denir) koyularak çağrılır.
#* Sadece List sınıfına ait metodlardır.
#* Ait olduğu nesne üzerinden doğrudan değişiklik yapar.

#todo Listelerde metot kullanımı: 
drivers = [
    "Oscar Piastri", "Lando Norris", 
    "George Russell", "Kimi Antonelli",
    "Max Verstappen", "Yuki Tsunoda",
    "Charles Leclerc", "Lewis Hamilton"]
print(drivers) #buraya herhangi bir şey eklemedik yani albon'u görmeyeceğiz.

#? append()
drivers.append("Alexander Albon") #Append metodu ile albonu liste sonuna ekledik
print(drivers) #burada ise albonu görürüz

#? insert()
drivers.insert(1,  "Carlos Sainz") #Insert metodu ile 1. index değerine "Carlos Sainz"'i sıkıştırdık.
print(drivers) #Burada 1. indexte sainzi görürüz

last_drivers = [
    "Liam Lawson", "Isack Hadjar",
    "Esteban Ocon", "Oliver Bearman",
    "Lance Stroll", "Fernando Alonso", 
    "Nico Hulkenberg", "Gabriel Bortoleto"
    "Pierre Gasly", "Franco Colapinto"
] #yeni bir liste tanımladık ve burada kalan diğer driverları yazdık.

#? extend()
drivers.extend(last_drivers) #drivers listesine last_drivers listesini ekledik
print(drivers) #burada iki listenin birleşmiş halini görürüz

#? indexteki değeri çekmek list_name[index]
print(drivers[2]) #Bu 2. indexteki değeri çekiyor, print fonksiyonu ile de yazdırdık.

#? indexteki değeri değiştirmek
drivers[4] = "DUTDUT DURUT" #MAX VERSTAPPEEEEN!
print(drivers) #4. Indexteki değeri (Kimi Antonelli) "DUTDUT DURUT" ile değiştirdik.

#? pop()
drivers.pop(4) #burda da DUTDUR DURUT" ifadesini index'i ile sildik.
print(drivers)

#? remove
#buraya veya gelmeli
#drivers.remove("DUTDUT DURUT") #burada da içeriğini girdik, ilk denk geldiğini siler.
print(drivers)

#? her bir driverı yazdırma
for driver in drivers:
    print(driver)

#region examples

#todo Bir Formula 1 yarışındaki anlık sıralama. Sıralama sürekli değişir, eleman eklenir ve çıkarılır.
# Yarışın 10. turunda "Norris" kaza yapıp elendi (Listeden sil).
# "Russell" arkadan gelip listeye son sıradan dahil oldu (Listeye ekle).
# "Sainz" ile "Hamilton" yer değiştirdi (İndeks manipülasyonu yap).

# yaris_siralamasi = ["Verstappen", "Norris", "Leclerc", "Hamilton", "Sainz"]

# # 10. Tur gerçekleşti
# yaris_siralamasi.remove("Norris") # Norris elendi
# yaris_siralamasi.append("Russell") # Russell sona eklendi

# # Hamilton (3. index) ve Sainz (4. index) yer değiştiriyor
# yaris_siralamasi[3], yaris_siralamasi[4] = yaris_siralamasi[4], yaris_siralamasi[3]

# print(f"Yarış Sonu Sıralaması: {yaris_siralamasi}")

#todo Girilen data sheetten ilkisim.soyisim@outlook.com şeklinde mail_adresses üretilip ekrana yazdırılan uygulama.
#* İpucu1: split() fonksiyonu
#* İpucu2: bir listenin uzunluğu ne olursa olsun son elemanına nasıl ulaşırım
users = ["Burak Yılmaz", "Adal Su Uygur", "Yasemin Uygur Erdem", "Sami Lütfü Esen Berk"]
domain_name = "@outlook.com"

#path i - list comprehension
# for names in users:
#     #print(names) #test
#     divided_names = names.lower().split(" ")
#     print(divided_names) #test
#     mail_adresses = [f"{divided_names[0]}.{divided_names[-1]}{domain_name}" for item in divided_names]
#     print(mail_adresses) #test

#path ii - for loop
# mail_addresses = []
# mail_uzantisi = "@outlook.com"
# for user in users:
#     name_slices = user.split(" ")
#     ilkisim = name_slices[0]
#     soyisim = name_slices[-1]
#     mail_addresses.append(f"{ilkisim}.{soyisim}{mail_uzantisi}")
# print(mail_addresses)

#todo 10ar tane rastgele sayı üretilip 2 listeye eklenecek. 3. listeye aktarılacak. append kullanılması yasak, index mantığıyla çalışılacak.
lst_1 = []
lst_2 = []
lst_3 = []
from random import randint

#region kendi çözümüm
# for i in range(10):
#     sayi_1 = randint(a=0,b=100)
#     lst_1.insert(i, sayi_1)
#     sayi_2 = randint(a=0,b=100)
#     lst_2.insert(i, sayi_2)
#     lst_3.insert(i, lst_1[i] + lst_2[i])
# print(lst_1)
# print(lst_2)
# print(lst_3)
#endregion

#region hocanın çözümü
# for i in range(10):
# #    print(randint(a=0,b=100)) #1. adım, ürettik evet 10 tane
#     lst_1.insert(i, randint(a=0,b=100)) #2. adım ooh hemen üretilen kodla lst_1'e ekleyek
#     lst_2.insert(i, randint(a=0, b=100)) #4. adım, bak bunu da ürettik hatta test edelim yine.
#     lst_3.insert(i, lst_1[i]+lst_2[i]) #6. adım, oh misler gibi çalıştı bak, bir deyazdıralım da görelim
# #print(lst_1) #3. test adımı, ee düzgün çalışıyor demekki o zaman lst_2'ye de aynı şekilde ekleyek
# #print(lst_2) #5. adım, çözdük, o zaman devamke
# print(f"{lst_1}\n{lst_2}\n{lst_3}")
#endregion

#endregion
