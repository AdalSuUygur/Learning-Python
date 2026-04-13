
#! BUILT-IN FUNCTIONS

#* Doğrudan adıyla, nesneyi argüman olarak vererek çağrılırlar.
#* Bu fonksiyonlar "genelde" iterable olan tüm nesnelerde kullanılabilir.

#* Built in fonksiyonlarda çıktı olarak liste değil de kendi nesnesini veriyorsa içindeki değerlerin yalnızca ihtiyaç duyulduğunda diğer nesnelere çevrilmesini sağladığı içindir.
#* Neden önemli peki? ÇÜNKÜ Bu bellek verimliliği, büyük veri kümeleri için büyük bir avantajdır. MALİYET TATLIM!

#? range() fonksiyonu - built in fonksiyon.
for i in range(19):
    print(i) #tek sayı verdik, başlangıç değeri 0, artış miktarı 1

for i in range(3,6):
    print(i) #2 değer verirsek ilk değer başlangıç, ikinci değer bitiş, artış miktarı 1

for i in range(5,65,3):
    print(i) #başlangıç, bitiş, artış miktarı olarak sıralandı.

#todo Koleksiyonlarda genelde kullanılan fonksiyonlar
numeric_lst = [1,2,3,4,5,6,7,8,9,0]
alpha_lst = ["a","b","c","d","e","f","g","h"]

#region Veriyi Tanımak için Kullanılan Fonksiyonlar
#? len() built-in-function
#* Var olan listenin uzunluğu (kaç elemanı olduğunu) verir.

print(len(numeric_lst))
print(len(alpha_lst))

#? sum() buil-in-function
#* Listedeki tüm SAYISAL elemanların toplamını verir.

print(sum(numeric_lst))
# print(sum(alpha_lst)) # Çalışmadı, neden? ÇÜNKÜ STR + INT yapmaya çalıştı ve hata gönderdi. Type error.

#? max() - min() buil-in-functions
#* Listedeki en büyük ve en küçük değeri bulur (str de kabul eder)

print(max(numeric_lst), min(numeric_lst))
print(max(alpha_lst), min(alpha_lst))

#? sorted() buil-in-function
#* Listedeki elemanları sıralayıp YENİ BİR LİSTE döndürür.

print(sorted(numeric_lst)) #çıktı olarak lsite verdi, küçükten büyüğe sıraladı.
print(sorted(alpha_lst))

#endregion

#region Fabrika İşçileri (Map & Filter)
#? filter() buil-in-function
#* Bir kurala tanımlanır ve kurala uyan elemanları ayıklar
#* Listeler üzerinde filtrelemeye yarayan fonksiyon
#* Listedeki tüm öğeleri gezer ve koşulu True döndüren öğeleri seçerek yeni bir sonuç dizisi oluşturur.
#* Filtreleme kuralı basit olduğunda, genellikle yerleşik ve isimsiz Lambda fonksiyonları kullanılır, bu da kodu daha kısa yapar:
#* Filter fonksiyonu obje içinde obje yarattığı için (Lambda aslında bir fonksiyon) aslında oldukça maliyetli O(N**2) kadar maliyetli oluyor.

print( #filter fonksiyonu ile üretilen liste, geçiçi bir liste olduğu için
    list( #eldeki veriyi listeye çevirdik (çevirmezsek çalışmaz)
        filter(lambda x: x < 5, numeric_lst) #kümelere benzer, x öyle ki, numberic_lst'te 5'ten küçük olan x'leri al.
        )
    )

#region Examples
#todo Verilen listedeki değerlerin karşılığı sayısal ise bunu yazdıran uygulama
#* Hint: isgidit() fonksiyonunu kullan
#* Lambda fonksiyonu bir performans sorunudur, bunu engellemek için kullanmadan yapalım:

some_values = ["123", "su", "zxc", "987", "345"]
only_digit = list(
    filter(str.isdigit, some_values) #! lambdadan kurtulduk burda 
                                     #! built in fonksiyonlarını tiplerine özel olarak çalıştırabiliriz. 
                                     #! yani lambdayı built in fonksiyonlar özelinde kullanmayabiliriz.
)
print(only_digit)
#* Python programlama dili, içerisindeki built in fonksiyonları kullandığımız zaman daha hızlı çalışır.

#todo filter fonksiyonu ile çift sayıların filtrelenip ve liste olarak ekrana yazdırılması
# even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
# print(even_numbers)

#todo sonu .com ile biten mail adreslerini filter fonksiyonu ile yazdıran ifade
#* Hint: endswith() fonksiyonunu kullan

