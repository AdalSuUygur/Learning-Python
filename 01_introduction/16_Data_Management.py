
#! DATA MANAGEMENT
# 1. HTTP Döngüsü (Pizzacı Analojisi): İstemci (Sen) ve Sunucu (Pizzacı) arasındaki o "kurallı konuşma".
# 2. JSON Yapısı (Koli Analojisi): Verilerin o "standart kutunun" içinde nasıl düzenli durduğunu hatırla.
# 3. API Mantığı (Garson Analojisi): Senin mutfağa girmene gerek kalmadan, garsonun (API) aradaki köprüyü nasıl kurduğu.

#! HTTP Protokolü:
#* Sen evdesin (**Client/İstemci**). Pizza yemek istiyorsun. Pizzacı dükkanı ise uzakta (**Server/Sunucu**).
#* Senin pizzacıya telefon açıp "Bana karışık pizza gönder" demen **Request (İstek)**'tir.
#* Pizzacının sana pizzayı kutulayıp göndermesi **Response (Cevap)**'tır.
#* HTTP ise, o telefon konuşmasının **kurallarıdır**.
#* "Önce merhaba de, sonra adresini ver, sonra siparişi söyle" gibi kurallar bütünüdür.
#* Eğer bu kurallar (Protokol) olmasaydı; sen Türkçe konuşurken pizzacı Çince konuşuyor olabilirdi ve pizza asla gelmezdi. 
#* Bütün web siteleri (Google, YouTube, Instagram) bu kurallar sayesinde, senin bilgisayarın hangi marka olursa olsun aynı şekilde açılır.
#? Yani HTTP Protokolü: Farklı dildeki istemlerin server tarafında anlaşılabilmesi için konulmuş kurallar bütünüdür.

#! JSON (Java Script Object Notation)
#* Diyelim ki evini taşıyorsun (Veri transferi).
#* Eşyalarını (Verilerini) kamyona rastgele atamazsın. Kırılır, kaybolur.
#* Hepsini standart kolilere (JSON) koyarsın. Üzerine ne olduğunu yazarsın.
#* Yeni eve gittiğinde kolileri açar, eşyaları tekrar yerleştirirsin.
#? Yani JSON: Verilerin internette seyahat ederken bozulmaması için konulduğu o standart, metin tabanlı kolidir.

#! API (Application Programming Interface)
#* API, iki farklı yazılımın birbiriyle konuşmasını sağlayan "Ortak Bağlantı Noktası"dır.
#* Restorandaki Garson gibidir: Sen (Client) mutfağa (Server) giremezsin. Siparişini (Request) garsona verirsin, o da sana yemeği (Response) getirir.
#* Elektrik Prizi gibidir: Duvarın arkasındaki (Backend) karmaşık kabloları bilmene gerek yoktur. Fişi prize takarsın ve çalışır.
#* Güvenliktir: Mutfağın sırlarını ve malzemelerini (Veritabanı) dışarıdan gelenlere karşı koruyan kapıdaki görevlidir.
#? Yani API: İki farklı yazılımın, birbirlerinin kodlarını veya çalışma şekillerini görmeden, sadece veri alışverişi yaparak anlaşmasını sağlayan köprüdür.

# Not: İlk kullanım amacı farklı programlama dillerinde yazılmış farklı ortamlarda çalışabilen uygulamaların birbirleriyle konuşması için idi.
# Ancak artık hayatımız mikro servisler girdi ve bununla birlikte her farklı bir özellik için farklı bir API kullanılıyor. 
# Mesela e-ticaret sitesindeki search için bir API, ödeme için bir API, kategoriler için API, mobil uygulama için APIler kullanılıyor.

#* Bütün paketler pypi.org sitesinde. Buradan requests adlı paket indirilecek.
#* Bir modül nasıl yüklenir?
# 1. pypi.org sitesine gidilerek ilgili modül aratılır.
# 2. modülün sitesinde isminin altında "copy to clipboard" seçeneği seçilir.
# 3. VS Code'da terminal açılır.
# 4. venv aktif olunup olunmadığı kontrol edilir. Aktifse; yapıştır ve paketi yükle.
# 5. venv aktif değilse terminale: .\venv\Scripts\activate yazmak gerekli. Aktif olduktan sonra yapıştır ve modülü yükle.
#* Not: Bu neden önemli? Çünkü modüller venv içerisine yüklenir.

