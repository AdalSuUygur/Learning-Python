
#! Control Flow Statements / Karar Mekanizmaları (If-Else, Match-Case)
#* Belirli bir koşulun sağlanıp sağlanmamasına göre farklı kod bloklarının çalıştırılmasının standart yoludur.

#region If - Elif - Else
#? If - Elif - Else SYNTAX
#* if - elif - else bloğunda herhangi bir şart tutarsa diğer şartlara bakılmaz.
#* Mantıksal operatörler (and, or, not) kullanarak birden fazla karmaşık koşulu aynı anda kontrol etmeye olanak tanır.
kosul_1 = ""
kosul_2 = ""
if kosul_1:
    # Koşul_1 doğru ise bu blok çalışır
    print("Koşul 1 Doğru")
elif kosul_2:
    # Koşul_1 yanlış VE Koşul_2 doğru ise bu blok çalışır
    print("Koşul 2 Doğru")
else:
    # Yukarıdaki koşulların hiçbiri doğru değilse bu blok çalışır
    print("Hiçbiri Doğru Değil")

#todo Kullanıcıdan alınan 2 tane tam sayının büyük olanının hesabı
number_1 = int(input("Birinci sayı: "))
number_2 = int(input("İkinci sayı: "))

if number_1 > number_2 :
    print(f'{number_1} daha büyüktür {number_2}')
elif number_1 == number_2: 
    print("Her ikisi birbirlerine eşittir.")
else:
    print(f'{number_2} daha büyüktür {number_1}')

#todo Girilen sayının tek mi çift mi
#* Kendi çözümüm ^^ (Mod ifadesini bilmiyordum, bu şekilde çözdüm. BU KOD BLOĞU sana workaround'un her zaman olduğunu göstersin!)
#* GO GIRLLLLL!!!!!
number = float(input("Sayıyı giriniz: "))
sonuc = number / 2
if sonuc.is_integer() == True:
    print("Sayı çifttir")
else:
    print("Sayı tektir.")

#Mod ifadesi ile kolay çözümü :)
sayi = int(input('Bir sayi giriniz :'))
if sayi %2 == 0:
    print(f'{sayi} çift')
else:
    print(f'{sayi} tek')
#endregion

#region Ternary If (Tek satır if)
#? Ternary If (Tek satır if) SYNTAX
#* Tek satırda if-else gibi düşün. Tek mi çift mi gibi tek şart olan durumlarda kullanılır.

#değişken = [True ise atanacak değer] if [koşul] else [False ise atanacak değer]
sayi = 0
sonuc = "Pozitif" if sayi > 0 else "Pozitif Değil (Sıfır veya Negatif)"

#todo Yaşını giren kullanıcının reşit olup olmaması durumunu kontrol eden ternary if
age = int(input("Your age: "))
status = "adult" if age >= 18 else "child"
print(status)

#todo Girilen sayının negatif mi pozitif mi olduğunu kontrol eden ternary if
number = int(input("Number: "))
print(f"Status {'positive' if number > 0 else 'negative'}") #f-string fonksiyonu içinde yazdık.

#todo Girilen sayının negatif mi pozitif mi olduğunu kontrol eden If-Elif-Else bloğu
number = int(input("Sayıyı giriniz: "))
if number > 0:
    print(f'Sayınız pozitiftir.')
elif number == 0:
    print("Sayınız nötrdür.")
else: 
    print("Sayınız negatiftir.")

#endregion

#region Match-case yapısı:
#? Match-case yapısı:
#* if else'e alternatif olarak gelen bir yapı. (C ailesindeki switch-case) match-case status kontrolü için sıklıkla tercih edilir ancak case'de and/or kullanmak daha zor.
#* Genel olarak birebir uyum (==) sağlandığında case ifadesi daha tercih edilir.

#todo Subscription yapılan üyeliklerdeki statusu beliren uygulama
boxing_gloves_status = "passive"
match boxing_gloves_status:
    case "passive":
        pass
    case "active":
        pass
    case "modified":
        pass
    case _:
        print("None")