# mails = [
#     "burak.yilmaz@outloo.com", 
#     "savage@mail.com", 
#     "beast@", 
#     "keko@com.xyz", 
#     "adal@gmail.com"
# ]

# correct_mails = (list(
#     filter(
#         lambda x: x.endswith(".com"), mails)
#     )
# )
# print(correct_mails)
#endregion

#? map() built-in-function
#* map() fonksiyonunun ana amacı, koleksiyon üzerinde döngü kurup her öğeyi hızlı ve verimli bir şekilde işler.
#* Her elemana bir fonksiyon uygular.
#* Bu, özellikle büyük veri kümeleriyle çalışırken geleneksel for döngülerine göre daha okunabilir ve genellikle daha hızlı bir yaklaşımdır.

#* Tip dönüşümlerinde kullanılabilir, filtrelemelerde kullanılabilir, bir sınıf bir tipe ait mi değil mi gibi uygulamalarda kullanılır.
#* Gerçek hayat uygulamalarında "maplemek" terimi; belirli bir tipteki elemanları belirli bir tipe dönüştürmeye denir.

#SYNTAX YAPISI:
# map(fonksiyon, iterable nesne)

print(
    list(
        map(
            str, numeric_lst #numeric_lst içerisindeki itemları numeric ancak map fonksiyonu ile str'ye dönüştürdük.
        )
    )
)

#region Examples
#todo Mail adreslerinin içerisinde "@" olup olmadığını kontrol eden uygulama
# mail_adresses = [
#     "burak.yilmaz@outlook.com",
#     "hakan.yilmaz",
#     "ipek.yilmaz@outlook.com"
# ]

# print(
#     list(
#         map(
#             lambda x: "@" in x, mail_adresses
#         ) #true, false, true çıktısı verir. 
#     )
# )

# print(
#     list(
#         filter(
#             lambda x: "@" in x, mail_adresses
#         ) #bu da doğrudan mail adreslerini çıkartır.
#     )
# )

#todo Liste içerisindeki listede verilen ürünler ile alakalı uygulamalar
products = [ #ürün adı, stoktaki miktarı, fiyatı
    ["boxing gloves", 100, 59.9],
    ["punching bags", 150, 160.99],
    ["hand wrap", 200, 11.99]
]

#Priceların ekrana yazdırılması
# print(
#     list(
#         map(
#             lambda x: x[2], products
#         )
#     )
# )

#Pricelara %10 KDV uygulanılması
# print(
#     list(
#         map(lambda x: round(x * 1.1,2), [price for name, stock, price in products])
#     )
# )

#todo Verilen listedeki isimlerin baş harflerini büyüten uygulama
names = [ #Bu listemiz
    "lale selam",
    "aslı meram",
    "karam çalık",
    "alık balık",
    "sade kanık"
    ]

# print(
#     list(
#         map(str.title, names)
#     )
# )

#todo verilen listeden mail adresi craft eden uygulama
domain_name = "@outlook.com"

#kendi çözümüm boşluğu kaldırarak çözmüşüm
# print(
#     list(
#         map(
#             lambda x: x + domain_name, [name.lower().replace(" ", "") for name in names]
#         )
#     )
# )
#hocanın çözümü hoca nokta eklemiş
# print(
#     list(
#         map(
#             lambda x: f"{x.replace(' ', '.')}{domain_name}", names)
#         )
#     )

#todo Verilen 2 farklı listenin aynı indexlerinin toplanması uygulaması
#* ÖNEMLİ: Sana gerçek hayat uygulamalarında BİR LİSTENİN DİĞERİNDEN KISA OLDUĞU CASE'i HESABA KATMANI İSTERLER!!!!
from random import randint
numbers_1 = [randint(-100,100) for _ in range(25)]
numbers_2 = [randint(-100,100) for _ in range(12)]
#print(numbers_1) #test
#print(numbers_2) #test

#PATH I - map()
# print(
#     list(
#         map(
#             lambda x, y: (x + y), numbers_1, numbers_2)
#         ) 
#     )
#map() fonksiyonu da kısa olanı alır ikili verilen inputlarda, bu yüzden bu çıktı da düzgün gelir.

#PATH II - zip()
#print(list(zip(numbers_1, numbers_2))) #şu an bu 2 elemanlı tuplelerden oluşan bir liste, test amaçlı yazdırdık

