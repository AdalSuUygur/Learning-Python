
# Barbut 2 zarla oynanır
# Büyük zar atan kazanır
# Zardaki en küçük değer 1 en büyük değer 6'dır.
# Minimum 2; maximum 12 atılabilir.

from random import randint, choice #random zar atılacağı için

# bots = ["elton", "adal", "ipek", "özlem", "mirza"]
# Choice fonksiyonu nedir, listedeki random bir elemanı seçer aslında, burdaki kullanım amacımız da şu
# rastgele bir rakip karşımıza geliyor, onu seçtiriyor bize.
# x = choice(bots) #test
# print(x) #test

users = {
    "1": {'user name': 'beast',
          'password': '123',
          'safe':2000
    },
    "2": {'user name': 'savage',
          'password': '987',
          'safe':2000
    },
        "3": {'user name': 'bear',
          'password': '456',
          'safe':2000
    }
}

easy_bots = ["elton", "adal", "ipek", "özlem", "mirza"]
hard_bots = ["burak", "sarah", "su"]

#* Task list: 

# Kullanıcıya günlük chip verilecek. 
def gain_daily_chips(x: int = 1000, y: int = 2000) -> int: #Kullanıcı, proje bağımsız, default olarak1000 - 2000 aralığında chip üreten program
    # Bu değerleri admin de özel günlere göre adjustlayabilir diye dinamik olarak ekledik.
    return randint(a=x,b=y)

# Rastgele bot kullanıcı seçimi
def select_bot_player(bots_type: list = easy_bots) -> str:
    return choice(bots_type)

#Minimum bet: 100 olsun
minimum_bet = 100
#minimum 100, en fazla max kasasındaki değer kadar girebilir.

def is_bet_valid(current_bet: int, safe: int) -> bool:
    if minimum_bet <= current_bet <= safe:
        return True
    else:
        return False
    
# Zar atma fonksiyonu
def roll_dice() -> int:
    return randint(a=2,b=12)

#Kullanıcının kasasının değerinin güncellenmesi
def update_safe(user:dict, chip_amount: int, status:str = "win") -> str: #kazandın veya kaybettin diye dönecek
    if status == "win":
        user.update({
            "safe": user.get("safe") + chip_amount
        })
        return f'You win! Your current safe is: {user.get("safe")}'
    
    elif status == "lose":
        user.update({
            "safe": user.get("safe") - chip_amount
        })
        return f'You lost :( your current safe is: {user.get("safe")}'

# print(update_safe(user=users.get("1"), chip_amount=200, status="win")) #test

def main():
    sign_user = users.get("1")

    gained_chip = gain_daily_chips()

    msg = update_safe(user=sign_user, chip_amount=gain_daily_chips)

    print(
        f"Welcome, {sign_user.get('user name')}\n"
        f"You've earned {gained_chip} amount of as your daily free chip!\n"
        f"{msg}"
    )

    while True:
        if sign_user.get("safe") >= minimum_bet:
            print(f"Opponent found! Beware of {select_bot_player()}!")

            bet = int(input("Please make a bet: "))

            if is_bet_valid(current_bet=bet, safe=sign_user.get("safe")):

                user_roll = roll_dice()
                bot_roll = roll_dice()

                if user_roll > bot_roll:
                    print(f"{update_safe(user=sign_user, chip_amount=bet, status='win')}")
                elif user_roll < bot_roll:
                    print(f"{update_safe(user=sign_user, chip_amount=bet, status='lose')}")


            else:
                print("Your bet is not valid.")

        else:
            print(f"Your safe is below the minimum bet amount. Your currency: {sign_user.get('safe')}")
            break