#todo Match case'te and ifadesinin kullanımı (ÇOK ZOR SAÇMA SAPAN SYNTAX)
kitap = 5
adet_kitap = int(input('Satın Alınan Kitap Sayısı: '))
if adet_kitap <= 0:
    print('Eksi kitap sayısı olamaz.')
else:
    match adet_kitap:
        case n if 1 <= adet_kitap <= 5: #if ile iç içe kullanıyoruz :)
            print(f'Ödenecek Tutar: {kitap * adet_kitap * 0.95}')
        case n if 5 <= adet_kitap <= 10:
            print(f'Ödenecek Tutar: {kitap * adet_kitap * 0.90}')
        case n if 10 <= adet_kitap <= 15:
            print(f'Ödenecek Tutar: {kitap * adet_kitap * 0.85}')
        case n if 15 <= adet_kitap <= 20:
            print(f'Ödenecek Tutar: {kitap * adet_kitap * 0.80}')
        case _:
            print('En fazla 20 kitap satın alabilirsiniz.')
#endregion

#region examples
#region IF-ELIF-ELSE KULLANIMI

#todo Kenar uzunlukları girilen üçgenin eşkenar, ikizkenar, çeşitkenar olduğunu yazdıran uygulama
# kenar_1 = int(input("Kenar 1: "))
# kenar_2 = int(input("Kenar 2: "))
# kenar_3 = int(input("Kenar 3: "))
# if kenar_1 == kenar_2 and kenar_1 == kenar_3:
#     print("eşkenar")
# elif kenar_1 != kenar_2 and kenar_1 != kenar_3 and kenar_2 != kenar_3:
#     print("çeşitkenar")
# else:
#     print("ikizkenar")

#todo Karakterin sesli harf mi sessiz harf mi olduğunu bulan uygulama
# karakter = input("Karakter: ")
# if karakter.isalpha():
#     if karakter in "aeıioöuü":
#         print("sesli harf")
#     else:
#         print("sessiz harf")
# else:
#     print("girilen karakter alfabetik değil.")

#todo Girilen sayının +, 0, - olduğunu yazdıran uygulama
# sayi = int(input("Sayıyı giriniz: "))
# sayi_durumu = ""
# if sayi < 0:
#     sayi_durumu = "Negatif"
# elif sayi == 0:
#     sayi_durumu = "Nötr"
# elif sayi > 0:
#     sayi_durumu = "Pozitif"
# else:
#     print("İlginç bir deneme.")
#     exit()
# print(f'Girilen sayı {sayi}, {sayi_durumu} bir değerdedir.')

#todo Girilen sayılardan büyük olanın ekrana yazdırılması
# n1 = int(input("First number: "))
# n2 = int(input("Second number: "))

# if n1 > n2:
#     gross_n = n1
# elif n2 > n1:
#     gross_n = n2
# else:
#     print("Sayılar birbirlerine eşit.")
#     exit()
# print(f'Greater number between given numbers is {gross_n}')

#todo elif ve else ile Tam Karar Zinciri
# sepet_tutari = float(input("Total sepet miktarı: "))
# if (sepet_tutari >= 1000):
#     indirim = 0.2
# elif (sepet_tutari >= 500):
#     indirim = 0.1
# elif (sepet_tutari >= 250):
#     indirim = 0.05
# else:
#     indirim = 0
# odenecek_toplam = sepet_tutari - (sepet_tutari * indirim)
# print(f'Total ödenmesi gereken miktar {odenecek_toplam} kadardır')

#todo Kullanıcı etkinliğe katılma şartlarını yerine getiriyor mu? (Nested if örneği)
#* Şartlar: Kullanıcının yaşı 18 ve üzeri olmalı VE Giriş kodu doğru olmalı (1234)
# yas = int(input("Yaşınızı giriniz: "))
# sifre = int(input("Şifreyi giriniz: "))

# if (yas >= 18): #Eğer yaşı 18e eşit veya büyükse
#     if (sifre == 1234): #şifre sorduk ve 1234'e eşit mi diye kontrol ettik
#         print("İçeri girebilirsiniz.") #eşitse de giriş sağlam.
#     else: #şifre 1234 değilse
#         print("Şifre yanlış.") #şifre yanlış dedik
# else: #Eğer yaşı 18den küçükse (yani diğer tüm şartlar)
#     print("Yaşınız tutmuyor.") #yaşı tutmuyor dedik.