# print(
#     list(
#         map(
#             lambda x: x[0] + x[1], #iki elemanlı tuplelerden 0. eleman ve 1. elemanı yani tupleleri topluyoruz birbirleriyle.
#             zip(numbers_1, numbers_2) #burda zip'ten çıkartıp listeye çevirmiyoruz çünkü çıkan zip özel nesnesi de iterable bir nesne
#         )
#     )
# ) #zip fonksiyonu zaten kısa olana kadar alacağı için bu senin safe yolun olacak.
#endregion

#endregion

#region Birleştiriciler (Zip & Enumerate)

#? zip() built-in-function
#* Listeleri, tupleları, numply arraylerini YANİ koleksiyonları birbirleriyle eşleyerek birleştiren bir fonksiyon
#* Elemanları sırasıyla birleştirir, Tuple çiftlerinden oluşan YENİ bir zip nesnesi (kendine özgü bir tip) oluşturur.
#* Zip fonksiyonu ile transpoz işlemi sıklıkla yapılır (satır sütun bilgilerini sütur satın olarak güncelleme, yani yerlerini değiştirme)

esleştirilmiş_veri = zip(alpha_lst, numeric_lst) #bu bir veridir, bunu listeye çevirmek gerekir.
eslestirilmiş_lst = list(esleştirilmiş_veri)
print(eslestirilmiş_lst)

#* En başta, her iki listenin de uzunluğunu yazdırdık ve birbirlerinden farklılardı, peki bu zip ile patlamadıysa zip kaç elemanlı oldu?
print(
    len(
        eslestirilmiş_lst 
    )
) #uzunluğu küçük olanı aldı, yani, verinin karşılığı yoksa bunu paketlemedi.

#? Unzipping (* operatörü ile)
#* Genellikle zip() yerleşik fonksiyonu ile oluşturulmuş bir veri yapısını geri açma(unboxing) bağlamında kullanılır.
unzipped_numeric, unzipped_alpha = zip(*eslestirilmiş_lst)
print(unzipped_numeric) #burda ziplenmiş veriyi geri aldık ancak orijinal listedeki 9,0'ı almadı çünkü eşleştirilmiş listede kesip atılmıştı bunlar
print(unzipped_alpha)

#region Examples
#todo Örnek zip() fonksiyonu uygulaması, 2 listede 10ar adet random sayılar üretilecek ve indexlerdeki değerler toplanarak sonuçları liste olarak veren uygulama
from random import randint
# number1 = [randint(a= 0, b=100) for _ in range(10)]
# number2 = [randint(a= 0, b=100) for _ in range(10)]

# numbers = list(zip(number1, number2))
# addition = [n1+n2 for n1, n2 in numbers]
# print(numbers)
# print(addition)

#todo Index ve itemı ziplenen uygulama (zip ile enumerateyi taklit etme)
# lst = ['ayhan', 'elton', 'adal', 'merve']

# print(
#     list(
#         zip(
#             range(len(lst)), lst #indexi nasıl alabiliriz, range nerde durmalı, listenin uzunluğu kadar durmalı, buyrun yaptık
#             ) #ve böylece enumerate() built in fonksiyonunu zip ile taklit ettik.
#         )
#     )

#todo Ödev: Transpoz ödevi, 3 line 10ar tane rastgele sayı ile doldurulacak ve index değerleri olarak çıktı alınacak
# matrix = [
#     [34, 56, 123, 56], # --> bu iç listeler list comprehnsion ile rastgele sayılar ile doldurulacak
#     [23, 67, 12, 45],
#     [11, 54, 89, 22], # --> 3 line yeterli
# ]
# Output:
# [(34, 23, 11), (56, 67, 54), (123, 12, 89), ....]

# matrix = [
#     [randint(0,100) for _ in range(10)] #0-100 arasında 10 tane sayı ürettim
#     for _ in range(3) #bundan 3 tane üretmem gerekiyordu bunu da list comprehension ile ürettik
# ]
#print(matrix) #test

#path i
# matrix_transpose = list(    zip(  matrix[0], matrix[1], matrix[2]  )   )
# print(matrix_transpose)

#path ii
# print(list(zip(*matrix)))


# print(matrix[i][j]) 
# i = range(len(matrix))
# j = range(10)
#endregion

#? enumarete() built-in-function
#* Bir koleksiyonu döngüde gezerken hem elemana hem de sırasına (indeksine) ihtiyacınız olduğunda bunları veren fonksiyon

for index, item in enumerate(alpha_lst):
    print(
        f"Index value: {index}", end=" - "
        f"Item Value: {item}\n"
    )
#endregion

