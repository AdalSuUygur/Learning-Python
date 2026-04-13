
#! Dosyadan veri okuma ve şifreleri kendi not defterimize kriptolama

#region File I/O Modülü

#? File I/O Modülü
# Bu modül dosya açma/kapama/okuma/veri yazma/silme için kullanılan bir yapı
# Veritabanı varken tercih edilmez ancak uygulama amaçlı şimdilik çekiyoruz.

#* OS --> Oparating System

# #region Dosya Açma ve İçerisine Bilgi Yazma
# try:
#     file = open(file='new_file.txt', mode='w', encoding='utf-8') #Yaratıcı dosyaya isim verdik, mode verdik (yazma amaçlı ondan write'in w'si)
#     # Burdaki encoding de TR karakterlere duyarlı olması için
#     file.write('Name: Adal Su\nOccupation: Developer\n') #Yazdırdık
#     file.close()
# except FileExistsError as err: #Kendine has exceptionları
#     print(err)
# except FileNotFoundError as err:
#     print(err)
# #* Bu işlem sonucunda "new_file.txt" adında bir dosya SKILLEDHUB_3 Workspaceine eklenecek ve içerisinde Adal Su Developer yazılmış olacak.
# #* Hali hazırda aynı isimde bir dosya varsa tekrar yaratmaz.
# #endregion

# #region Dosya Yeni Bilgi Yazma
# try:
#     file = open(file='new_file.txt', mode='a', encoding='utf-8') # append'in a'sını seçtik mode olarak.
#     file.write('Full Name: İpek Yılmaz\nOccupation: Art Historian\n')
#     file.close()
# except FileExistsError as err:
#     print(err)
# except FileNotFoundError as err:
#     print(err)
# #endregion

# #region Dosyadan Veri Okuma
# try:
#     file = open(file='new_file.txt', mode='r', encoding='utf-8') #mode'umuz read kelimesinin r'si.
#     for line in file.readlines():
#         print(line)
#     file.close()
# except FileExistsError as err:
#     print(err)
# except FileNotFoundError as err:
#     print(err)
# #endregion

# #* Open'ın ikinci bir şekilde açılması, bunda ayrıca dosyayı kapatmaya gerek duymuyor (RAM efficiency)
# with open(file='new_file.txt', mode='a', encoding='utf-8') as file:
#     file.write('Full Name: Hakan Yılmaz\nOccupation: Chemist\n')

#endregion

#region Crypto Modülü

from socket import gethostbyname, gethostname
from datetime import datetime #Hatanın alınma tarihi için
from Crypto.Cipher import AES #AES: Kriptolama modülü
from Crypto.Random import get_random_bytes

def sys_log(**kwargs) -> str: #System log adlı aslında bir fonksiyon yazıyoruz


    try: #kullanıcı email adresini girerken @ olmasın ve burada da exception oluşsun.
        if '@' not in kwargs.get('email_address'):
            raise ValueError('Invalid email address..!') #ValueError verdirttik
        return 'Your email address is valid..!' #Bu da düzgün girilen e-mail adresi için
    

    except ValueError as err:
        aes_key = get_random_bytes(16) #16 bitlik bir key oluşturdum.
        aes_obj = AES.new(key=aes_key, mode=AES.MODE_EAX) #AES objesi yaratıyorum ki içerisindeki algoritma türlerinden yararlanabileyim
        #Key olarak şimdi yazdırdığımız keyi, mode olarak ise random bi tane seçtik


        chipper_text = aes_obj.encrypt(b'valueerrorhappen') #chipper_text ecript edilmiş hali yani kriptolanmış hali olacak.
        #Burda dedik ki byte byte yani karakter karakter value error happened


        with open(file=kwargs.get('file'), mode='a', encoding='utf-8') as file: #file açıyoruz
            file.write(str(chipper_text)) #kriptolanmış metni yazdık
            file.write(' || ') #süs amaçlı
            file.write(f'Machine Name: {kwargs.get("machine_name")}') #farklı bilgiler
            file.write(' || ') #araya cızırtı sokuyoruz
            file.write(f'IP Address: {kwargs.get("ip_address")}')
            file.write(' || ')
            file.write(f'Exception Date: {kwargs.get("exception_date")}')
        return f'{err}'


print(
    sys_log(
        file='log.txt', #bir file name göndereceğiz
        machine_name=gethostname(), #makinamızın ismi
        ip_address=gethostbyname(gethostname()), #ip adresimiz
        exception_date=datetime.now(), #bu şuanki zaman
        email_address='qwe.qwezxc.com' #içerisinde @ olmayan email adress :D
    )
)

#endregion
