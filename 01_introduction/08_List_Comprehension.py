
#! LIST COMPREHENSION

#* Bir listeyi oluşturmak için gereken adımları (boş liste tanımlama, döngü kurma, .append() ile ekleme), tek bir sözdizimi içine yerleştirmektir.
#* Yani listeyi kısaca oluşturmak için List Comprehensions kullanılır.

#Geleneksel yöntem ile liste oluşturma:
lst_geleneksel = []
for i in range(10):
    lst_geleneksel.append(i)
print(lst_geleneksel)

#YA DA list comprehension ile kısa yoldan liste oluşturma:
#* append etme mantığı gibi düşün, bak geleneksek yöntemle i'yi ekliyoruz append ile ama tek satırda.
lst_comprehension = [i for i in range(10)]
print(lst_comprehension)
#* Comprehension kompleksleştikçe yazması da okuması da zorlaşıyor, peki neden tercih ediliyor? ÇÜNKÜ ÇOK DAHA AZ MALİYETLİ

#region examples
#todo Ternary if + List Comprehension ile
fruits = [
    "Apple", "Banana", "Orange", "Mango", "Pineapple",
    "Strawberry", "Grapes", "Watermelon", "Peach", "Cherry",
    "Papaya", "Kiwi", "Blueberry", "Raspberry", "Guava",
    "Pomegranate", "Lemon", "Apricot", "Fig", "Pear"]

#todo1 meyve listesindeki meyvelerin içerisinde "a" geçiyorsa bu meyveleri yazdıran uygulama
lst_includes_a = [fruit for fruit in fruits if "a" in fruit.lower()] #fruit.lower() yazmamızın sebebi de içinde küçük a harfine bakıyor olmamız.
print(lst_includes_a)

#todo2 meyve listesindeki meyvelerin içerisinde "an" geçiyorsa True, geçmiyorsa False eklenen uygulama
# Hint: "adult" if age >= 19 else "child"
lst_includes_an = [True if "an" in fruit.lower() else False for fruit in fruits] #ternary if yapısı ile kullanabildik
print(lst_includes_an)

#todo Girilen sampledaki sesli harfleri, sessiz harfleri, typoları ayrı listelere ekleyen uygulama. İlgili listelerde eleman tekrarı olmamalı. Space ignore.
sample = "buRa1k _Ayi?Lm2aZu"
# sesli_harfler = list(
#     {ch for ch in sample if ch in "aeıioöuü"}) #set comprehension :D set de küme, tekrarlı eleman olmaz.
# sessiz_harfler = set(
#     [ch for ch in sample if ch in "bcçdfgğhjklmnprsşvyz"])
# typo_char = list(
#     {ch for ch in sample if not ch.isalpha()}
# )
# print(sesli_harfler, sessiz_harfler, typo_char)

#todo rastgele üretilmiş 10 sayı ile list comprehension uygulaması
from random import randint
# lst_random = [randint(a=10, b=100) for _ in range(10)] #i yerine underscore yani _ kullandık sayaç yerine zaten çok da önemli değil.
# print(lst_random)

# #geleneksel yöntemle:
# lst_random_geleneksel = []
# for i in range(10):
#     lst_random_geleneksel.append(randint(0,100))
# print(lst_random_geleneksel)

#todo rakamların karesinin list compehension ile oluşturulması
# lst_squares = [i**2 for i in range(10)] #işlem yapabildik.
# print(lst_squares)

#todo 0-100 arasındaki çift sayıları listeye eklenmesi
#deneme = [i % 2 = 0, for i in range(101)] #* Bak bu olmadı, gördün mü? Çünkü if'e ihtiyaç var.
                                           #* List Comprehension uygulamarında içine if de ekleyebiliriz.
# lst_even_numbers = [i for i in range(101) if i%2 == 0] #if ile birlikte kullanabildik.
# print(lst_even_numbers)

#todo -100 ile 100 aralığındaki 1000 random sayı ile oluşturulan bir listeden pozitif sayıları çekme uygulaması
numbers = [randint(a=-100, b=100) for i in range(1000)] #numbers diye 1000 itemlı liste oluşturuldu

# lst_positive_numbers = [number for number in numbers if number > 0]
# print(lst_positive_numbers)
#endregion