from requests import get #request modülünden get fonksiyonunu kullanacağımız için bunu aldık.
from requests.exceptions import HTTPError, ConnectionError, Timeout, RequestException #her farklı modülün kendi exception sınıfları vardır
from pprint import pprint #güzel gözülmesi için

#todo var olan bir API ile işlemler
try: #Her API'nin bir endpointi vardır. Biz bu endpoint'e request atarız.
    end_point = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=d8aaaaadcc674ee181cd1457e811c0df"
    # NewsAPI'den aldığımız beleş API key'ini yapıştırıyoruz.

    response = get(end_point, timeout= 6000) # endpointten talepte bulunduk, 6 sn içinde yanıt gelmezse timeout olur dedik.

    data = response.json() #gelen yanıtı json'a dönüştürüyoruz.
    # pprint(data) #yazdırdık ve veriye ulaştık!

#* ilk makalenin yazarını ve title'ını ekrana basmak için:
    #region Kendi çözümüm
    # 1. adım: data'nın içine giriyoruz. Data bir sözlük yapısı. Data içerisindeki "articles" keyine gidiyorum.
    # data.get("articles")
    # 2. adım: Şu an elimde bir liste var. 
    # details for details in data.get("articles")
    # 3. adım: Listenin her elemanı bir sözlük. Yani details yazar ve makale detaylarını içeren bir sözlük.
    # details.get("author")
    # 4. adı: sözlüğün yazar isimli keyini aldım. Yey!

# Şimdi bunları toparlayalım ve tek satırda yazdıralım:
    # pprint(
    #     list(
    #         details.get("author") for details in data.get("articles")
    #     )
    # )

    #region Hocanın çözümü
    # print(
    #     f'Author: {data.get("articles")[0].get("author")}\n'
    #     #datanın articles keyine girdik
    #     #burası bir liste
    #     #listenin 0. indexindeki elemana eriştik
    #     #burası bir sözlük
    #     #sözlüğün yazarını aldık
    #     f'Title: {data.get("articles")[0].get("title")}\n'
    # )

    #todo ödev1
    #* End-User'dan alınan "author name"in makalelerini yazdıran uygulama
    #region Kendi çözümüm
    # author_name = input("Please enter the author's name: ").lower()
    # results = [details for details in data.get("articles") if details.get("author").lower() == author_name]
    # for result in results:
    #     pprint(result)
    
    #region Hocanın çözümü:
    # author_name = input('Author Name: ')
    # Path I
    # for article in data.get('articles'):
    #     if article.get('author') == author_name:
    #         pprint(article)
            
    # Path II
    # results = [article for article in data.get('articles') if article.get('author') == author_name]
    
    # for result in results:
    #     pprint(result)

except HTTPError as err: #alınan her hataya farklı cevaplar vermek için
    print(f"HTTP error: {err}")
except ConnectionError as err: #her bir hatayı ayrı ayrı yazabiliriz
    print(f"Connection error: {err}")
except (Timeout, RequestException) as err: #ya da hepsini böyle parantez içinde tek bir çıktıda yazabiliriz
    print(err)

#todo bulunan bir free API'den veri alalım bu da ikinci ödev
try:
    poke_name = input("Pokemon's name: ").lower()

    url = f"https://pokeapi.co/api/v2/pokemon/{poke_name}"
    print(f"{poke_name} aranıyor...")

    response_2 = get(url, timeout=5)
    data_2 = response_2.json()

    print(f'{data_2.get("name").upper()} YETENEKLERİ:')

    ability_names = [item.get('ability').get('name') for item in data_2.get('abilities')]
    pprint(ability_names)

except (HTTPError, ConnectionError, Timeout, RequestException) as err:
    pprint(err)

