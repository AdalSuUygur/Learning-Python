
#! Operatörler
#* Bir veya daha fazla işlenen, operand adı verilen değer üzerinde belirli bir matematiksel, mantıksal veya atama eylemini gerçekleştiren mekanizmalardır.

#? in operatörü
print('s' in 'su') #su içinde s varsa true döner
print('a' in 'su') #içinde mi diye sorar
#? not in operatörü
print('s' not in 'su') #su içinde s yoksa true döner
print('a' not in 'su') #içinde değil mi

#todo Girilen 3 sayıdan büyük olanın ekrana yazdılması (and & or operatörlerinin kullanılması)
n1 = int(input("First number: "))
n2 = int(input("Second number: "))
n3 = int(input("Third number: "))
max_number = 0 #Maximum sayımıza atamak üzere bir değişken tanımladık

#burada hep matematikteki mantık ifadelerini düşün, çünkü aynı şekilde çalışıyor.
#Lisedeki ilk sınavında matematik sınavına girip mantık çözmüştün
#Hiç çalışmamıştın ve 30 bekliyordun, sınıf birincisi oldun ve 80 aldın.
#Daha sonra hiç çalışmayarak tüm liseyi geçeceğini sandın ama çok yanıldın :D Yine de bu güzel bir anı olarak kaldı. :)

#and için: 
# 1 1 = 1
# 1 0 = 0
# 0 1 = 0
# 0 0 = 0

#or için:
# 1 1 = 1
# 1 0 = 1
# 0 1 = 1
# 0 0 = 0

if n1 > n2 and n1 > n3: 
    max_number = n1
elif n2 > n1 and n2 > n3:
    max_number = n2
elif n3 > n1 and n3 > n2:
    max_number = n3
else:
    print(f'The given numbers could be same.')
    exit()
print(f'The maximum number is : {max_number}')
