
#! LOOPS: 
#* Tekrarlı işleri yaparken tercih edilen yazılım konsepti.

#? FOR DÖNGÜSÜ
#* bir koleksiyonun elemanları üzerinde veya belirli bir sayı aralığı üzerinde sırayla ilerlemek (iterate etmek) için kullanılan döngüdür.

# SYNTAX YAPISI
isim = "Python"
# "isim" (string) içindeki her bir harf için döngüyü çalıştır
for harf in isim: #burada harf olarak adlandırılan şey, takma/geçici isim.
    print(harf)

#todo Girilen başlangıç bitiş ve artış miktarlarına göre for döngüsü kurulumu
start = int(input("Başlangıç: "))
finish = int(input("Bitiş: "))
step = int(input("Artış miktarı: "))
for i in range(start, finish, step):
    print(i,end=" ")

#todo 0-100 arası sayıların ekrana yazdırılması uygulaması
for i in range(0,100):
    print(i, end="-")

#region FOR LOOP

#todo Bozma Testi
# Bir listenin üzerinden geçerken, o listeden eleman silmeye çalışırsak ne olur?

# sayilar = [1, 2, 3, 4, 5] #Liste tanımlandı

# for sayi in sayilar: #listedeki her bir elemanı geçerken
#     if sayi == 2: #eğer eleman 2 ise 
#         sayilar.remove(sayi) # Listeyi dönerken değiştirdik!
#     print(sayi) # ve sayıyı yazdırdık

# print("Sonuç:", sayilar) #döngüden çıktıktan sonra ise listenin tamamını yazdırdık

#çıktılar sırasıyla:
# 1
# 2 Burda 2 var ama 3 yok
# 4
# 5
# Sonuç: [1, 3, 4, 5] burda ise 3 var ama 2 yok NEDEN???

# Çünküüü
# 1. adımda, Python 0. indekste `1`'i buldu, bastı.
# 2. adımda, 1. indekste `2`'yi buldu, sildi.
# 3. adımda, Silince, arkadaki `3` sayısı kayarak `2`'nin (yani 1. indeksin) yerine geçti.
# 4. adımda, Döngü "Sıra 2. indekste" dedi ve devam etti. Ama `3` artık 1. indekste olduğu için onu **ATLADI**.

#* Bu koddan çıkartmamız gereken: Asla üzerinde iterasyon yaptığın listeyi (for döngüsü içindeyken) değiştirme! 
#* Bunun yerine listenin bir kopyasını al veya yeni bir liste oluştur.

#todo Girilen sampledaki sesli harfleri, sessiz harfleri, typoları ayrı listelere ekleyen uygulama. İlgili listelerde eleman tekrarı olmamalı. Space ignore.
sample = "buRa1k _Ayi?Lm2aZu"
# for char in sample.lower():
#     if char.isalpha():
#         if char in "aeıioöuü":
#             if char not in sesli_harfler:
#                 sesli_harfler.append(char)
#         else:
#             if char not in sessiz_harfler:
#                 sessiz_harfler.append(char)
#     else:
#         if char == " ":
#             continue #ignore attık
#         elif char not in typo_char:
#             typo_char.append(char)

# print(f"{sessiz_harfler}\n{sesli_harfler}\n{typo_char}")

#todo bu sayı aralığındaki tek sayıların ve çift sayıların toplamını yazdıran uygulama
# toplam_cift = 0
# toplam_tek = 0
# for i in range(0,100):
#     if i % 2 == 0:
#         toplam_cift += i
#     else:
#         toplam_tek += i
# print(f"Çiftlerin toplamı: {toplam_cift}\n"
#       f"Teklerin toplamı: {toplam_tek}")

#todo Girilen şifrenin min 8 karakter uzunluğunda ve boşluksuz olduğunu doğrulayan uygulama
# password = input("Please enter your password: ")
# is_valid = True
# for char in password:
#     if char == " ":
#         is_valid = False
#         msg = "gap is not accepted in passwords"
#     elif len(password) < 8:
#         is_valid = False
#         msg = "length is too short"

# if is_valid:
#     print("Your password is valid!")
# else:
#     print(msg)

#endregion

#region BOTH LOOPS

#todo 10 tane random sayı üreten uygulama
from random import randint #random sınıfından randint fonksiyonunu çağırdık.

# for i in range(1,11): #range fonksiyonunda son sayı dahil olmadığı için +1 ekledik
#     random_number = randint(a = 0, b = 100)
#     print(f'{i}. üretilen sayı = {random_number}')

#* YA DA 

# i = 0
# while i < 10:
#     random_number = randint(a=213, b=32425)
#     i += 1
#     print(f'{i}. üretilen sayı = {random_number}')

#todo Girilen sayıya kadar toplamı veren uygulama
# hedef_sayi = int(input("Kaça kadar olan sayılar toplansın: "))

# i = 0
# toplam = 0
# while i <= hedef_sayi:
#     toplam = toplam + i
#     print(f'{i}. adımdaki toplam = {toplam}')
#     i = i + 1
# print(f'istenen toplam = {toplam}')

#* YA DA

# bitis = int(input("Kaça kadar gitsin? "))
# sayi = range(1, bitis)
# toplam = 0
# for i in sayi:
#     toplam = i + toplam
#     print(f'her adımdaki toplam: {toplam}')
# print(f'sonuçtaki toplam: {toplam}')

#todo Girilen sayının faktöriyelini hesaplayan uygulama
n = int(input("Faktöriyeli hesaplanacak sayı: "))
faktoriyel = 1
i = 1

# if n > 0:
#     while i <= n:
#         faktoriyel = faktoriyel * i
#         print(f'{i}. adımdaki toplam = {faktoriyel}')
#         i = i + 1
# elif n == 0:
#     faktoriyel = 1
# else:
#     print("Faktöriyel hesabı yapılamaz.")
#     exit()
# print(f'istenen faktöriyel = {faktoriyel}')

#* YA DA

# for i in range(1, n + 1):
#     faktoriyel = faktoriyel * i
#     print(f'{i}. adımdaki toplam = {faktoriyel}')
# print(f'istenen faktöriyel = {faktoriyel}')

#endregion