#region Mantıksal Dedektifler (Any & All)

#? any() buil-in-function
#* Listedeki elemanları gezer, istenilen en az bir tane varsa true döndürür, yoksa false döndürür.
#* Yani, any içinde herhangi bir şey tutuyosa true, tutmuyosa false dönüyor

bos_lst = [0, False, "", (), []] # Tüm elemanlar boş (0, False, boş string, boş liste)
print(any(bos_lst)) # Sonuç: False (Çünkü listede True kabul edilen tek bir değer bile yok.)
print(any(numeric_lst)) #Sonuç: True çünkü 0 haricindeki sayılar True döner.

#region Examples
#todo any() fonksiyonu uygulaması
# programming_languages = [   "python",  "java", "go"    ]
# print(  any(    pl == "python" for pl in programming_languages  )   ) #1 tane şart tutarsa true döner, yani true çıkar.
# print(  any(    pl == "c#" for pl in programming_languages  )   ) #hiçbir şartı tutmuyor. False döner.

#todo any fonksiyonu ile verilen listede 10'dan büyük sayı var mı kontrol eden uygulama
# numbers = [3,4,5,6,7,8,9]
# result = any(number > 10 for number in numbers)
# print(result)

#todo any() fonksiyonu list comprehension örnekleri ile daha iyi anlaşılabilir.
passwords = ["123", "98a", "12q", "987"]
print(
    any(
        ch.isalpha() for pwd in passwords for ch in pwd #password listesindeki her pwd adlı itemın ch adlı karakterinin alfabetik olup olmadığına bakar
        ) #True döner çünkü bir tane bile elemanının içinde olması yeterli.
) #çıktı olarak da True alırız.

# List comprehension ile nested for yaptık, daha sonra beynim yanarsa diye buraya açık halini ekliyorum:
# for pwd in passwords:
#     for ch in pwd:
#         print(any(ch.isalpha()))

#todo is_valid Password uygulaması
# Şartlar: min 16 karakter, min 1 büyük; 1 küçük harf, min 1 noktalama işareti, min 1 rakam
# Hint: String kütüphanesi içerisinde noktalama işaretleri hazır olarak var
import string
password = input("Enter a password: ")

#region kendi çözümüm
# def is_valid(password):
#     karakter = len(password) #min 16 karakter olmalı
#     buyuk_harf = any(char.isupper() for char in password)
#     kucuk_harf = any(char.islower() for char in password)
#     noktalama_isareti = any(char in string.punctuation for char in password) #bunu yine kullanmada sıkıntı çektim.
#     rakam = any(char.isnumeric() for char in password)
#     if karakter <= 16:
#         return False, "minimum karakter sınırı"
#     elif not buyuk_harf:
#         return False, "büyük harf eksik"
#     elif not kucuk_harf:
#         return False, "küçük harf eksik"
#     elif not noktalama_isareti:
#         return False, "noktalama işareti eksik"
#     elif not rakam:
#         return False, "rakam eksik"
#     return True, "valid password"

# gecerli_mi, ciktisi = is_valid(password)

# if gecerli_mi:
#     print("hoşgeldiniz " + ciktisi)
# else:
#     print(ciktisi)
#endregion

# region hocanın çözümü
# if len(password) < 16:
#     print("invalid password")
# if not any(ch.isupper() for ch in password):
#     print("invalid password")
# if not any(ch.islower() for ch in password):
#     print("invalid password")
# if not any(ch.isdigit() for ch in password):
#     print("invalid password")
# if not any(ch in punctuation for ch in password):
#     print("invalid password")

#*logic mantığı
# if (
#     len(pwd) < 16 and
#     not any(ch.isupper() for ch in pwd)
#     #and ile bağlayıp herhangi bir şey
# ):
#     print()

# endregion
#endregion

#? ALL FUNCTION
#* Bir şart yazılır ve şart listenin tüm elemanları için sağlıyorsa true, sağlamıyorsa false döndürür.
#* Bütün itemların şartı sağlaması lazım
ages = [18,24,35,65,41,13]
member = all(age > 18 for age in ages)
print(member) #hepsi 18den büyük olmadığı için false döner

#todo örnek tüm ürünlerde stok var mı yok mu
# products = [
#     ['name', 'boxing gloves', 'price', 59.99, 'stock', 5],
#     ['name', 'punching bags', 'price', 159.99, 'stock', 15],
#     ['name', 'handwrap', 'price', 19.99, 'stock', 0]
# ]

