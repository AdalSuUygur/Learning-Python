
#! LISTS - LİSTELER
#* Farklı veri tiplerini tek bir yerde tutmaya yarayan veri koleksiyonlarıdır.
#* Listeler verileri kalıcı olarak depolamazlar, listeler RAM'de depolanır.
#* LİSTELER DEĞİŞTİRİLEBİLİR (MUTABLE) BİR VERİ KOLEKSİYONUDUR

# SYNTAX YAPISI
meyveler = ["elma", "muz", "kiraz"]
karisik_liste = [10, "Merhaba", 3.14, True] #burdan öğrenmemiz gereken şu, listelerde FARKLI VERI TİPLERİ AYNI ANDA DEPOLANABİLİR!!

#? Index Nedir, nasıl çalışır
#* Index, bir listedeki her bir öğenin konumunu belirten sayısal etikettir. 
#* Listeler sıralı olduğu için, her öğenin sabit bir konumu vardır.
#* Negatif indeksleme ile listenin son öğesine -1. elemanı ile ulaşabildiğimizi gösterir.

#SYNTAX OLARAK GÖSTERİMİ
isimler = ["Ali", "Burak", "Cem", "Deniz"]
# Index:    0       1       2        3
# Negatif: -4      -3      -2       -1

print(isimler[0])   # Çıktı: Ali (İlk öğe)
print(isimler[3])   # Çıktı: Deniz
print(isimler[-1])  # Çıktı: Deniz (Son öğe)

#region Nested List
#? Nested List Yapısı
#* Liste içerisinde liste yapısıdır, en basit anlatımıyla matematikteki matriks yapısı gibi düşün.

alisveris_sepeti = [
    "Ekmek",                        # 0. indexteki Tekil Ürün
    "Süt",                          # 1. indexteki Tekil Ürün
    ["Elma", "Muz", "Portakal"],    # 2. indexteki öğeler (Meyveler Kutusu)
    ["Kalem", "Silgi"],             # 3. indexteki öğeler (Kırtasiye Kutusu)
    15.99                           # 4 indexteki ürün (fiyat)
]
# alisveris_sepeti listesi 5 öğeye sahiptir ve 2 ve 3. indexteki öğeler de ayrıca listelerdir.
print(alisveris_sepeti[2][2]) #Listenin 2. indexteki elemanının 2. indexindeki elemanını yazdır.
#endregion

#region Dilimleme
#? Slicing (Dilimleme) Operatörü
#* Pandas (veri analizinde de) kullanılır, çok önemli!!!!
#* Mevcut bir SIRALI YAPININ belirli bir bölümünü alarak YENİ BİR YAPI oluşturma işlemidir. 
#* Bu dilimleme orjinal listeyi değiştirmez.

#SYNTAX YAPISI
#           yeni_liste = eski_liste [başlangıç_index(DAHİL) : bitiş_index(HARİÇ) : adım] 
#             default değerleri --- [       0 (SIFIR)       :    listenin_sonu   :  1  ]

fruits = [
    "Apple", "Banana", "Orange", "Mango", "Pineapple",
    "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
    "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
    "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"
]

print(fruits[2:7]) #birinci değer başlangıç indexi, ikinci değer n-1 olacak şekilde kapanış indexi
print(fruits[:3]) #burada başlangıç belirtilmedi yani başlangıç 0 ve burada : ile 3.ye kadar diyoruz
print(fruits[1::2]) #birden başla, iki iki zıplayarak git demek çift iki nokta ile 
print(fruits[::4]) #gene başlangıCı vermedi ama 4er 4er zıplayarak git anlamına geldi 

print(fruits[::-1]) #0dan başla, -1 -1 git dedik ve aslında listeyi tersine çevirmiş olduk. 
# eksi koyunca reverse ediliyor gibi düşün, 0. eleman direkt son eleman gibi düşün
print(fruits[10::-3]) #başlangıç verdik diye burda reverse düşünme, 10. elemandan başla geriye doğru 3er adımla git
print(fruits[::-2])
#endregion

#region Satır Sutün Algoritması
#? Satır-Sütun algoritması
#* SATIR SÜTUN ALGORİTMALARINDA: i satırı, j sütunu yönetir, yani i 1. adımındayken j orada belirtilen adım kadar çalışır.

#Geleneksel yöntem:
for i in range(1,11):
    for j in range(1,11):
        print(f"{i} x {j} = {i * j}")
    print("-------------------")

#List comprehension ile yapılması:
lst_carpim_tablosu = [ 
    (i*j) #yazdırılacak sonuç 
    for i in range(1,11) #en dış döngü
    for j in range(1, 11) #en iç döngü
]
print(lst_carpim_tablosu)
#* Tek satır olmadı yine alt satıra geçtik, ee ne anlamı kaldı list comprehension'ın? Go for benchmark testing!

#List comprehension ile PRINT FONKSİYONU İÇİNDE yapılması:
print(
    [
        [f"{i} x {j} = {i * j}" for i in range(1, 11)] for j in range(1, 11) #liste içinde liste yaptık
    ]
    ) #Burda aslında list içinde for içinde for ve liste içinde liste de tanımlıyoruz, sınırımız yok.
#endregion
