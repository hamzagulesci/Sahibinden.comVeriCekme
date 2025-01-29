Sahibinden.com Veri Çekme Aracı
Bu proje Hamza Güleşci tarafından geliştirilmiştir. Bu araç, sahibinden.com üzerinde yapılan arama sonuçlarını kolayca toplamak ve bunları Excel veya TXT formatına dönüştürmek amacıyla hazırlanmıştır.
Kod yalnızca eğitim amaçlı yazılmıştır ve verilerin organize edilmesine yardımcı olmak için tasarlanmıştır.

📋 Özellikler
* Ürün adları, fiyatları, konum bilgileri ve linklerini toplar.
* Ürünlerin kapak resimlerini indirip Excel dosyasına ekler (opsiyonel).
* Veriler TXT veya Excel formatında kaydedilebilir.
* Sayfa sayısı sınırlaması olmaksızın çok sayıda ürün verisi toplayabilir.

🚀 Kurulum ve Kullanım: Gerekli Adımlar

1️⃣ ChromeDriver Yolu Ayarı
Kod içindeki driver_path değişkenine, sisteminizde yüklü olan ChromeDriver'ın tam dosya yolunu ekleyin.
Örnek: 
driver_path = "C:\\Users\\PC\\Desktop\\SahibindenVeriCekme\\chromedriver-win64\\chromedriver.exe"

**ÖNEMLİ**   
ChromeDriver'ı bu linkten sizin kendi chrome tarayıcınızın sürümüyle aynı olmalı ya da yakın olmalı!
https://googlechromelabs.github.io/chrome-for-testing/

2️⃣ Arama URL'si Hazırlığı
Sahibinden.com üzerinde arama yapın.
Sayfa görüntüleme boyutunu 50 olarak ayarlayın.
Tarayıcınızdaki URL'yi kopyalayın ve program size sorduğunda terminale yapıştırın.

3️⃣ Kütüphane Gereksinimleri
Bu kodun çalışması için aşağıdaki Python kütüphanelerini yüklemeniz gerekir:

* Selenium
* Requests
* Pillow (PIL)
* OpenPyXL
Kütüphaneleri yüklemek için:
pip install selenium requests pillow openpyxl 

4️⃣ Temp Klasörü
Ürünlerin kapak resimlerini kaydetmek için proje dosyasında Temp adında bir klasör oluşturulmalıdır.

5️⃣ Kodun Çalıştırılması
1) Gerekli kütüphaneler yüklendikten sonra kod dosyasını bir Python editöründe açın (örneğin VSCode).
2) Kod çalıştırıldığında, şu adımları takip edin:
* Dosya adını girin.
* Kaydetmek istediğiniz dosya formatını seçin (Excel veya TXT).
3) Program tamamlandığında dosyalar belirtilen formatta kaydedilecektir.

⚠️ Kullanım Sırasında Dikkat Edilmesi Gerekenler
* Yasal Sorumluluklar:
Kodun kullanımı sırasında sahibinden.com'un kullanım şartlarına ve yasal düzenlemelere uyduğunuzdan emin olun. Tüm yasal sorumluluk kullanıcıya aittir.

* Lisans

Bu yazılım, **MIT Lisansı** ile lisanslanmıştır.

* Eğitim Amacı:
Bu araç yalnızca eğitim ve bireysel kullanım amaçlı geliştirilmiştir; kötüye kullanım hedeflenmemiştir.

* Kapak Fotoğrafları:
Fotoğraflar Excel dosyasına eklenirken "Temp" klasörüne kaydedilir. Bu klasörü silmeden önce işlemlerin tamamlandığından emin olun.

Not:
Bu proje açık kaynaklıdır ve geliştirilmesi için katkılara açıktır. Herhangi bir hata veya geliştirme öneriniz varsa benimle iletişime geçebilirsiniz. 😊