#* YA DA

# if (yas >= 18 and sifre == 1234): #Tek satırda da bu kod bloğunu çözebiliriz. 
#     #* ÖNEMLİ: "and" operatörü ile mantıksal ifade kurduk.
#     print("İçeri girebilirsiniz.")
# else:
#     print("İçeri giremezsiniz.")

#todo If-Elif-Else ve f-string kullanarak basit bir not ortalama hesaplayıcı yapmak.
#* Kullanıcıdan 3 farklı sınav notu (vize1, vize2, final) alınır ve float'a dönüştürülür.
# vize1 = float(input("İlk vize notu: "))
# vize2 = float(input("İkinci vize notu: "))
# final = float(input("Final notu: "))

# ortalama = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4) #Ortalama hesaplanır. Matematikteki öncelikler göz ardı edilmez.
# if(ortalama > 90): # Eğer ortalama 90 ve üstüyse:
#     print(f"Ortalamanız {ortalama:.2f} kadar ve AA ile geçersiniz.") #"AA - Başarılı"
# elif(ortalama > 70): # İlk if seçeneğini eledik, yani ortalama >90 değilse bu adıma geldik ve soruyoruz, ortalama 70'ten büyük mü?
#     print(f"Ortalamanız {ortalama:.2f} kadar ve BB ile geçersiniz.")  #"BB - İyi"
# elif (ortalama > 50): #diğer iki seçeneği eledik, yani ortalama 90dan ve 70'ten küçük. Bu koşulda 50'den büyük mü?
#     print(f"Ortalamanız {ortalama:.2f} kadar ve CC ile geçersiniz.") #Eğer öyleyse "CC - Geçer"
# else: #aksi taktirde...
#     print(f"Ortalamanız {ortalama:.2f} kadar ve FF ile kalırsınız.") #FF - Kaldı

#todo Girilen login bilgilerinin doğruluğuna göre girişin yazdırılması
# username = input("Username: ").lower() #aldığımız username'i küçük harflere çevirdik.
# password = input("Password: ") #her ikisinin string ifade olması gerek ki mukayese edilebilsin.

# if username == "beast" and password == "123": #tek satır, genelde kullanılan (hacklenme ihtimalini azaltır)
#     print("Correctly entered.")
# else:
#     print("Wrong entry.")
#* YA DA
# if username == "beast":
#     if password == "123":
#         print("Correctly entered.")
#     else:
#         print("Wrong password.")
# else:
#     print("Wrong username.")
#* Bu uygulamada hangi değeri yanlış girdiğini belirttik, hacklenme oranımızı %50 artırdık.

#todo Girilen ürünün adı: domates, biber, patlıcan ise sebze; notebook, kindle, tablet ise teknoloji; şampuan, sabun, parfüm ise kozmetik reyonu çıktısı veren uygulama
# urun_adi = input("Ürünün ismi: ").lower() #lower metodu ile gelen inputu küçük harflere çevirdik ki if bloğu içinde sıkıntı yaşamayalım
# reyon_adi = "reyon" #best practice, DONT REPEAT YOURSELF için hep :) ağaç yaşken eğilir ^^

# if urun_adi == "domates" or urun_adi == "biber" or urun_adi == "patlıcan":
#     reyon_adi = "Sebze"
# elif urun_adi == "notebook" or urun_adi == "kindle" or urun_adi == "tablet":
#     reyon_adi = "Teknoloji"
# elif urun_adi == "şampuan" or urun_adi == "parfüm" or urun_adi == "sabun":
#     reyon_adi = "Kozmetik"
# else:
#     print("Aradığınız ürün bulunmamaktadır.")
#     exit()
# print(f'Satın alınan ürün için {reyon_adi} Reyonuna gidiniz.')

