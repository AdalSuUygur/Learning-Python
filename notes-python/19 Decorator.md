
# DECORATOR

Decorator var olan bir fonksiyonun kodunu **değiştirmeden**, ona **yeni özellikler** eklememizi sağlayan bir yapıdır.

## Decorator neden kullanılır?

Diyelim ki 50 tane fonksiyonun var (Sepet, Profil, Ödeme vs.). Patron dedi ki:
*"Bu 50 fonksiyona girmeden önce kullanıcının şifresi doğru mu diye kontrol et."*

* **Amele Yöntemi:** 50 fonksiyonu tek tek açıp, hepsinin en başına `if sifre_dogru_mu:` kodunu kopyala-yapıştır yapmak. (Kabus!)
* **Decorator Yöntemi:** Bir tane `@login_kontrol` diye decorator yazarsın. Fonksiyonların tepesine bu etiketi yapıştırırsın. Bitti!

**Gerçek Hayat Kullanımları:**

1. **Login Kontrolü:** (Kullanıcı giriş yapmış mı?)
2. **Loglama:** (Bu fonksiyon saat kaçta çalıştı?)
3. **Performans Testi:** (Bu fonksiyonun çalışması kaç saniye sürdü?)

## Syntax

Decorator'lar aslında **"Fonksiyon alan ve geriye fonksiyon döndüren fonksiyonlardır."** (Biraz tekerleme gibi ama mantığı basit).

Python'da decorator kullanmak için fonksiyonun tepesine **`@decorator_adi`** (Pie Syntax / Syntactic Sugar) koyarız.

Bu yapı "Wrapper Pattern" olarak geçer ve her yerde aynıdır.

```py
# Decorator Şablonu
def decorator_adi(orijinal_fonk):
    
    def wrapper(*args, **kwargs):
        # 1. Fonksiyon çalışmadan ÖNCE yapılacaklar
        print("Fonksiyon başlamadan önceki işlemler...")
        
        # 2. Orijinal fonksiyonu çağır
        sonuc = orijinal_fonk(*args, **kwargs)
        
        # 3. Fonksiyon çalıştıktan SONRA yapılacaklar
        print("Fonksiyon bittikten sonraki işlemler...")
        
        return sonuc
        
    return wrapper

# Kullanımı:
# @decorator_adi
# def islem(): ...

```

## Neden `*args, **kwargs` kullandık?

Wrapper fonksiyonunun içine `(*args, **kwargs)` koyduk.
Çünkü decorator'ı yapıştırdığımız fonksiyonun kaç parametre alacağını bilemeyiz.

* Belki parametresizdir: `gizli_raporu_oku()`
* Belki 3 parametrelidir: `topla(a, b, c)`

`*args` ve `**kwargs` sayesinde decorator'ımız **evrensel** olur, her fonksiyona uyar.
