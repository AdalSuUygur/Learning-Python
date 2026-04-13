
# Liste için Built-in-methods

Listeler, üzerlerinde işlem yapmak için birçok yerleşik metoda sahiptirler.
Bu metotlar, liste adından sonra nokta (.) (Bu duruma nokta notasyonu denir) koyularak çağrılır.

Bir liste tanımlayarak metodlarını öğrenelim, listemiz ünlü boksörleri içerien bir liste olsun.:

```py
boxers = ['Mike Tyson', 'Muhammed Ali', 'Lenox Lewix', "Evander Holyfiled", "George Foreman"]
print(boxers) #burada herhangi bir manipülasyon yapmadık, yani sadece var olan listeyi göreceğiz
```

Şimdi ise, **.append() metodu** ile "Rocky Marciano"u listemize ekleyelim:

```py
# Listenin sonuna ekler
boxers.append("Rocky Marciano") #Listenin sonuna ekler
print(boxers) #burada ise Rocky'i görürüz
```

Sırada, **.insert() metodu** ile kullanıcıdan alınan index değerine yine kullanıcıdan alınan boksör ismini sıkıştıralım.

```py
boxer_name = input("Name: ")
index_value = int(input("Index: "))
boxers.insert(index_value, boxer_name) #Insert metodu
print(boxers) #Burada girilen indexte girilen boksörü görürüz
```

**Merging two lists:** Yeni bir liste tanımlayacalım ve bu liste içerisine ilk listemizde eklemediğimiz boksörleri ekleyelim:

```py
royal_division = ["Antorny Jasua", "Tyson Fury", "Deantony Wilder"]
#yeni bir liste tanımladık ve buraya farklı boksörleri yazdık.
```

Şimdi ise, iki listeyi birbirleriyle birleştirelim :) **.extend() metodu**nu kullanarak!

```py
boxers.extend(royal_division) #boxers listesine royal_division listesini ekledik
print(boxers) #burada iki listenin birleşmiş halini görürüz
```

Sadece indexini bildiğimiz bir değerin çıktısını öğrenmek istersek?

```py
print(boxers[2]) #Bu 2. indexteki değeri çekiyor, print fonksiyonu ile de yazdırdık.
```

Peki bu çıktıyı kendimizin belirlediği şekilde değiştirirsek?

```py
boxers[5] = "Joe Frazeir"
print(boxers) #5. Indexteki değeri "Joe Frazeir" ile değiştirdik.
```

Sürekli ekledik veya elimizdeki veriyi manipüle ettik, bir de çıkartmayı deneyelim ve bunu **.pop() metodu**nu kullanarak yapalım:

```py
boxers.pop(0) #burada da 0. indexteki ifadeyi index'i ile sildik.
print(boxers)
```

VEYA **.remove() metodu** ile içeriği vererek de silebiliriz!

```py
boxers.remove("Lenox Lewix") #burada da içeriğini girdik, ilk denk geldiğini siler.
print(boxers)
```

Son olarak, elimizdeki tüm verileri sırayla gezmek istersek de for döngüsünü kullanabiliriz :)

```py
for boxer in boxers: #boxer geçiçi bir isim olarak verildi burada.
    print(boxer)

for i in range(len(boxers)): #boxers listesinin uzunluğu kadar
    print(boxers[i])
```

## En çok karıştırılanlar

### Eklemek: `.append()` vs `.extend()`

* **`append(x)`:** Listeye `x` elemanını tek bir parça (paket) olarak ekler.
* **`extend(x)`:** `x` bir listeyse, içindeki elemanları tek tek çıkarır ve bizim listeye ekler (Unpacking).

```py
sepet = ["Elma", "Armut"]
eklenecek = ["Muz", "Çilek"]

# sepet.append(eklenecek) 
# Sonuç: ["Elma", "Armut", ["Muz", "Çilek"]] -> Liste içinde liste oldu (Nested List).

sepet.extend(eklenecek)
# Sonuç: ["Elma", "Armut", "Muz", "Çilek"] -> Hepsi tek bir aile oldu.

```

### Silmek: `.pop()` vs `.remove()`

* **`pop(index)`:** "Şu **konumdaki** elemanı at" (İndeks bazlı). Eğer indeks vermezsen en sonuncuyu atar. Ayrıca attığı elemanı sana geri verir (return eder).
* **`remove(değer)`:** "Listede gördüğün ilk 'Elma'yı sil" (Değer bazlı). Konumunu bilmediğin şeyleri silmek için kullanılır.
