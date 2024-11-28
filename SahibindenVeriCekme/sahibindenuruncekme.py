import os
import time
import requests
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from PIL import Image
from io import BytesIO
import openpyxl
from openpyxl.drawing.image import Image as ExcelImage

# Ürün verilerini belirli bir URL'den toplamak için fonksiyon
def extract_product_data(url, num_pages, page_size=50):
    # Ürün verilerini saklamak için listeler
    product_images = []     # Ürün kapak resimleri
    product_names = []      # Ürün isimleri
    product_prices = []     # Ürün fiyatları
    product_locations = []  # Ürün konumları
    product_links = []      # Ürün sayfa linkleri

    driver_path = "C:\\Users\\PC\\Desktop\\SahibindenVeriCekme\\chromedriver-win64\\chromedriver.exe"  # ChromeDriver yolu

    for page in range(num_pages):
        offset = page * page_size
        full_url = f"{url}&pagingOffset={offset}"

        # Selenium için Chrome tarayıcı başlat
        service = Service(driver_path)
        driver = webdriver.Chrome(service=service)

        try:
            # Sayfayı yükle
            driver.get(full_url)
            time.sleep(3)  # Sayfanın yüklenmesini bekle

            # Sayfada ürün olup olmadığını kontrol et
            title_elements = driver.find_elements(By.CLASS_NAME, "classifiedTitle")
            if not title_elements:
                print(f"Sayfa {page+1} boş. Veri bulunamadı, işlem sonlandırılıyor.")
                break  # Sayfa boşsa döngüyü sonlandır

            # Ürün başlıklarını al
            for element in title_elements:
                product_names.append(element.get_attribute("title"))  # Ürün adı ekle
                product_links.append(element.get_attribute("href"))   # Ürün linki ekle

            # Ürün fiyatlarını al
            price_elements = driver.find_elements(By.CLASS_NAME, "classified-price-container")
            for element in price_elements:
                price = element.text.strip()  # Fiyat bilgisi varsa al
                product_prices.append(price if price else "")

            # Ürün konum bilgilerini al
            location_elements = driver.find_elements(By.CLASS_NAME, "searchResultsLocationValue")
            for element in location_elements:
                # Konumdaki iki kelimeyi birleştirip aralarına boşluk koy
                location = " ".join(element.text.strip().split())
                product_locations.append(location)

            # Ürün kapak fotoğraflarını al
            image_elements = driver.find_elements(By.XPATH, '//td[contains(@class, "searchResultsLargeThumbnail")]//img')
            for element in image_elements:
                product_images.append(element.get_attribute("src"))  # Kapak fotoğrafı URL'sini ekle

        except Exception as e:
            print(f"Hata oluştu: {e}")
            break
        finally:
            driver.quit()  # Tarayıcıyı kapat

    return product_images, product_names, product_prices, product_locations, product_links

# Veriyi dosyaya kaydetmek için fonksiyon
def save_data_to_file(product_images, product_names, product_prices, product_locations, product_links):
    # Kullanıcıdan dosya adı ve dosya türü al
    file_name = input("Verileri kaydedeceğiniz dosya adını girin: ").strip()
    file_type = input("Verileri hangi formatta kaydetmek istersiniz? (excel/txt): ").strip().lower()
    
    # Excel formatında kaydetme seçeneği
    if file_type == 'excel':
        workbook = openpyxl.Workbook()  # Yeni Excel dosyası oluştur
        sheet = workbook.active
        sheet.title = "Product Data"    # Çalışma sayfasına başlık ekle
        
        # Başlık satırını ekle
        sheet.append(["Image", "Product Name", "Product Price", "Location", "Product Link"])
        
        # Resimleri kaydedecek geçici klasör oluştur
        temp_dir = "C:\\Users\\PC\\Desktop\\SahibindenVeriCekme\\temp"
        os.makedirs(temp_dir, exist_ok=True)
        
        # Verileri Excel'e ekle
        for i in range(len(product_names)):
            sheet.append([None, product_names[i], product_prices[i], product_locations[i], product_links[i]])

            # Resmi kaydet ve Excel hücresine ekle
            if product_images[i]:
                try:
                    response = requests.get(product_images[i])
                    img = Image.open(BytesIO(response.content))
                    temp_file_path = os.path.join(temp_dir, f"temp_image_{i}.png")
                    img.save(temp_file_path, format='PNG')

                    # Excel dosyasına resmi ekle
                    img_excel = ExcelImage(temp_file_path)
                    img_excel.width = 80  # Resim genişliği
                    img_excel.height = 80 # Resim yüksekliği
                    sheet.add_image(img_excel, f"A{i + 2}")
                    
                except Exception as e:
                    print(f"Fotoğraf eklenirken hata oluştu: {e}")
                    continue

        # Excel dosyasını kaydet
        workbook.save(f'{file_name}.xlsx')
        print(f"Veriler {file_name}.xlsx dosyasına kaydedildi.")
    
    # TXT formatında kaydetme seçeneği
    elif file_type == 'txt':
        # Her ürünü satır olarak kaydet
        with open(f'{file_name}.txt', 'w', encoding='utf-8') as file:
            for i in range(len(product_names)):
                file.write(f"Ürün Adı: {product_names[i]}\n")         # Ürün adını yaz
                file.write(f"Fiyat: {product_prices[i]}\n")           # Fiyatı yaz
                file.write(f"Konum: {product_locations[i]}\n")        # Konumu yaz
                file.write(f"Link: {product_links[i]}\n")             # Linki yaz
                file.write("-" * 40 + "\n")                           # Ayrım çizgisi
        print(f"Veriler {file_name}.txt dosyasına kaydedildi.")
    
    else:
        print("Geçersiz dosya formatı seçildi.")

# Kullanım örneği: URL girilir ve veri çekme/kaydetme işlemi başlatılır
url = input("Verileri çekmek için URL girin: ")
num_pages = int(input("Kaç sayfa veri çekmek istersiniz? (Her sayfada 50 ürün) "))
product_images, product_names, product_prices, product_locations, product_links = extract_product_data(url, num_pages)
save_data_to_file(product_images, product_names, product_prices, product_locations, product_links)
