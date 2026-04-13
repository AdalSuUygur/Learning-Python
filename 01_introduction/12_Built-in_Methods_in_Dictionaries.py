
#todo Güvenli Veri Çekme
#* Durum: Bir web sitesinin ayarlarını tutan bir sözlük var. Ancak bazı kullanıcılar tüm ayarları seçmemiş.
#* 1. Kullanıcının "tema"sını ekrana bas.
#* 2. Kullanıcının "dil" ayarını ekrana bas.
ayarlar = {"tema": "dark", "ses": 50} # (Dikkat: "dil" ayarı yok!)

print(ayarlar["tema"])

ayarlar["dil"] = "TR"
print(ayarlar["dil"])

#todo Profil Birleştirme
#* Elinde iki yarım sözlük var.
#* `ana_profil` sözlüğünü güncelle. `ek_bilgi` içindeki her şeyi `ana_profil`in içine tek hamlede yapıştır.
#* **Dikkat:** İkisinde de "rol" var. Hangisi kazanacak? Sonucu tahmin et.

ana_profil = {"ad": "Su", "rol": "Admin"}
ek_bilgi = {"sehir": "İstanbul", "yas": 25, "rol": "SuperAdmin"}

print(ana_profil | ek_bilgi)