#todo Alınan kitap sayısına göre indirimi yazdıran uygulama
# #* Bir kitap 5 TL
# kitap_fiyat = 5
# #* Kullanıcıdan satın aldığı kitap sayısını alalım
# kitap_sayisi = int(input("Satın alınan kitap sayısı: "))
# # Alınan kitap sayısı 1 ile 5 arasında ise yüzde 5 iskonto
# if 0 < kitap_sayisi <= 5:
#     indirim = 0.05
# # Alınan kitap sayısı 6 ile 10 arasında ise yüzde 10 iskonto
# elif 5 < kitap_sayisi <= 10:
#     indirim = 0.10
# # Alınan kitap sayısı 11 ile 15 arasında ise yüzde 15 iskonto
# elif 10 < kitap_sayisi <= 15:
#     indirim = 0.15
# # Alınan kitap sayısı 16 ile 20 arasında ise yüzde 20 iskonto
# elif 15 < kitap_sayisi <= 20:
#     indirim = 0.20
# # Alınan kitap sayısı 20'yi aşarsa hata verir.
# elif kitap_sayisi > 20:
#     print("Maximum kitap sayısını aştınız.")
#     exit()
# else:
#     print('Hesaplanamaz bir değer girildi.')
#     exit()

# odenecek_tutar = kitap_fiyat * kitap_sayisi #math beybi
# indirimli_odenecek = odenecek_tutar * (1 - indirim)

# print(f'Kitap fiyatı: {kitap_fiyat} TL\n'
#     f'İndirimsiz ödenilecek tutar: {odenecek_tutar} TL\n'
#     f'İndirim yüzdesi: %{indirim * 100}\n'
#     f'İndirim miktarı: {kitap_fiyat * kitap_sayisi * indirim} TL\n'
#     f'İndirim sonrası ödenecek tutar: {indirimli_odenecek} TL')

#todo Doğru login ile BMI hesaplayan uygulama
# username = input("Username: ").lower()
# password = input("Password: ")
# if username == "beast" and password == "123":
#     print(f'{username}, welcome!') #Bak girişi yaptık, ondan sonra devam ediyoruz koda, giriş yapamazsa bu bloğa ulaşamaz.
#     weight = float(input("Your weight in kgs: "))
#     height = float(input("Your height in cms: "))
#     BMI = weight / (height ** 2) # ** ifadesi C ailesindeki ^ anlamına geliyor, yani üssü.
#     status = ""
#     if 0 < BMI <= 18.5: # 0 < BMI and BMI <= 18.5 yerine geçer aslında, and kullanmadık ortaya aldık değeri
#         status = "Lean"
#     elif 18.5 < BMI <= 24.9:
#         status = "Normal"
#     elif 25 < BMI <= 29.9:
#         status = "Weighted"
#     elif 30 < BMI <= 34.9:
#         status = "First degree obesity"
#     elif 35 < BMI <= 39.9:
#         status = "Second degree obesity"
#     elif BMI > 40:
#         status = "Morbid obesity" 
#     else:
#         print("Wrong entry.")
#         exit()
#     #Neden exit verdim? IF BLOĞUNA DÜZGÜN GİRDİĞİ HER SENARYODA bir sonraki satırdaki PRINT fonksiyonunu YAZ DI RA CAK.
#     #Amaaaaa bu blokta value değerine bir şey atamıyorum ve değer bommmmmboş
#     #DRY prensibini uygulayabilmek için value değerine atadık ancak düzgün çalışması adına burdan çıktık.
#     print(f'User name: {username}\n' #!Sonraki satıra geçmek için \n
#             f'BMI: {BMI}\n'
#             f'Status: {status}')
# else:
#     print("Invalid credantials.")

#endregion

#region MATCH-CASE KULLANIMI

#todo Girilen günün weekday/weekend olduğunu bulan uygulama
# gun = input("Gün: ").lower()
# if gun in ("pazartesi", "salı", "çarşamba", "perşembe", "cuma", "cumartesi", "pazar"):
#     match gun:
#         case "pazartesi" | "salı" | "çarşamba" | "perşembe" | "cuma":
#             print("weekday")
#         case "cumartesi" | "pazar":
#             print("weekend")
# else:
#     print("girdiyi kontrol et")

#todo Girilen trafik lambası rengine göre uygun mesaj yazdıran uygulama
# light_color = input("Light color: ")
# if light_color in ("red", "green", "yellow"):
#     match light_color:
#         case "red":
#             print("stop")
#         case "yellow":
#             print("ready")
#         case "green":
#             print("pass")
# else:
#     print("wrong entry")

