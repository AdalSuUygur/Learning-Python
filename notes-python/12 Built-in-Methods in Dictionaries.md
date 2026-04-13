
# Sözlüklerde CRUD

Sözlükler, RAM üzerinde çalışan mini veritabanlarıdır. CRUD işlemleri syntax olarak çok benzerdir.

| CRUD | İşlem | Kod Örneği (`d` sözlüğü) | Açıklama |
| --- | --- | --- | --- |
| **C** | **Create** (Oluştur) | `d["yeni_anahtar"] = değer` | Olmayan bir anahtara değer atarsan **YARATILIR.** |
| **R** | **Read** (Oku) | `d["anahtar"]` `d.get("anahtar")` | Veriyi çağırırsın. `.get()` kullanmak daha güvenlidir. |
| **U** | **Update** (Güncelle) | `d["eski_anahtar"] = yeni` | Var olan bir anahtara değer atarsan **GÜNCELLENİR.** |
| **D** | **Delete** (Sil) | `d.pop("anahtar")` `del d["anahtar"]` | Anahtarı ve değerini uçurur. |

> **Dikkat Et:**
> **Create** ve **Update** işleminin yazımı AYNIDIR!
>
> * Anahtar yoksa -> Yaratır.
> * Anahtar varsa -> Ezer (Günceller).

```py
araba = {"marka": "Ford", "model": "Mustang"}

# 1. CREATE (Ekleme) - Yeni anahtar yaz, değer ata.
araba["yil"] = 1964 
# {'marka': 'Ford', 'model': 'Mustang', 'yil': 1964}

# 2. READ (Okuma) - İki yol var.
print(araba["marka"])       # Ford (Eğer 'marka' yoksa kod PATLAR!)
print(araba.get("renk"))    # None (Eğer 'renk' yoksa None döner, güvenlidir) ✅

# 3. UPDATE (Güncelleme) - Var olan anahtara yeni değer ata.
araba["yil"] = 2024
# Yıl artık 2024 oldu.

# 4. DELETE (Silme) - pop() metodu.
silinen_model = araba.pop("model") 
# 'model' silindi, değeri 'silinen_model'e atandı.
```

## Dictionary için Built-in-methods

Sözlüklerin kendine has çok güçlü metotları vardır.
Yeni bir item eklerken de: key - value olarak eklemek gerek sözlüğün yapısından dolayı

### Erişim Metotları (Güvenli Okuma)

* **`.get(key)`:** Anahtar varsa değeri getirir, **yoksa `None` döner.** (Programı patlatmaz, QA dostudur).
* **`.keys()`:** Sadece anahtarların listesini verir.
* **`.values()`:** Sadece değerlerin listesini verir.
* **`.items()`:** Hem anahtarı hem değeri ikili paketler (Tuple) halinde verir. (Döngüler için efsanedir).

### Veriye Ulaşma (Köşeli Parantez vs .get())

* Köşeli Parantez `[]` (Riskli Yol):

Eğer anahtar varsa getirir, **yoksa programı PATLATIR (KeyError).**

```py
print(sozluk["marka"]) # Çıktı: Ford
# print(sozluk["renk"]) # HATA! KeyError: 'renk'

```

* `.get()` Metodu (Güvenli Yol - Tavsiye Edilen)

Eğer anahtar varsa getirir, **yoksa `None` döner (Program çökmez).**

```py
print(sozluk.get("model")) # Çıktı: Mustang
print(sozluk.get("renk"))  # Çıktı: None (Hata yok, temiz iş)

```

> **Not:** Veri temizlerken binlerce satırla uğraşacaksın. Bazı satırlarda veri eksik olabilir. `.get()` kullanmazsan kodun sürekli patlar.

## Güncelleme Metotları

* **`.update({yeni_veri})`:** Sözlüğe başka bir sözlüğü yapıştırır. Varsa günceller, yoksa ekler.
* **`.setdefault(key, value)`:** "Eğer bu anahtar varsa elleme, yoksa bu değeri ata."

## Silme Metotları

* **`.pop(key)`:** Anahtarı siler ve değerini sana geri verir (Listelerdeki gibi).
* **`.popitem()`:** Son eklenen öğeyi siler (Python 3.7+).
* **`.clear()`:** İçini komple boşaltır.

## Sözlüklerde Gezinmek (Looping)

```py
kisi = {"ad": "Ali", "yas": 25}

# Sadece Anahtarlar (Keys)
for k in kisi.keys():
    print(k) # ad, yas

# Sadece Değerler (Values)
for v in kisi.values():
    print(v) # Ali, 25

# İkisi Bir Arada (En Çok Kullanılan - Unpacking)
for k, v in kisi.items():
    print(f"Anahtar: {k} --- Değer: {v}")

```
