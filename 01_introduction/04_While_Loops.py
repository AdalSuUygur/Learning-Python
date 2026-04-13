
#! LOOPS: 
#* Tekrarlı işleri yaparken tercih edilen yazılım konsepti.

#? While Loop
#* Belirli bir koşul True olduğu sürece içerisindeki kod bloğunu çalıştırmaya devam eder. 
#* Ne zaman duracağını, yani sayacı veya koşulu değiştirmeyi programcının kendisi yönetmelidir.

# SYNTAX YAPISI
counter = 0 #Sayaç, çözülen problemin bağlamında başlangıç değeri ile başlar.
while counter <= 9: #Anahtar kelimesi while, ve şart kelimesi.
    print(counter)
    counter = counter + 1 #counter += 1 şeklinde de yazılabilir.
    # Koşulu değiştiren adım yazılmazsa sonsuz döngü olur

#? Sonsuz döngü
#* Bir döngünün durma koşulunun hiçbir zaman sağlanamadığı (yani koşulun sürekli True kaldığı) durumdur. İsteyerek oluşturulur.

# SYNTAX YAPISI
while True:
    print(counter) #Döngüden çıkılmadığı için sonsuza dek counter'ı yazdıracak ne olursa olsun.
    break #Döngüden çıkması için break yazılır.

#todo anket cevapları alınan uygulamada 3 kez hayır girilirse döngünün sonlandığı uygulama
counter = 0
while True:
    cevap = input("Evet/Hayır: ").lower()
    match cevap:
        case "evet":
            counter = 0
        case "hayır":
            counter += 1
            if counter == 3:
                print("Anket katılımı iptal edildi.")
                break
        case _:
            print("Girdiniz evet ya da hayır dışında, lütfen girdinizi kontrol ediniz.")

#region WHILE LOOP

#todo Girilen sayının asal olup olmadığını kontrol eden uygulama
# while True:
#     try:
#         sayi = int(input("Lütfen bir sayı giriniz: "))
#         is_asal = True
#         if sayi < 2: #2den küçük asal sayı yoktur ve negatif sayılar asal olamaz.
#             print("Negatif sayılarda asallık bakılmaz ve 2'den küçük sayılar asal değildir.")
#             break
#         else:
#             for i in range(2, sayi):
#                 if sayi % i == 0:
#                     is_asal = False
#                     break
#             if is_asal == True:
#                 print(f"Girilen sayı ({sayi}) asaldır.")
#             else:
#                 print(f"Girilen sayı ({sayi}) asal değildir.")
#     except (ValueError, TypeError) as err:
#         print(f"{err} sebebiyle hata verildi, lütfen sayıyı tekrar giriniz.")

#todo random bir sayı üretilir, 3 tahmin hakkı, tahmin sonucu ekrana yazdırılır
# from random import randint #* Random sayı üretebilmek için randint fonksiyonunu random kütüphanesinden çağırdık
# deneme = 3
# i = 1

# random_sayi = randint(a=0,b=10)
# while i <= deneme:
#     tahmini_sayi = int(input("Tahmininiz: "))
#     if tahmini_sayi ==  random_sayi:
#         print("Doğru bildiniz")
#         break
#     else:
#         print(f"{i}. hakkınız, yanlış tahmin.")
#     i += 1

# if i > deneme:
#     print(f"Deneme hakkınız bitti.\n"
#           f"Doğru tahmin: {random_sayi} olacaktı.")

#todo 0-100 arasındaki çift ve tek sayıların toplamlarının ekrana yazdırılması
# i = 0
# sum_even = 0
# sum_odd = 0

# while i <= 100:
#     if i %2 == 0:
#         sum_even += i
#     else:
#         sum_odd += i
#     i = i + 1
# print(f'Sum of Even Numbers: {sum_even}\nSum of Odd Count: {sum_odd}')

#todo (0-100) aralığındaki sayıların ekrana yazdırılması
# i = 0 #counter olarak i, C ailesinde genelde o şekilde kullanılıyor, alıştık ^^
# while i <= 100:
#     print(i)
#     i = i + 1 #i += 1 de olur
# print("Döngü sonlandı")

#* YA DA

# i = 100
# while i >= 0:
#     print(i, end="-")
#     i -= 1 # i = i - 1 de olur
# print("Döngü sonlandı")

#endregion

#region SONSUZ LOOP

#todo anket cevapları alınan uygulamada 3 kez hayır girilirse döngünün sonlandığı uygulama
# counter = 0
# while True:
#     cevap = input("Evet/Hayır: ").lower()
#     match cevap:
#         case "evet":
#             counter = 0
#         case "hayır":
#             counter += 1
#             if counter == 3:
#                 print("Anket katılımı iptal edildi.")
#                 break
#         case _:
#             print("Girdiniz evet ya da hayır dışında, lütfen girdinizi kontrol ediniz.")

#endregion
