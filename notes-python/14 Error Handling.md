
# ERROR HANDLING

Amacımız kodumuzun "kaza yapmasını" engellemek, kaza yapsa bile "hava yastıklarını" açmak.
Error gelirse ne olur?
> **CRASH!**

Elimizde olmayan bir durumdan dolayı ya da;\
X firmanın yazdığı API'ye request atılan durumlarda;\
Bağlandığın veritabanında bağlantın kesildiyse vs. gibi olası hatalara karşı bu yapı kullanılır.

Error Handling, programın ölmesini engelleyip "Bir sorun oldu ama ben ayaktayım, devam ediyorum" demesini sağlayan sanattır.

Yazılımda kullanıcıyı gerizekalı olarak düşün, kullanıcı her zaman hata yapar. Sayı yerine harf girer, saçma sapan şeyler yapar. Veya kullanıcıdan bağımsız olarak internet kesilir, dosya silinir olur vs ve bunların hepsi programın çalışmasını sekteye uğratır.

Error handling ile bu hataları **öngörmerüp ve yakalayabiliriz.**

Bu yapıyı kullanırken end-user'ın yaptığı tüm hataları düşünmemelisin, çünkü end-user'ın yaptığı hatalar front-end yapısında farklı dillerle halledilir. Burada eğer kontrol etmeye kalkarsak server'a gidip gelinebilir, bu da cost-back sebebiyeti verir. Yani maliyeti artırır.

* `try`: Şüphelendiğiniz, yani hata oluşturma potansiyeli olan kod bloğunu içerir. Program bu kod bloğunu dener.
* `except`: `try` bloğu içinde bir hata (istisna) meydana gelirse, programın normal akışı durur ve kontrol hemen `except` bloğuna geçer. Bu blok, hatayı yakalar ve kullanıcıya yönelik bilgilendirici bir mesaj verme veya sorunu çözmeye çalışma gibi işlemleri gerçekleştirir.
* `finally`: İsteğe bağlıdır. `try` bloğu hata oluştursa da oluşturmasa da mutlaka çalıştırılması gereken kodları (örneğin, bir dosyayı kapatma, veritabanı bağlantısını sonlandırma) içerir.

## Syntax Yapısı

Python'da hata yönetimi 4 bloktan oluşur. Bu akışı zihnine kazı:

1. **`try` (Dene):** "Hata çıkma ihtimali olan tehlikeli kodları buraya yaz." (Mayın tarlası).
2. **`except` (Yakala):** "Eğer `try` bloğunda hata çıkarsa, programı patlatma, burayı çalıştır." (Ambulans).
3. **`else` (Sorun Yoksa):** "Eğer `try` bloğu tertemiz çalıştıysa, hata çıkmadıysa burayı çalıştır." (Ödül).
4. **`finally` (Her Türlü):** "Hata olsa da olmasa da, en sonda mutlaka burası çalışsın." (Temizlikçi).

### Seviye 1: Temel Koruma (`try-except`)

```py
try:
    sayi1 = 10
    sayi2 = 0
    sonuc = sayi1 / sayi2  # BURASI PATLAR! (ZeroDivisionError)
    print(sonuc)
except:
    print("Hoppala! Bir sayıyı 0'a bölemezsin dostum.")

print("Program buradan çalışmaya devam eder...")
```

* **Sonuç:** Program çökmez! Ekrana "Hoppala!..." yazar ve alt satırdan devam eder.

### Hatayı Tanımak (Spesifik Yakalama)

"İnternet yok" hatası ile "Yanlış şifre" hatası farklıdır.
Python'da hataların türleri vardır.

| Hata Türü | Ne Zaman Çıkar? | Örnek |
| --- | --- | --- |
| **`ZeroDivisionError`** | Sayıyı 0'a bölersen. | `10 / 0` |
| **`IndexError`** | Listede olmayan sırayı istersen. | `liste[99]` |
| **`KeyError`** | Sözlükte olmayan anahtarı istersen. | `dict["olmayan"]` |
| **`TypeError`** | Elma ile Armudu toplarsan. | `"yazi" + 5` |
| **`ValueError`** | Tipi doğru ama içeriği yanlışsa. | `int("Ali")` |

```py
try:
    sayi = int(input("Bir sayı gir: ")) # Kullanıcı "Ali" girerse ValueError
    sonuc = 10 / sayi                   # Kullanıcı 0 girerse ZeroDivisionError

except ValueError:
    print("Sana sayı gir dedim, yazı girdin!")

except ZeroDivisionError:
    print("Matematik kurallarını çiğnedin! 0'a bölünmez.")

except Exception as e:
    # Öngöremediğimiz başka bir hata olursa bunu genel olarak yakalar
    print(f"Beklenmedik bir hata oldu: {e}")
#Burdaki tüm hatalara bak demek. 
#Bu da maliyeti iyice katlar. Bu sebeple çok nadir kullanılır.

# Her şeyi öngöremiyoruz ee neden her yere try-except yazmıyoruz. Çünkü try-except maliyetli bir işlemdir. Bu yüzden arada bir yazıyoruz. Programın memory ve işlemciden yediği miktar maliyetini belirler.
```

### Full Paket (`else` ve `finally`) 📦

Veri tabanı bağlantılarında veya dosya işlemlerinde bu yapı hayat kurtarır.

```py
try:
    # 1. Riskli işlem
    veri = int(input("Yaşınızı girin: "))
    oran = 100 / veri

except ValueError:
    # 2. Hata varsa burası
    print("Lütfen sadece sayı girin.")

except ZeroDivisionError:
    # 2. Hata varsa burası
    print("Yaş 0 olamaz.")

else:
    # 3. HİÇ HATA YOKSA burası çalışır
    print(f"İşlem başarılı! Oran: {oran}")
    # Veritabanına kaydetme işini genelde buraya koyarız.

finally:
    # 4. Ne olursa olsun çalışır
    print("--- İşlem Bitti (Veritabanı bağlantısı kapatıldı) ---")
```

### Birden fazla hata gelebileceği durumlarda

```py
# SYNTAX YAPISI
try:
    bolunen = int(input("Bölünen sayı: "))
    bolen = int(input("Bölen sayı: "))
except (ZeroDivisionError, ValueError, TypeError) as err: #Parantez içine aldık
    print(err)
```

## **Senior Developer Uyarısı**

Asla ama asla şöyle kod yazma:

```py
# ❌ KÖTÜ KOD
try:
    # kodlar...
except:
    pass  # Hatayı yut ve hiçbir şey yapma
```

Buna **"Silent Fail" (Sessiz Hata)** denir. Programın çalışıyor sanırsın ama arkada veriler yanıyordur. Hatayı mutlaka ya logla ya da ekrana yazdır.

## Exception Raise

Bazı durumlarda, developer bile/isteye exception raise eder, neden? Çünkü nereden hata geldiğini bulunmasına yardımcı olur.

```py
# Örneğin:
#Database'den gelen data'da bir tanesinin mail adresinde "@" yok, eklenmemiş.
try: 
    mail_adress = input("Type mail adress: ") 
    #Normalde bu son kullanıcıdan gelmez, gelen datadan olur.
    if '@' not in mail_adress:
        raise TypeError('Mail adress have to containg "@"')
except TypeError as err:
    print(err)
    #Genelde log tutuluyor
    #Müşteri bilgilendirici feedback/mail gider
    #Notification sistemleri de çalışabilir
    #Kendimize mail atarız
    #Bazı sistemlerde ticket açılır ve görevlendirme yapılır vs vs.
```

Uygulamada hangi tuşlara basıldı, en son ne yapıldı gibi kayıtların tutulmasına log denir.
