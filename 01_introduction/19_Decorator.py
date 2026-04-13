
#! Decorator
#* Var olan fonksiyonun ham hali iş yapıyorsa decorator ile süslemiş oluruz.
#* Araba düşün, paketsiz hali de var, full paket hali de var, arada devasa bir fiyat farkı var, ancak amaçları aynı. 
#* İşte bu paketli halindeki sensördür, popo ısıtmasıdır falan hepsi aslında decorator.

#? SYNTAX

# 1. Adım: Aynı fonksiyon tanımlar gibi decorator tanımlanır, ancak içerisine parametre olarak fonksiyon verilir.
def my_decorator(func):
    # 2. Adım: İçerisinde wrapper (hediye paketi :D) adlı iç fonksiyon olur. 
    def wrapper():

        print('Bazı işler burada çalıaşcak..!') #* Ara adım: Fonksiyon verilmeden önce çalışacak kod bloğu. Aslında süsleme kısmı

        # 3. Adım: Bu wrapper adlı fonksiyonun içerisinde argümanı verilen fonksiyon execute edilir.
        func()

        print('belki bazı işlerde burada çalışacak..!') #* Ara adım: Fonksiyon çağrıldıktan sonra çalışacak kod bloğu. Aslında süsleme kısmı
    
    # 4. Adım return wrapper denilir.
    return wrapper

#* Not: wrapper execute edilmez, define edilir ve standby olarak beklemesi için return wrapper dedik.

# 5. Adım: Kullanımı yazılan bir fonksiyonun başına "@" ifadesi ile decorator çağrılır.
@my_decorator
def hello():
    print('Merhaba')

hello()

#region Examples

#todo Matematiksel işlem bloğunda decorator kullanımı uygulaması
# from math import pow, factorial
# from time import time_ns

# def calculate_time_execution(func):
#     def wrapper(*args, **kwargs):
#         start_time = time_ns()
#         func(*args, **kwargs)
#         end_time = time_ns()
#         print(f'Perfomace: {end_time - start_time} ns')
    
#     return wrapper

# @calculate_time_execution
# def calculate_pow(x: int, y: int):
#     print(f'Sonuç: {pow(x, y)}')

# @calculate_time_execution
# def calculate_factorial(number: int):
#     print(f'Sonuç: {factorial(number)}')

# @calculate_time_execution
# def sum_number(x: int, y: int, z: int):
#     print(f'Sonuç: {x + y + z}')

# calculate_pow(x=2, y=3)
# calculate_factorial(number=5)
# sum_number(x=1, y=2, z=3)

#* Burada 3 tane farklı iş yapan fonksiyon görüyoruz. 
#* Bunların her birisinin çalışma süresini hesaplamak için teker teker fonksiyon yazılmak yerine decorator ile tüm hepsinde hesaplanabilir.

#todo Verilen fonksiyonun execute edildi an ve logun verilmesi ile alakalı decorator yazılması
# from datetime import datetime

# def log_info(func):
#     def wrapper(*args, **kwargs):
#         print(
#             '===============================\n'
#             f'Yapılan İşlem: {func.__name__}\n'
#             f'İşlem Tarihi: {datetime.now()}\n'
#         )
#         return func(*args, **kwargs)
#     return wrapper

# @log_info
# def para_cekme(hesap_no: str, bakiye: int, cekilecek_tutar: int):
#     bakiye -= cekilecek_tutar
#     return (
#         f'Bu {hesap_no}, para çekildi.\n'
#         f'Güncel Bakiye: {bakiye}'
#     )

# print(
#     para_cekme(
#         hesap_no="123456789",
#         bakiye=1000,
#         cekilecek_tutar=500
#     )
# )

# #* Aynı işlemi para yatırma için de yapalım:

# @log_info
# def para_yatırma(hesap_no: str, bakiye: int, yatırılacak_tutar: int):
#     bakiye += yatırılacak_tutar
#     return (
#         f'Bu {hesap_no}, para yatırıldı..!\n'
#         f'Güncel Bakiye: {bakiye}'
#     )

# print(
#     para_yatırma(
#         hesap_no='1234456',
#         bakiye=1000,
#         yatırılacak_tutar=500
#     )
# )

#todo Verilen userların yetkilerine göre raporu görüntüleyebilme uygulaması
# def is_manager(func):
#     def wrapper(user):
#         if user.get('role') in ['manager', 'general manager']:
#             return func(user)
#         else:
#             print(f'{user.get("username")} - {user.get("role")}\nRaporu görüntüleme yetkiniz bulunmamaktadır..!')
#     return wrapper

# @is_manager
# def get_report(user):
#     print(f'{user.get("username")} - {user.get("role")}\nReport görüntülendi..!')

# user_1 = {
#     'username': 'Hasan Cobanoğlu',
#     'role': 'manager'
# }

# user_2 = {
#     'username': 'Rana Nur Ceylan',
#     'role': 'general manager'
# }

# user_3 = {
#     'username': 'Burak Yılmaz',
#     'role': 'Irgat'
# }

# get_report(user_1)
# get_report(user_3)
# get_report(user_2)

#todo Senaryo: Gizli bir raporu okuyan fonksiyonumuz var. Ama herkes okuyamasın, sadece yetkili olan okusun.
# # 1. DECORATOR FONKSİYONU
# def yetki_kontrol(hedef_fonksiyon):
    
#     # 2. WRAPPER (SARMA) FONKSİYONU (İÇ KATMAN)
#     def wrapper(*args, **kwargs): # args ve kwargs sayesinde her fonksiyona uyar!
        
#         print("--- Güvenlik Kontrolü Yapılıyor... ---")
#         kullanici = "admin" # (Burada normalde veritabanına bakılır)
        
#         if kullanici == "admin":
#             # Yetki varsa, asıl fonksiyonu çalıştır:
#             return hedef_fonksiyon(*args, **kwargs)
#         else:
#             print("HATA: Yetkiniz yok! Giremezsiniz.")
            
#     # 3. Wrapper'ı geri döndür (Paketlenmiş hali)
#     return wrapper

# # --- KULLANIM ---
# @yetki_kontrol
# def gizli_raporu_oku():
#     print(">> Çok gizli devlet sırları burada yazıyor...")

# @yetki_kontrol
# def fuzeleri_firlat():
#     print(">> Füzeler fırlatıldı! 🚀")

# # --- TEST ---
# gizli_raporu_oku()
# print("\n")
# fuzeleri_firlat()

#endregion
