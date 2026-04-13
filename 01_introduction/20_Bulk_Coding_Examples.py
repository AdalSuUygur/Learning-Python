
#todo ATM uygulaması

adal_account = {
    "account no": "123456",
    "password": "123",
    "balance": 2000,
    "additional balance": 1000
}

yasemin_account = {
    "account no": "425789",
    "password": "456",
    "balance": 3000,
    "additional balance": 1000
}

sarah_account = {
    "account no": "369874",
    "password": "789",
    "balance": 4000,
    "additional balance": 1000
}

habiba_account = {
    "account no": "123654",
    "password": "963",
    "balance": 5000,
    "additional balance": 1000
}

users = [adal_account, sarah_account, habiba_account, yasemin_account]

#region para çekme algoritması:
#* 1. balance, amount büyükse zaten parasını çekebiliyor
#* 2. balance, amount karşılamazsa:
#* 2.1. ek hesabın devreye girsin mi?
#* 2.1.1. Evet derse para ek hesaptan alınacak
#* 2.1.1.1. Bütün parası amount karşılıyor mu?
#* 2.1.2. Hayır derse işlem iptal edilecek

#* İskelet yapımız:
#? İlk yazılan kod bloğu (1)
# def withdraw_money(account: dict, amount: int):
#     if account.get("balance") >= amount:
#         account["balance"] -= amount
#         print("Paranız çekiliyor.")
#     else:
#         pass #diğer seçenekler devreye girecek.

#? ikinci geliştirme sonucu yazılan kod bloğu (2) ve (2.1.1.1)
# total_balance = account.get("balance") + account.get("additional balance")

# if total_balance >= amount:
#     pass
# else:
#     print(
#         "yetersiz bakiye byyyyyy"
#     )

#? üçüncü geliştirme sonucu yazılan kod bloğu (2.1)
# use_additional_balance = input("Yetersiz bakiye, ek hesap bakiyesini kullanmak ister misiniz? (Y/N): ") #daha sonra guard yazacağımız için lower falan yapmadık.
# match use_additional_balance:
#     case "y":
#         pass
#     case "n":
#         print("Transaction has been calcelled.")

#? dördüncü geliştirme sonucu yazılan kod bloğu (2.1.1)
# detach_amount = amount - account["balance"] #ek hesaptan düşürülecek miktar
# account["balance"] = 0
# account["additional balance"] -= detach_amount

#? beşinci geliştirme sonucu yazılan kod bloğu (Kullanıcının inputta restrict edilmesi için geliştirilecek olan guard)
#* bu tarz kullanıcıyı strict ettirilen fonksiyonlara utilities denir

# def get_valid_answer(question: str, valid_options: tuple) -> str: #Kullanıcıdan doğru yanıtı alma; soruyu ve seçenekleri aldık ve string dönüşlü olacak şekilde tanımladık.
# # Amaç: Bana opsiyonları olan hangi soru gelirse gelsin question'ı ve options'ları birleştirip kullanıcıya gösterdiğim bir fonksiyon 
# # (aslında amacımız input fonksiyonu içinde yazılan açıklamayı düzgün şekilde yaratmak ve kullanıcıyı strictlemek.)
#     question += f' ({", ".join(valid_options)}): ' #virgüllerle birleştir, kimi? valid_options adlı parametreleri yani question ile birlikte optionları da yazdık.

#     response = input(question) #kullanıcıdan gelen cevap 
#     while response.lower().strip() not in valid_options: #Eğer kullanıcı valid answer dışında bir yanıt girdiyse
#         print("Please type a valid option.") #Dedik ki, gardaş dur orda
#         response = input(question) #hop tekrar istedik inputu
    
#     return response #ne zaman kullanıcı valid answer girer o zaman döngüden çıkar ve biz de girdiyi artık döndürürüz.

#     return question satırı ile test aşaması, doğru yazdık mı diye.
# print(get_valid_answer(
#     question="Do you want to use additional balance?",
#     valid_options=("y", "n")
# ))

#? altıncı geliştirme sonucu yazılan kod bloğu (guard'ı kullanma)
# use_additional_balance = get_valid_answer(
#                         question="Do you want to use additional balance?",
#                         valid_options=("y", "n"))