#todo Girilen ayın çıktısını yazdıran uygulama
# try:
#     month = int(input("Month index: "))
#     if month in (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12):
#         match month:
#             case 1:
#                 pass
#             case 2: 
#                 pass
#             case 3: 
#                 pass
#             case 4: 
#                 pass
#             case 5: 
#                 pass
#             case 6: 
#                 pass
#             case 7:
#                 pass
#             case 8:
#                 pass
#             case 9:
#                 pass
#             case 10: 
#                 pass
#             case 11: 
#                 pass
#             case 12:
#                 pass
#     else:
#         print("no such month")
# except (ValueError, TypeError) as err:
#     print(f"because of {err} you have to enter again.")

#endregion

#region TERNARY IF KULLANIMI

#todo Sınav sonucuna göre harf notunu yazdıran nested+ternary if yapısı
# exam_score = 85
# result = "AA" if exam_score >= 80 else "BB" if exam_score >= 60 else "CC"
# print(result)

#todo Ternary if tek/çift sayı kontrolü
# sayi = int(input("Sayıyı giriniz: "))
# print("Çift") if sayi % 2 == 0 else print("Tek")

#todo Ternary if erişkinlik durumu
# yas = int(input("Yaşınız: "))
# print("Reşit") if yas > 18 else print("Reşit değil")

#endregion

#region IF MATCH KARŞILAŞTIRMA

#todo Girilen mevsimin aylarını yazdıran uygulama.
# season = input("Season: ").lower()
#? Match Case kullanarak:
# match season:
    # case 'winter':
    #     print(f'{season} season includes: December, January, February months.')
    # case "spring":
    #     print(f'{season} season includes: March, April, May months.')
    # case "summer":
    #     print(f'{season} season includes: June, July, August months.')
    # case "autumn" | "fall" : # '|' şu ifade or anlamına geliyor.
    #     print(f'{season} season includes: September, October, November months.')
    # case _: #else ifadesi aslında
    #     print("There is no such a thing love.")
#? If-Elif-Else kullarak:
# if season == "winter":
#     print(f'{season} season includes: December, January, February months.')
# elif season == "spring":
#     print(f'{season} season includes: March, April, May months.')
# elif season == "summer":
#     print(f'{season} season includes: June, July, August months.')
# elif season == "autumn" or season == "fall":
#     print(f'{season} season includes: September, October, November months.')
# else:
#     print("There is no such a thing love.")

#todo Girilen ay ve günün hangi mevsime ait olduğunu yazdıran uygulama
# ay = input("Ayı giriniz: ").lower()

# while True:
#     #bunu 1-31 arasıda nasıl tutabilirim?
#     #gelecekten gelen Su, bunu 1-31 aralığına tutacak güncellemeyi yapıyor :')
#     gun = int(input("Ayın hangi günü: "))
#     if 1 <= gun <= 31: #aha tuttuk.
#         break
#     else:
#         print("Gün negatif veya 31'den büyük değerde olamaz. Girdinizi kontrol ediniz.")
#? IF_ELSE ve MATCH_CASE birleştirerek kullandık :)
# match ay:
#     case "ocak" | "şubat":
#         mevsim = "kış"
#     case "nisan" | "mayıs":
#         mevsim = "ilkbahar"
#     case "temmuz" | "ağustus":
#         mevsim = "yaz"
#     case "ekim" | "kasım":
#         mevsim = "sonbahar"
#     case "mart":
#         if gun >= 21:
#             mevsim = "İlkbahar"
#         else:
#             mevsim = "Kış"
#     case "haziran":
#         if gun >= 20:
#             mevsim = "Yaz"
#         else:
#             mevsim = "İlkbahar"
#     case "eylül":
#         if gun >= 22:
#             mevsim = "Sonbahar"
#         else:
#             mevsim = "Yaz"
#     case "aralık":
#         if gun >= 21:
#             mevsim = "Kış"
#         else:
#             mevsim = "Sonbahar"
#     case _: 
#         print("Böyle bir ay/gün bulunmamaktadır.")
#         exit()
# print(f'Şu anda mevsim: {mevsim}')

#endregion

#endregion
