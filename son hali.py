import numpy as np
import cv2
from itertools import combinations

# Görüntülerin yolu ve dosya adlarını içeren bir liste oluşturun
resimler = [
    "1.png",
    "2.png",
    "3.png",
    "4.png",
    "5.png",
    "6.png",
    "7.png",
    "8.png",
    "9.png",
    "10.png",
    "11.png",
    "12.png",
    "13.png",
    "14.png",
    "15.png",
    "16.png",
    "17.png",
    "18.png",
    "19.png",
    "20.png",
    "21.png",
    "22.png",
    "23.png",
    "24.png",
    "25.png",
    "26.png",
    "27.png",
    "28.png",
    "29.png",
    "30.png",
    "31.png",
    "32.png",
    "33.png",
    "34.png",
    "35.png",
    "36.png",
    "37.png",
    "38.png",
    "39.png",
    "40.png",
    "41.png",
    "42.png",
    "43.png",
    "44.png",
    "45.png",
    "46.png",
    "47.png",
    "48.png",
    "49.png",
    "50.png",
    "51.png",
    "52.png",
    "53.png",
    "54.png",
    "55.png",
    "56.png",
    "57.png",
    "58.png",
    "59.png",
    "60.png",
    "61.png",
    "62.png",
    "63.png",
    "64.png",
    "65.png",
    "66.png",
    "67.png",
    "68.png",
    "69.png",
    "70.png",
    "71.png",
    "72.png",
    "73.png",
    "74.png",
    "75.png",
    "76.png",
    "77.png",
    "78.png",
    "79.png",
    "80.png",
    "81.png",
    "82.png",
    "83.png",
    "84.png",
    "85.png",
    "86.png",
    "87.png",
    "88.png",
    "89.png",
    "90.png",
    "91.png",
    "92.png",
    "93.png",
    "94.png",
    "95.png",
    "96.png",
    "97.png",
    "98.png",
    "99.png",
    "100.png",
    "101.png",
    "102.png",
    "103.png",
    "104.png",
    "105.png",
    "106.png",
    "107.png",
    "108.png",
    "109.png",
    "110.png",
    "111.png",
    "112.png",
    "113.png",
    "114.png",
    "115.png",
    "116.png",
    "117.png",
    "118.png",
    "119.png",
    "120.png",
    "121.png",
    "122.png",
    "123.png",
    "124.png",
    "125.png",
    "126.png",
    "127.png",
    "128.png",
    "129.png",
    "130.png",
    "131.png",
    "132.png",
    "133.png",
    "134.png",
    "135.png",
    "136.png",
    "137.png",
    "138.png",
    "139.png",
    "140.png",
    "141.png",
    "142.png",
    "143.png",
    "144.png",
    "145.png",
    "146.png",
    "147.png",
    "148.png",
    "149.png",
    "150.png",

    # Diğer görüntü dosyalarını buraya ekleyin
]

# Görüntüleri yükleyip parçalara ayırma işlemini gerçekleştiren fonksiyon
def ozellikleri_cikar(resimler):
    orb = cv2.ORB_create()  # OpenCV kütüphanesinde bulunan ORB (Oriented FAST and Rotated BRIEF) öznitelik dedektörünü oluşturur. 
    ozellikler = [] # ozellikler adında boş liste oluşturur.
    for resim in resimler:
        görüntü = cv2.imread(resim) # fonksiyon, belirtilen resmi okur ve görüntü değişkenine atar.
        gri = cv2.cvtColor(görüntü, cv2.COLOR_BGR2GRAY) # fonksiyon, görüntüyü renkli moddan gri tonlamalı moduna dönüştürür. Gri tonlamalı görüntü, daha hızlı ve daha verimli özellik çıkarma için kullanılır.
        anahtar_noktaları, tanimlayicilar = orb.detectAndCompute(gri, None)# görüntü üzerinde anahtar noktaları bulur ve bu anahtar noktaları için tanımlayıcılar çıkarır.
        # Anahtar noktaları, görüntünün dikkate değer bölgelerini temsil ederken, tanımlayıcılar bu bölgelerin özelliklerini tanımlar. Bu fonksiyon, gri görüntüyü ve None parametresini alır. None parametresi, bir maske kullanılmadığını belirtir.
        
        ozellikler.append((resim, tanimlayicilar))  # Oluşturulan resimler ve tanımlayıcıları ozellikler listesine eklenir.
    return ozellikler

# İki resim arasındaki benzerlik oranını hesaplayan fonksiyon
def benzerliği_hesapla(parça1, parça2):
    korelasyon = cv2.matchTemplate(parça1, parça2, cv2.TM_CCOEFF_NORMED) # Bu fonksiyon, bir resim parçalarını eşleştirir ve benzerlik derecesini hesaplar. "cv2.TM_CCOEFF_NORMED" parametresi, korelasyon yöntemi olarak katsayı korelasyonu kullanılacağını belirtir.
    benzerlik = korelasyon[0][0] # Hesaplanan korelasyon değeri, "korelasyon" değişkenine atılır
    return benzerlik

# En çok benzeyen resimleri bulan fonksiyon
def en_cok_benzeyen_resimleri_bul(ozellikler):
    en_cok_benzeyen = [] # Boş bir liste oluşturur
    kombinasyonlar_listesi = combinations(ozellikler, 2)  # ozellikler  listesindeki özelliklerin tüm 2'li kombinasyonları elde edilir
    for (resim1, özellik1), (resim2, özellik2) in kombinasyonlar_listesi: 
        benzerlik = benzerliği_hesapla(özellik1, özellik2)
        if benzerlik == 1:  # Benzerlik oranı 1 ise
            en_cok_benzeyen.append((resim1, resim2, benzerlik)) #  resim çiftini ve benzerlik oranını kaydet
    return en_cok_benzeyen

# Görüntü özelliklerini çıkar
ozellikler = ozellikleri_cikar(resimler)

# En çok benzeyen resimleri bul
benzer_resimler = en_cok_benzeyen_resimleri_bul(ozellikler)


# Sonuçların yazdırılması
print("Benzerlik Oranı 1 Olan Resim Çiftleri:")
print("Benzerlik oranının 1 olması resimlerin benzer olduğunu ifade eder!")
for resim_cifti in benzer_resimler:
    resim1, resim2, benzerlik = resim_cifti
    print(f"{resim1} ve {resim2} arasındaki benzerlik: {benzerlik}")