#? yedinci geliştirme sonucu yazılan kod bloğu (süsleme, account bilgilerini verelim)
# def account_information(account: dict):
#     print(
#         f"Account No: {account["account no"]}\n"
#         f"Balance: {account["balance"]}\n"
#         f"Additional Balance: {account["additional balance"]}"
#     )
#endregion

#! HADİ HEPSİNİ BİRLEŞTİRİP SÜSLEYELİM

def withdraw_money(account: dict, amount: int):
    if account.get("balance") >= amount:
        account["balance"] -= amount
        account_information(account=account)
    else:
        total_balance = account.get("balance") + account.get("additional balance")

        if total_balance >= amount:
            use_additional_balance = get_valid_answer(question="Do you want to use additional balance?",valid_options=("y", "n"))
            match use_additional_balance:
                case "y":
                    detach_amount = amount - account["balance"] #ek hesaptan düşürülecek miktar
                    account["balance"] = 0
                    account["additional balance"] -= detach_amount
                    account_information(account=account)
                case "n":
                    print("Transaction has been calcelled.")
                    account_information(account=account)
        else:
            print(
                "Insufficient balance, transaction has been cancelled."
            )
            account_information(account=account)

def get_valid_answer(question: str, valid_options: tuple) -> str: 
    question += f' ({", ".join(valid_options)}): ' #virgüllerle birleştir, kimi? valid_options adlı parametreleri yani question ile birlikte optionları da yazdık.

    response = input(question) #kullanıcıdan gelen cevap 
    while response.lower().strip() not in valid_options: #Eğer kullanıcı valid answer dışında bir yanıt girdiyse
        print("Please type a valid option.")
        response = input(question) #hop tekrar istedik inputu
    
    return response #ne zaman kullanıcı valid answer girer o zaman döngüden çıkar ve biz de girdiyi artık döndürürüz.

def account_information(account: dict):
    print(
        f"Account No: {account['account no']}\n"
        f"Balance: {account['balance']}\n"
        f"Additional Balance: {account['additional balance']}"
    )

#testing aşaması
# Case 1: Paramızın yettiği senaryo
# withdraw_money(account=adal_account, amount=1000)
# Case 2: Additional hesaptan para çektiğimiz senaryo
# withdraw_money(account=adal_account, amount=2999)
# Case 3: Her türlü paramızın yetmediği senaryo
# withdraw_money(account=adal_account, amount=3500)

#? Burası da para yatıracağımız senaryo :)
#dışarda bir ek balance için default değer tanımlaması gerek bence
default_additional_balance = 1000

#region hocanın çözümü
#* (TRY1) ve negatif balance gördük.
# def deposit_money(account: dict, amount: int):
#     if account["additional balance"] < default_additional_balance: #ek hesap default değerinde mi diye sorduk
#         account["balance"] += amount #gelen tüm parayı balancea yatırdık
#         short = default_additional_balance - account["additional balance"] #eksik olan meblağ hesabını yaptık
#         if account["balance"] >= short:
#             account["balance"] -= short
#             account["additional balance"] += short
#         else:
#             account["balance"] -= amount
#             account["additional balance"] += amount
#         account_information(account=account)

#* Bu da fixed hali (TRY2)
def deposit_money(account: dict, amount: int, transaction_name: str = "owner"):
    short = 1000 - account['additional balance']
    if amount >= short:
        kalan = amount - short
        account['additional balance'] += short
        account['balance'] += kalan
    else:
        account['additional balance'] += amount
    if transaction_name == "owner":
        account_information(account=account)
#endregion

#region Kendi çözümüm ancak gemini beğenmedi ki bence de big o notation kısmına uymadı.
# def deposit_money(account: dict, amount: int):
#     if account["additional balance"] < default_additional_balance:
#         for i in range(1, amount+1, 1):
#             if account["additional balance"] < default_additional_balance:
#                 account["additional balance"] += 1
#             else:
#                 account["balance"] += 1
#         account_information(account=account)
#     else:
#         account["balance"] += amount
#         account_information(account=account)
#endregion

