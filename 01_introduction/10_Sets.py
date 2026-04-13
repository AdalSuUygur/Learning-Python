
#! SETS - KÜMELER
#* Matematikteki kümeler yapısıdır. Bir koleksiyondur.
#* Öğeler sırasızdır, değiştirilebilirdir. Ancak öğeler UNIQUE yapıdadır.
#* Yani: tekrarlı eleman olmaz ama kendine has unique bir dönüş tipi vardır.

#? SYNTAX
# Set süslü parantez "{}" ile tanımlanır.

numbers = {1, 4, 1, 5, 3, 2, 1, 3, 3, 5, 5, 5, 2, 3, 4, 5}
print(numbers)
# Çıktı: {1, 2, 3, 4, 5}
# -> Bak, tekrar eden sayıların hepsi uçtu! Sıra da değişti.
# Yani, tekrar eden sayılar gösterilmedi!

# Sadece sayısal verilerde değil, sözel ifadelerde de kullanılabilir.
full_name = "adalsuuygur"
unique_ch = set(full_name) #bu da convert etme özelliği
print(unique_ch)

# Boş Set Tanımlarken DİKKAT:
bos_sozluk = {} # Bu bir dict (sözlük) yaratır.
bos_set = set() # Boş set sadece bu şekilde yaratılır.

#? set() built-in-methods
#* Formula1 Driverlarından devam edelim :)
drivers = {
    "Oscar Piastri", "Lando Norris", 
    "George Russell", "Kimi Antonelli",
    "Max Verstappen", "Yuki Tsunoda",
    "Charles Leclerc", "Lewis Hamilton"
} #süslü parantez ile set olarak tanımladık :)
print(drivers) #buraya herhangi bir şey eklemedik yani albon'u görmeyeceğiz.

#* Eleman eklemek için .add()
drivers.add("Alex Albon") #Alex Albon'u driverlara ekledik
print(drivers)

#* Eleman silmek için .remove()
drivers.remove("Alex Albon") #Burda Alex Albon'u setimizden çıkarttık.
print(drivers)
# Remove methoduna olmayan bir eleman yazıldığında patlar

#* Eleman silmek için .discard(), farkı ise patlamıyor :)
drivers.discard("Alex Albon") #Şu an setimizde alex albon yok ama bu blok çalışacak
print(drivers)
# Çünkü discard methodu bu varsa silerim yoksa da ignorelar devam ederim diyor

last_drivers = {
    "Max Verstappen", "Yuki Tsunoda",
    "Charles Leclerc", "Lewis Hamilton",
    "Carlos Sainz", "Alex Albon",
    "Liam Lawson", "Isack Hadjar",
    "Esteban Ocon", "Oliver Bearman",
    "Lance Stroll", "Fernando Alonso", 
    "Nico Hulkenberg", "Gabriel Bortoleto",
    "Pierre Gasly", "Franco Colapinto" } 
#yeni bir set tanımladık ve burada kalan diğer driverları ve drivers setindeki bazılarını yazdık.

#* İki setin kesişen elemanları için .intersection()
print(drivers.intersection(last_drivers))

#* İki seti birleştirmek için .union()
print(drivers.union(last_drivers)) #tekrarlayan eleman göremeyiz

#* Bir setin diğer set ile arasındaki farklı elemanları görmek için .difference()
print(drivers.difference(last_drivers))

#? set()'in kendine has operatörleri

#* Birleşim (Union) `|`
print(drivers | last_drivers) #union methodu

#* Kesişim (Intersection) `&`
print(drivers & last_drivers) #intersection methodu

#* Fark (Difference) `-`
print(drivers - last_drivers) #difference methodu

#* Simetrik Fark (Symmetric Difference) `^`
#(Kesişimin tam tersi gibi düşün)
print(drivers ^ last_drivers)

#region Examples

#todo Bir e-ticaret siten var. Günlük ziyaretçi ID'lerini topluyorsun ama bazıları siteye 10 kere girmiş. Analiz için bize sadece "tekil" (unique) kişiler lazım.

gunluk_ziyaretciler = [101, 102, 101, 105, 102, 108, 101] #listesini bir set'e çevirerek tekrarlayanları temizle.

eski_ziyaretciler = {101, 102, 103} #adında bir kümemiz daha var.

set_gunluk_ziyaretciler = set(gunluk_ziyaretciler)

print(
    eski_ziyaretciler & set_gunluk_ziyaretciler
) #Hem bugün hem de eskiden gelen ortak ziyaretçileri bul

print(
    set_gunluk_ziyaretciler - eski_ziyaretciler
) #Sadece bugün gelen (eski listede olmayan) "yeni" ziyaretçileri bul

#endregion