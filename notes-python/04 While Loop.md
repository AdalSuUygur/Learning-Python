
# WHILE LOOP (Koşul Tabanlı Tekrar)

Kemerleri bağla, çünkü döngülerle "SONSUZLUĞA" gitme ihtimalimiz var. :)

while döngüsü, belirli bir koşul (condition) doğru (True) olduğu sürece içerisindeki kod bloğunu çalıştırmaya devam eder. Yani:

>`While` bloğu şart bozulana kadar **tekrar tekrar** kontrol eder ve yapar.

Ne zaman duracağını, sayacı veya koşulu değiştirmeyi programcının kendisi belirler.

>Türkçesi: **"... olduğu sürece yap."**

Veri biliminde `while` döngüsünü genellikle **"sonunu bilmediğimiz"** durumlarda kullanırız.

* "Modelin hatası %1'in altına düşene kadar eğit."
* "Dosyadaki satırlar bitene kadar oku."
* "Kullanıcı 'çıkış' yazana kadar soru sor."

## SYNTAX

```py
# Başlangıç değeri (Sayaç)
sayaç = 0

while sayaç <= 3:  # Koşul: sayaç 3'ten küçük veya eşit olduğu sürece
    print(sayaç)
    # Koşulu değiştiren adım (Aksi takdirde sonsuz döngü olur)
    sayaç += 1
```

**DİKKAT:** _Koşul hiçbir noktada false değerini almıyorsa program sonsuz döngüye girer._

## Büyük Tehlike: Sonsuz Döngü (Infinite Loop) ♾️

Eğer `while` koşulu asla `False` yapılmazsa, program sonsuza kadar (veya RAM dolana kadar) çalışır.

```py
# SAKIN PROD ORTAMINDA DENEME :)
while True:
    print("Durduramazsın beni!")
```

Sonsuz döngü, bir döngünün durma koşulunun hiçbir zaman sağlanamadığı (yani koşulun sürekli `True` kaldığı) durumdur.

### Kontrol Kuleleri: `break` ve `continue`

Döngü dönerken müdahele edilmesi gereken zamanlarda (örneğin koşulun elle false yapılması gereken zamanlarda) kullanılan operatörler.

#### Break (Çıkış Butonu)

**`break`**: "Yeter, dükkanı kapatıyoruz!" Döngüyü anında öldürür ve çıkar. Koşul ne olursa olsun döngü biter.

* Örnek: Aradığım veriyi buldum, artık listenin geri kalanına bakmama gerek yok.

#### Continue (Pas Geç Butonu)

**`continue`**: "Bunu pas geç, sıradakine bak." Döngüyü kırmaz, sadece o anki turu (iterasyonu) atlar ve başa döner.

* Örnek: Sadece çift sayıları işlemek istiyorum, tek sayı gelirse "pas geç".

```py
sayac = 0
while sayac < 10:
    sayac += 1
    
    if sayac == 3:
        print("3'ü sevmem, atlıyorum.")
        continue # Aşağıdaki print çalışmaz, döngü başa döner.
        
    if sayac == 6:
        print("6 oldu, ben kaçar!")
        break # Döngü tamamen biter.
        
    print(f"Sayı: {sayac}")
```

### While - Else (Python'un Gizli Silahı)

Çoğu dilde (Java, C++) bu yoktur. Python'da döngünün ucuna `else` ekleyebilirsin.

* **Ne zaman çalışır?** Döngü, şartı artık sağlamadığı için **doğal yollarla** biterse çalışır.
* **Ne zaman ÇALIŞMAZ?** Eğer döngü `break` ile zorla durdurulursa `else` bloğu çalışmaz.

**Arama Algoritması Örneği:**

```python
aranan = 5
i = 0

while i < 4:
    if i == aranan:
        print("Bulundu!")
        break # Break ile çıktığı için else çalışmayacak.
    i += 1
else:
    print("Döngü bitti ama aranan sayı bulunamadı.") 
    # Eğer break hiç çalışmazsa burası devreye girer.
```