#region gemini çözümü ama anlamadım
# def deposit_money(account: dict, amount: int):
    # # 1. Ek bakiyenin dolması için ne kadar lazım?
    # short = default_additional_balance - account["additional balance"]

    # # 2. Elimizdeki paradan ne kadarını buraya aktarabiliriz?
    # # (Ya eksiğin tamamını veririz ya da elimizde ne kadar varsa o kadarını)
    # eklenecek_ek_bakiye = min(amount, max(0, short))

    # # 3. Geri kalan her şeyi ana bakiyeye at
    # eklenecek_ana_bakiye = amount - eklenecek_ek_bakiye

    # # ŞİMDİ GÜNCELLEYELİM:
    # account["additional balance"] += eklenecek_ek_bakiye
    # account["balance"] += eklenecek_ana_bakiye

    # account_information(account=account)
#endregion

#testing 2 aşaması
# deposit_money(adal_account, 367)
# deposit_money(adal_account, 3435)

#? EFT işlemleri için yazılacak fonksiyon
# Para yollama işlemleri için yazılacak fonksiyon

# First try, burada aslında para gönderme işlemini yaptık, ancak sonucunda giden paranın hesap bilgileri de göndericiye gösteriliyor olacak
def eft(account: dict, receiver_no: str, amount: int) -> None:
    withdraw_money(account=account, amount=amount)

    for user in users:
        if user.get("account no") == receiver_no:
            deposit_money(account=user, amount=amount, )

# eft(account=adal_account, receiver_no="369874", amount=1500) #bu aşamadan yolladığımın hesabın tüm bilgilerini ben yollayıcı olarak görüyorum. Görmemem gerek.
# Peki neden görüyorum? Çünkü içerde parayı deposit ile yani hali hazırda var olan bir fonksiyonla aslında yatırdım
# ilk önce gönderici hesaptaki parayı çektim (withdraw fonksiyonu ile) ve alıcı hesaba bu parayı yatırdım (deposit fonksiyonu ile)
# ancak deposit fonksiyonu içerisinde account informationları bastırıyor bu yüzden de gönderici de bu fonksiyondaki printleri görüyor.

#* Peki nasıl çözebiliriz?
# Basit düşün, deposit_money fonskiyonuna gidip transaction name adında bir parametre verip defaultunu owner yaparsak sorunumuz çözülür.

# def deposit_money(account: dict, amount: int, transaction_name: str = "owner"):
#     ...
#     ...
#     ...
#     if transaction_name == "owner": #transaction name
#         account_information(account=account)

# def eft...
#     ...
#     ...
#     ...
#             deposit_money(account=user, amount=amount, transaction_name="eft") #Ve burdaki minik düzeltme ile

# depositte eklediğimiz tek satır ve eftdeki fix ile sorun çözüldü.

#region EFT Çözüm 2
# def eft(account: dict, receiver_no: str, amount: int) -> None:
#     withdraw_money(account=account, amount=amount)

#     finded_user = [user for user in users if user.get("account no") == receiver_no]
#     deposit_money(account=finded_user[0], amount=amount, transaction_name="eft")
#endregion

# testing 3 aşaması
# eft(account=adal_account, receiver_no="369874", amount=1000)

#? Login aşaması!!!

def login(account_no: str, password: str) -> dict:
    for user in users:
        if user.get("account no") == account_no and user.get("password") == password:
            return user
    
    return None

#testing 4 aşaması
# print(login(account_no=369874,password="789"))

def main():
    counter = 3
    while counter > 0:
        login_account = login(
            account_no=input("Account no: "),
            password=input("Password: "))

        if login_account is not None:
            print(f"Welcome to the jungle.")

            while True:
                transaction_no = input("Transaction No: ")
                
                match transaction_no:
                    case "1":
                        withdraw_money(
                            account=login_account, 
                            amount=int(input("Amount: ")))
                    case "2":
                        deposit_money(
                            account=login_account, 
                            amount=int(input("Amount: ")))
                    case "3":
                        eft(
                            account=login_account,
                            receiver_no=input("Receiver no: "),
                            amount=int(input("Amount: ")))
                    case _:
                        print("Please enter the valid transaction number.")

        else:
            print("Invalid credentials.")
            counter -= 1
    print("Hesabınız kilitlendi since you've reached maximum amount of tries.")

main()

# #endregion
