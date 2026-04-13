
#! COLLECTIONS

#? Unpacking - Unboxing (Söz dizimi özelliği)
#* Bir koleksiyonun öğelerini alıp bu öğeleri ayrı ayrı değişkenlere atanması durumudur.

my_family = [ #Bu listemiz
    ["Lale Selam", 29, "Analyst-Unemployed"],
    ["Aslı Meram", 33, "Guidance Counselor"],
    ["Karam Çalık", 37, "English Teacher"],
    ["Alık Balık", 61, "Retired"],
    ["Sade Kanık", 67, "Chauffeur"]
]

for item in my_family: #şimdi ailedeki her bir öğeyi dışarı çıkartıyoruz (bu da unboxing aslında)
    print(item) #Kısaca liste içindeki listenin dış listesinden kurtardık.

#* Unpacking yaparken karşılaması gereken valueların tam olması lazım, eksik veya fazla olursa patlar
for name, age, occupation in my_family: #myfamilyden bana gelen bilgileri öyle bir karşılayayım ki tık tık tık eşleşsin
    print(                              #Ki bu da unboxing bak
        f"Full name: {name}\n"
        f"Age: {age}\n"
        f"Occupation: {occupation}"
    )

#? .join() Metodu
#* join() metodu, bir iterable (liste, tuple, küme, dize vb.) içindeki tüm elemanları birleştirerek tek bir dize (string) oluşturan bir metoddur. 
# Birleştirme sırasında, metodun çağrıldığı dize, elemanlar arasına ayırıcı olarak eklenir.
#f formating +larla birleştirmek gibi, +larla neden birleştirmek yeirne join, çünkü stringler değiştirilemez yapılardır ve + ile eklendiğinde yeni bir string oluşturulur
#bu da haliyle maliyet demek, artılarla birleştirme, bu amatörce.

#* İki string ifadeyi birleştirmek için " " = "" + "" gibi kullanılır.
#* fstring içinde de benzer bir yapı ile ifadeler birleştirilir.
#* stringler değiştirilemez yapılardır, iki string ifadeyi birleştirince ramde farklı bir yere yazdırır (memory leake sebep olur) bundan dolayı daha az maliyetli olan join kullanılır.

#* Önemli Not: join() metodu, ayırıcı (separator) olarak kullanılacak olan dize üzerinde çağrılır, birleştirilecek iterable üzerinde değil.

#region Examples
#todo E-Ticaret Sepet Analizi
#* Sistemde bir hata olmuş ve bazı ürünlerin fiyatı negatif (`-`) girilmiş. Ayrıca 100 TL üzerindeki ürünlere %10 indirim yapman gerekiyor.
# fiyatlar = [150, -20, 300, 50, -5, 120]

# pozitif_fiyatlar = [(fiyat * -1) if fiyat < 0 else fiyat for fiyat in fiyatlar]
# print(pozitif_fiyatlar) #test, pozitifleri gördük

# indirimli_fiyatlar = [(fyt * 0.9) if fyt > 100 else fyt for fyt in ((fiyat * -1) if fiyat < 0 else fiyat for fiyat in fiyatlar)]
#tekrar list comprehension ile yaptım
#memory efficienct için generator kullandım pozitif fiyatlar için
#bunu ayrıca bir liste oluşturarak tanımlamadım ki hepsini list comp. içine alabileyim.
# print(indirimli_fiyatlar)

#todo Gelen iki data sheetten biri "İstanbul Müşterileri", diğeri "Geçen Ay Alışveriş Yapanlar". Ortak olanları sil ve istanbulda oturup geçen ay alışveriş yapmayanları bul.
# istanbul = ["a@mail.com", "b@mail.com", "a@mail.com", "c@mail.com"]
# alanlar = ["b@mail.com", "d@mail.com", "b@mail.com"]

# print(set(item for item in istanbul)) #set comprehension
# print(set(item for item in alanlar)) #tekrar eden elemanlardan arındırdık

# print(
# set(item for item in istanbul) #istanbulda oturup
# - #fark operatorü
# set(item for item in alanlar) #geçen ay alışveriş yapmayanları
# )

#todo Kelime Frekansı (Dictionary) Elinde bir cümle var ve hangi kelimenin kaç kere geçtiğini bulman gerekiyor.
metin = "elma armut elma kiraz elma armut"
meyveler = metin.split()

#Path I:
# frekanslar = {}
# for meyve in meyveler:
#     if meyve not in frekanslar.keys():
#         frekanslar[meyve] = 1
#     else:
#         frekanslar[meyve] += 1
# print(frekanslar)

#Path II: Dict Comprehension denedim ama çalışmadı çünkü bu blok içinde atama veya artırma yapamıyorum.
#frekanslar = {frekanslar[meyve] = 1 if meyve not in frekanslar else frekanslar[meyve] += 1 for meyve in meyveler}

#onun yerine gemini illaki oluşturcaksa böyle oluşturalım dedi.

# "Her meyve için: Anahtar=Meyve, Değer=Listede Kaç Tane Var?"
# frekanslar = {meyve: meyveler.count(meyve) for meyve in meyveler}
# print(frekanslar)

#todo List, Dict ve Zip (fermuar) mantığı

isimler = ["Ali", "Ayşe", "Mehmet"]
notlar = [85, 90, 70]

#Path I:
# sozluk = {
#     isim: score for isim,score in zip(isimler, notlar)
# }

#Path II:
# sozluk = dict(zip(isimler, notlar))
# print(sozluk)

#endregion
