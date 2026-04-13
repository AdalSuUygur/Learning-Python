
#! TUPLES - DEMETLER
#* Koleksiyonlardır.
#* Immutable yapısı sebebiyle CRUD operasyonları yapılamaz.
#* Değiştirilemediği için sabitleri tanımlamak için tercih edilir.
#* Yapısı gereği okuma operasyonlarında diğer koleksiyonlara göre daha hızlı çalışır.

#? Örneğin: Bir data sheet geliyor ve programcı buradan okuma yapacak. Bu noktada verilen değiştirilmemesi istendidiği için, tuple'a dönüştürülür.

#? SYNTAX YAPISI
# tuple tanımlaması = () yani normal parantez kullanılarak tanımlanır.
# --- TUPLE (Değiştirilemez) ---
koordinatlar_tuple = (41.0082, 28.9784)  # İstanbul'un konumu
# koordinatlar_tuple[0] = 50.000  # Değiştirilemez, typeError verir.

#todo Tuple kullanılarak yapılabilecek işlemler:
#* Tuplelarda built in fonksiyonları yoktur; 
#* Tupleların sadece count ve index methodları vardır.
tuple_1 = ("Galatasaray",
           "Adana Demirspor",
           "Beşiktaş",
           "Trabzonspor",
           "Fenerbahçe"
           )

tuple_2 = ("Red Skins",
           "Seahawks",
           "Vikings",
           "Patriots"
           )

tuple_3 = tuple_1 + tuple_2 #max yapılabilecek işlem toplama
print(tuple_3[2:5]) #ve dilimleme yapılabilir
