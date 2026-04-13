
#! Exception Handling (Try-Except-Finally)
#* try-except-finally bloğu, programın çalışması sırasında oluşabilecek istisnaları (exceptions) yönetmek için kullanılan bir mekanizmadır.

# SYNTAX YAPISI
try: #Hata beklediğimiz kodları try bloğunun içine alıyoruz.
    bolunen = int(input("Bölünen: "))
    bolen = int(input("Bölen: "))
    sonuc = bolunen / bolen #bölen değerine 0 verirsek hata verir.
    print(sonuc)
except (ZeroDivisionError, ValueError) as err: #except satırına da beklediğimiz hatayı yazıyoruz ve takma isim veriyoruz.
    print("Hatalı giriş.")
    print(f'{err}')
finally: #ne olursa olsun bu bloğa gel ve bunu çalıştır anlamına gelir.
    print("Çalışıyor.") 

#? Her şeyi öngöremiyoruz ee neden her yere try-except yazmıyoruz. 
#? Çünkü try-except maliyetli bir işlemdir. İşlemin memory ve işlemciden yediği miktar maliyetini belirler.
try:
    pass
except Exception as err: #Burdaki tüm hepsine tüm hatalara bak demek. Bu da maliyeti iyice katlar. Çok nadir kullanılır.
    pass

#? Bazı durumlarda bilerek exception raise edilir. Mesela gelen data'da bir tanesinin mail adresinde @ yok, eklenmemiş.
try: 
    mail_adress = input("Type mail adress: ") #Normalde bu son kullanıcıdan gelmez, gelen datadan olur.
    if '@' not in mail_adress:
        raise TypeError('Mail adress have to containg "@"')
except TypeError as err:
    print(err)
    #Genelde log tutuluyor
    #Müşteri bilgilendirici feedback/mail gider
    #Notification sistemleri de çalışabilir
    #Kendimize mail atarız
    #Bazı sistemlerde ticket açılır ve görevlendirme yapılır vs vs.

#region Examples

#todo Login, 3 yanlış hak, try-except & match-case & infinitive loop kullanımı isteniliyor. Login yapıldığında hesap makinesine ulaşılacak.
username = "adal"
password = "123"
#isim ve şifre belirledik
hak = 3
while hak > 0:
#kullanıcıdan da istedik neden döngü içinde, her seferinde sorabilmek için
    user_name = input("Username: ")
    pass_word = input("Password: ")
    if user_name == username and pass_word == password:
        print("Login successful") #login olduk ama hak için bir şey yapmadık. Test lazım.
        while True:
            try:
                n1 = int(input("Number1: "))
                n2 = int(input("Number2: "))
                operation = input("Enter desired matematical operation, e for exit: ")
                match operation:
                    case "+":
                        result = n1 + n2
                        print(f"Your calculation is : {n1} {operation} {n2} = {result}") #DRY prensibine uyamadım.
                    case "-":
                        result = n1 - n2
                        print(f"Your calculation is : {n1} {operation} {n2} = {result}")
                    case "*":
                        result = n1 * n2
                        print(f"Your calculation is : {n1} {operation} {n2} = {result}")
                    case "/":
                        result = n1 / n2
                        print(f"Your calculation is : {n1} {operation} {n2} = {result}")
                    case "e":
                        print("Exiting the program.")
                        break
                    case _:
                        print("Invalid entry, try again.")
            except (ValueError, TypeError, ZeroDivisionError) as err:
                print(f"Cannot continue because of ({err}), try again.")
    else:
        print(f"Login denied!, remaining tries = {hak - 1}")
        hak -= 1 #döngüye sokacağız mecbur, burda da hakkımızı düşürdük.
print("Hakkınızı yitirdiniz, bye!") #While döngüsünden çıktığımızda hakkımız kalmamış olcak.

#todo Girilen sayının asal olup olmadığını kontrol eden uygulama
while True:
    try:
        sayi = int(input("Lütfen bir sayı giriniz: "))
        is_asal = True
        if sayi < 2: #2den küçük asal sayı yoktur ve negatif sayılar asal olamaz.
            print("Negatif sayılarda asallık bakılmaz ve 2'den küçük sayılar asal değildir.")
            break
        else:
            for i in range(2, sayi):
                if sayi % i == 0:
                    is_asal = False
                    break
            if is_asal == True:
                print(f"Girilen sayı ({sayi}) asaldır.")
            else:
                print(f"Girilen sayı ({sayi}) asal değildir.")
    except (ValueError, TypeError) as err:
        print(f"{err} sebebiyle hata verildi, lütfen sayıyı tekrar giriniz.")

#endregion
