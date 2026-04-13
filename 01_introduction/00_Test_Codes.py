
a = [1, 2, 2, 2, 3]
b = [2]

#     c = []
    
#     for item in a_clean:
#         item for item in a_clean if item not in b_clean
    
#     lst_includes_a = [fruit for fruit in fruits if "a" in fruit.lower()] #fruit.lower() yazmamızın sebebi de içinde küçük a harfine bakıyor olmamız.

#     for item in a_clean 
    
    
    
    
    
#     == (item in b_clean):
#         continue
#     else:
#         c.append(item)
        
    
print([item for item in a if item not in b])



# #todo Filtreleme uygulaması
# #* Kullanıcıdan aradığı ürünün adını, fiyat aralığını, stokta olanları gösterip gösterilmeyeceği bilgilerini girdikten sonra gelen sonuçları ekrana yazdıralım.
# products = [
#     {'name': 'Lenovo X1 Carbon', 'price': 110_000, 'stock': 12},
#     {'name': 'Lenovo Thinkpad', 'price': 89_000, 'stock': 7},
#     {'name': 'Macbook Pro', 'price': 89_000, 'stock': 3},
#     {'name': 'Macbook Air', 'price': 125_000, 'stock': 5},
#     {'name': 'Asus Zenbook', 'price': 150_000, 'stock': 4},
#     {'name': 'Monster Huma', 'price': 55_000, 'stock': 18},
#     {'name': 'Monster Alba', 'price': None, 'stock': 0},
#     {'name': "Monster Abra", 'price': 72_000, 'stock': 0},
#     {'name': "Monster Tulpar", 'price': 104_000, 'stock': 3},
#     {'name': "Monster Semruk", 'price': 243_000, 'stock': 14},
#     {'name': "MSI Katana 17", 'price': 73_000, 'stock': 5}
# ]

# def filter_by_name(product: dict, filter: str) -> list:
    



# def get_clean_data(data: list) -> list: #gelen listede ismi veya priceı none olanları eledik
#     """Adı veya Fiyatı None olanları eler."""
#     # FAZ 6: List Comprehension kullanımı
#     return [p for p in data if p.get("name") is not None and p.get("price") is not None]
# print(get_clean_data(products))

# # --- FİLTRELER ---
# def filter_by_criteria(data: list, name_search: str, min_p: float, max_p: float) -> list:
#     """İsim ve Fiyat aralığına göre filtreler"""
#     return [
#         p for p in data 
#         if name_search.lower() in p["name"].lower() # İsim kontrolü
#         and min_p <= p["price"] <= max_p           # Fiyat kontrolü
#     ]


# # --- FAZ 4 & 5: GÜVENLİ INPUT FONKSİYONU ---
# def get_safe_float(prompt: str, default_value: float) -> float:
#     """
#     Kullanıcıdan sayı ister.
#     - Boş geçerse -> Default değeri döner.
#     - Harf girerse -> Hata vermez, uyarır ve Default değeri döner.
#     """
#     raw_data = input(prompt)
#     if not raw_data: # Kullanıcı hiçbir şey yazıp enter'a bastıysa
#         return default_value
    
#     try:
#         return float(raw_data)
#     except ValueError:
#         print(f"⚠️ Hatalı giriş! Varsayılan değer ({default_value}) kullanılıyor.")
#         return default_value

# # --- FAZ 3: STOK MANTIĞI ---
# def apply_stock_filter(data: list, only_in_stock: bool) -> list:
#     """
#     only_in_stock True ise: Sadece stoku > 0 olanları getir.
#     only_in_stock False ise: Hepsini getir (stok 0 olsa bile).
#     """
#     if not only_in_stock:
#         return data # Filtreleme yapma, hepsini gönder
    
#     return [p for p in data if p["stock"] > 0]


# # --- ANA PROGRAM (MAIN) ---
# def main():
#     print("--- ÜRÜN FİLTRELEME SİSTEMİ V1.0 ---")
    
#     # 1. Adım: Temiz Veriyi Hazırla
#     # Senin "beceremedim" dediğin yer burasıydı. Temiz veriyi bir değişkene alıyoruz.
#     clean_products = get_clean_data(products) 
    
#     # 2. Adım: Kullanıcıdan Verileri Güvenli Al (Faz 4-5)
#     aranan_isim = input("Aranan ürün adı (Hepsi için Enter): ").strip()
#     min_fiyat = get_safe_float("Min Fiyat (Varsayılan 0): ", 0.0)
#     max_fiyat = get_safe_float("Max Fiyat (Varsayılan 500.000): ", 500000.0)
    
#     stok_sorusu = input("Sadece stokta olanları mı göstereyim? (E/H): ").lower()
#     sadece_stoktakiler = True if stok_sorusu == 'e' else False

#     # 3. Adım: Filtreleri Uygula (Pipeline)
#     # Temiz listeden -> İsim/Fiyat Filtresine
#     filtered_list = filter_by_criteria(clean_products, aranan_isim, min_fiyat, max_fiyat)
    
#     # Kalan listeden -> Stok Filtresine
#     final_result = apply_stock_filter(filtered_list, sadece_stoktakiler)

#     # 4. Adım: Sonuçları Yazdır
#     print(f"\n🔍 Bulunan Ürün Sayısı: {len(final_result)}")
#     if not final_result:
#         print("😔 Kriterlere uygun ürün bulunamadı.")
#     else:
#         for urun in final_result:
#             durum = "✅ Stokta" if urun['stock'] > 0 else "❌ Tükendi"
#             print(f"- {urun['name']:<20} | {urun['price']:,.0f} TL | {durum}")

# # Programı Başlat
# main()

# #hoca da stock durumunu çözemedi, stock true gelirse stoğu 0 olmayanları gösterme, stock false gelirse stoğu sıfır olsa da göster anlamına geliyor

# #faz 3: stok durumunu çözdükten sonra, try excepte gerek var mı, varsa neden gerek var? ne olabilir burda? çöz.

# #faz4: bunları input yapsaydık, yani get data içine yazdıklarımızı, kullanıcı yanlışlıkla string girerse ne olur?

# #faz 5: kullancıı değer girmeyi atlarsa ne olacak?
