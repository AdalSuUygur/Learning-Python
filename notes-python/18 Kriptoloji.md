
# (Cryptography) CRYPTOGRAPHY (Kriptoloji)

Kriptoloji, en basit tabiriyle **"Veriyi Saklama Bilimi"**dir.

> **Amaç:** Bir veriyi, sadece anahtarı (şifresi) olan kişinin okuyabileceği, anahtarı olmayanın ise "anlamsız karakter yığını" olarak göreceği bir hale getirmektir.

* **Plaintext (Düz Metin):** Şifrelenmemiş veri. (Örn: "Adal Su")
* **Ciphertext (Şifreli Metin):** Şifrelenmiş veri. (Örn: `b'\x8e\xa4\x12...'`)

> **Neden Kullanılır?** Bir mektup yazdığını düşün. Bunu şeffaf bir dosyaya koyarsan (Plaintext) taşıyan kurye de okur, postacı da okur. Ama bunu kilitli bir çelik kasaya koyarsan (Ciphertext), sadece anahtarı olan alıcı okuyabilir. Dijital dünyada bu kasa **Kriptoloji**dir.

## File Encryption (Neden dosyalar şifrelenir?)

> **Hassas Veri (Sensitive Data):** Diyelim ki programın hata verdi ve hatanın içinde kullanıcının gizli bilgileri var. Bunlar düz metin olarak kaydedildiklerinde, herhangi bir sızmada kötü niyetli insanların eline geçer.

* **Ancak** şifreli kaydedildiyse dosyalar sızsa bile içindeki bilgiler erişilemez veya süreç alır.

> **KVKK / GDPR (Yasal Zorunluluk):** Kişisel verileri (TC kimlik, sağlık bilgisi) düz metin olarak saklamak suçtur. Mecburi şifreleme :)

## Özetle

1. **Kriptoloji:** Veriyi kilitli kasaya koymaktır.
2. **File Encryption:** O kasayı dosya sistemine kaydetmektir. Hacker dosyayı çalsa bile içini göremez.
3. **Örnekte:** "Hatalı e-mail girildiğinde, bu durumu şifreleyerek dosyaya not düş" diyor. Böylece log dosyasına bakan birisi, sistemin verdiği kritik hata mesajlarını açıkça okuyamıyor.
