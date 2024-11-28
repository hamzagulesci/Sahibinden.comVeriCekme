Bu yazılan kod Hamza Güleşci tarafından yapılmıştır.

Sahibinden.com Veri Çekme Aracı

Bu proje, sahibinden.com üzerinde yapılan arama sonuçlarını kolayca toplamak ve bunları Excel veya TXT formatına dönüştürmek amacıyla geliştirilmiştir.
Kod, eğitim amaçlı yazılmıştır ve yalnızca verilerin organize edilmesine yardımcı olmak için tasarlanmıştır.

//

Özellikler:

Ürün adları, fiyatları, konum bilgileri ve linklerini toplar.
Ürünlerin kapak resimlerini indirip, Excel dosyasına ekler (opsiyonel).
Veriler TXT veya Excel formatında kaydedilebilir.
Sayfa sayısı sınırlaması olmadan çok sayıda ürün verisini toplayabilir.

//

Kurulum ve Kullanım:
Gerekli Adımlar

1) ChromeDriver Yolu Ayarı:

Kod içindeki driver_path değişkenine sisteminizde yüklü olan ChromeDriver'ın tam dosya yolunu ekleyin.
Örnek:

* driver_path = "C:\\Users\\PC\\Desktop\\SahibindenVeriCekme\\chromedriver-win64\\chromedriver.exe"

2) Arama URL'si Hazırlığı:

Sahibinden.com üzerinde arama yapın ve sayfa görüntüleme boyutunu 50 olarak ayarlayın.
Tarayıcınızdaki URL'yi kopyalayın ve size sorduğu zaman terminale yapıştırıp devam edin

3) Kütüphane Gereksinimleri:

Bu kodun çalışması için aşağıdaki Python kütüphaneleri yüklenmiş olmalıdır:

* Selenium
* Requests
* PIL (Pillow)
* OpenPyXL
* Gerekli kütüphaneleri yüklemek için şu komutları çalıştırabilirsiniz:

pip install selenium requests pillow openpyxl

4) Temp Klasörü:

Resimleri koyacağı bir klasör olmalı "Temp" adında bunu unutmayın. (Klasörde mevcut)

5) Kodun Çalıştırılması:

Eğer gerekli kütüphaneler henüz yüklenmediyse, pip install komutlarını kullanarak yükleyin üst tarafta belirttim.
Kod dosyasını bir Python editöründe açın (Örnek VSCode).
Size sırasıyla sorucak ilk dosya ismini sonra dosya tipini.
Dosya ismini aldıktan sonra dosya formatının (Excel veya TXT) seçiminizi yapın.

**Kullanım Sırasında Dikkat Edilmesi Gerekenler**

* Yasal Sorumluluklar:
Bu kodu kullanırken sahibinden.com'un kullanım şartlarına ve yasal düzenlemelere uyduğunuzdan emin olun. Tüm yasal sorumluluk kullanıcıya aittir.

* Eğitim Amacı:
Bu araç yalnızca eğitim ve bireysel kullanım amaçlı geliştirilmiştir; kötüye kullanım hedeflenmemiştir.

* Kapak Fotoğrafları:
Fotoğraflar Excel dosyasına eklenirken geçici bir klasöre kaydedilir(Temp). Bu klasörü silmeden önce işlem tamamlandığından emin olun.

* Geliştirici Notları
Bu kod açık kaynaklıdır. Kodun geliştirilmesine katkıda bulunmak veya sorun bildirmek isterseniz, lütfen GitHub üzerinde bir pull request gönderin.
Geri bildirimleriniz için teşekkür ederim.