# stock = all(product[5] > 0 for product in products)
# print(stock) #false döner çünkü stokta 0 olan ürün var

#todo örnek password
# password = "Bu?ra4k_"

# is_password_valid = [
#     any(ch.isupper() for ch in password),
#     any(ch.islower() for ch in password),
#     any(ch.isdigit() for ch in password),
#     any(not ch.isalnum() for ch in password)
# ]
# print(
#     all(is_password_valid)
# )

#endregion

#region Kimlik Kontrolü

#? isinstance() built-in-function
#* içerisine girilen nesnenin belirli bir veri tipine ait olup olmadığını kontrol etmeye yarayan built-in fonksiyondur.
#* Yani: "Bu nesne, bahsettiğim türden bir şey midir?" sorusunun cevabını True veya False olarak verir.

print(isinstance(alpha_lst, str)) #alpha_lst öğesi string midir? HAYIR çünkü bir listedir :)
print(isinstance(alpha_lst, list))

#todo Verilen listeden tam ve ondalıklı sayıları alma uygulaması
lst = [None, "b", 3.14, False, 9, "Oscar Piastri"]

numbers = list( #listeye convert etmek için.
    filter(
        lambda x: isinstance(x, (int, float)), lst) #x yani lst'teki eleman int veya float mı
)
print(numbers) #çıktı olarak da: [3.14, False, 9] verir, çünkü isinstance değeri bool döndürür, bundan dolayı direkt öyle bir ifadeyi çıktı olarak verir.

#endregion

#region Examples

#todo 17. Ders ödevi #2
#* -100 ile + 100 arasında 10 tane rastegele sayı üretelim
#* sadece pozitif sayıları string dönüştürerek bir liste içerisinde çıktı verin

# from random import randint
# numbers = [randint(-100,100) for _ in range(10)]
# print(numbers) #test


# print( #4. adım : terminale çıktısını verdik
#     list( #3. adım : yazdırabilmek veya tutabilmek adına listeye çevirdik
#         map(str, #2. adım : map ile, gelen int değerleri str'ye çevirdik
#                 filter(lambda x: x>0, numbers) #1. adım : 0'dan büyük olan sayıları çektim
#             )
#         )
#     )

#todo 17. Ders ödevi #1
#* list comprehension ile 2 tane rastgele sayılar içeren liste oluşturun
#* üretilecek sayı aralıkları -100, +100
#* her iki listedeki sayıları toplayalım
#* toplamları negatif olanları pozitif dönüştürerek bir liste içerisinde yazdıralım

from random import randint
numbers_1 = [randint(-100,100) for _ in range(10)]
numbers_2 = [randint(-100,100) for _ in range(10)]
# print(numbers_1) #test
# print(numbers_2) #test

# print( #5. adım : terminale çıktısını verdik
#     list( #4. adım : bulunan değerleri listeye çevirdik.
#         map(abs, #3. adım : burda da hesaplanan değerlerin mutlak değerini aldık
#             map(lambda x: x[0] + x[1], #2. adım : map fonksiyonu ile tupledaki değerleri topladık
#                 zip(numbers_1, numbers_2)) #1. adım : iterable nesnemizi yarattık ve 2 farklı listenin indexlerini birleştirdik
#         )
#     )
# )

#derste örneğin çözümü ve hocanın esktraları:
# result = [abs(x+y) for x,y in zip(numbers_1,numbers_2)]
# lst_result = list(map(str, result))
# print(list(map(str, result)))
#çıktının "-" ifadelerle bağlanmasını istiyoruz.
# print("-".join(lst_result)) #stringe dönüştürmemizin sebebi join fonksiyonunu kullanmak.

#todo -100 ile 100 aralığındaki 1000 random sayı ile oluşturulan bir listeden pozitif sayıları çekme uygulaması
numbers = [randint(a=-100, b=100) for i in range(1000)] #numbers diye 1000 itemlı liste oluşturuldu

#PATH I --- list comprehension
# lst_positive_numbers = [number for number in numbers if number > 0]
# print(lst_positive_numbers)

#PATH II --- filter() function
# temp_lst = filter(lambda x: x>0, numbers) #geçici bir liste oluşturuldu, lambda fonksiyonunu küme tanımlamalarına benzetebilirsin
#* Geçici listede, numbers listesi içerisindeki x için, x>0 durumlarını temp_lst değişkenine ekle gibi bir çıkarım var.
# lst_positive_numbers_lambda = list(temp_lst) #gelen değişkeni listeye çevirdik.
# print(lst_positive_numbers_lambda)

#endregion
