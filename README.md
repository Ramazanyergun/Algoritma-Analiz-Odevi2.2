# Algoritma Analiz Odevi2.2
 2. Kisa Sinav 2. Ödev

Benzerlik Hesaplamada Kullanılan Algoritmalar

Resimler arasındaki benzerlikleri hesaplamak için farklı yöntemler ve algoritmalar kullanılabilir. İşte yaygın olarak kullanılan bazı yöntemler:
1.  Öklidyen Mesafesi: İki resim arasındaki benzerliği hesaplamak için en basit yöntemlerden biri, öklidyen mesafesi kullanmaktır. Bu yöntemde, her iki resim arasındaki piksel değerlerinin farkları hesaplanır ve bu farkların kareleri toplanarak mesafe hesaplanır. Daha düşük mesafe değerine sahip olan resimler, daha benzer olarak kabul edilir.
2. Orta Kare Hesaplama: Bu yöntemde, resimlerin pikselleri küçük kare bölgelere ayrılır. Her karenin piksel değerleri toplanarak orta değer hesaplanır. Ardından, iki resmin orta değerlerinin farkı hesaplanarak benzerlik ölçütü elde edilir.
3. Yapısal Benzerlik İndeksi (Structural Similarity Index, SSIM): SSIM, bir referans resim ile hedef resim arasındaki benzerliği ölçmek için kullanılan bir metriktir. Bu metrik, parlaklık, kontrast ve yapının korunması gibi faktörleri dikkate alarak benzerlik değerini hesaplar. SSIM, insan görsel algısına daha yakın sonuçlar vermek için tasarlanmıştır.
4. Histogram Benzerliği: Görüntülerin histogramlarının benzerliklerini hesaplayarak resimler arasındaki benzerliği tahmin etmek için kullanılan bir yöntemdir. Histogramlar, piksel yoğunluklarının dağılımını temsil eder ve benzer dağılıma sahip histogramlara sahip resimler, genellikle birbirlerine benzerdir.
5. Derin Öğrenme Yaklaşımları: Derin öğrenme, resimler arasındaki benzerliği hesaplamak için etkili bir yöntemdir. Evrişimli Sinir Ağları (Convolutional Neural Networks, CNN) gibi derin öğrenme modelleri, resimlerin içerdiği özellikleri çıkarmak ve resimler arasındaki benzerlikleri hesaplamak için kullanılabilir.
Bu yöntemler, resim benzerliğini ölçmek için yaygın olarak kullanılan bazı tekniklerdir. Her bir yöntem, farklı avantajlara ve dezavantajlara sahip olabilir ve uygulanan resimlerin özelliklerine bağlı olarak farklı sonuçlar verebilir. Ayrıca, çeşitli kombinasyonlar ve özelleştirmeler de yapılarak daha gelişmiş benzerlik hesaplama yöntemleri oluşturulabilir.

OpenCV Yöntemi

OpenCV (Open Source Computer Vision Library), bilgisayarla görüş alanında yaygın olarak kullanılan bir kütüphanedir. OpenCV'nin içinde birkaç resim benzerliği hesaplama yöntemi bulunmaktadır. İşte OpenCV ile kullanılan bazı resim benzerliği hesaplama yöntemleri:
Ortak Özellik Eşleştirme (Feature Matching): OpenCV, SIFT (Scale-Invariant Feature Transform), SURF (Speeded Up Robust Features) ve ORB (Oriented FAST and Rotated BRIEF) gibi özellik çıkarım yöntemlerini destekler. Bu yöntemlerle resimlerin özelliklerini çıkarabilir ve bu özellikleri kullanarak resimler arasında eşleştirmeler yapabilirsiniz. Özelliklerin eşleştirilmesi, resimlerin benzerlik derecesini hesaplamanıza yardımcı olur.
Histogram Benzerliği: OpenCV, resimlerin renk dağılımlarını temsil etmek için histogramlar kullanır. İki resmin histogramlarını oluşturup, bu histogramları karşılaştırarak benzerlik ölçebilirsiniz. Bhattacharyya mesafesi veya Kullback-Leibler (KL) uzaklığı gibi metrikler kullanılarak histogram benzerliği hesaplanabilir.
Template Matching: OpenCV, bir resimde belirli bir şablona (template) uyumlu bölgeleri bulmak için template matching yöntemini destekler. Şablon eşleştirme, resimde belirli bir nesnenin benzerlik ölçüsünü bulmak için kullanılabilir.
Resim Hizalama (Image Alignment): OpenCV, resimleri hizalamak ve benzerliklerini hesaplamak için dönüşüm matrislerini hesaplamak üzere kullanılabilir. Bu yöntem, iki resmin birbirine ne kadar benzediğini ölçmek için kullanılabilir.
Yönlü Gradyan Histogramları (Histogram of Oriented Gradients - HOG): OpenCV, resimlerin gradient bilgilerini kullanarak HOG özellik vektörleri çıkarabilir. Bu özellik vektörleri arasındaki benzerlik, resimlerin benzerliklerini hesaplama amacıyla kullanılabilir.
OpenCV, daha birçok resim işleme ve benzerlik hesaplama yöntemini destekler. Kullanılacak yöntem, özellikle uygulama amacına ve veri setinin özelliklerine bağlı olarak seçilmelidir.

Kodun Amacının Açıklanması

Kod, belirli bir resimler listesindeki görüntüler arasındaki benzerlikleri bulmayı amaçlar. Aşağıda kodun detaylı amacı açıklanmıştır:
resimler listesi, işlenecek görüntülerin dosya adlarını içerir.
ozellikleri_cikar fonksiyonu, resimleri yükler ve her bir görüntüden özellikleri çıkarır. Özellik çıkarmak için ORB (Oriented FAST and Rotated BRIEF) algoritması kullanılır. Görüntüler, gri tonlamalı hâle dönüştürülerek daha hızlı ve verimli özellik çıkarma sağlanır. Bu fonksiyon, her bir görüntünün adını ve özelliklerini içeren bir liste döndürür.
benzerliği_hesapla fonksiyonu, iki resim parçası arasındaki benzerlik oranını hesaplar. Bu fonksiyon, verilen resim parçalarını eşleştirerek benzerlik derecesini korelasyon yöntemiyle hesaplar.
en_cok_benzeyen_resimleri_bul fonksiyonu, özellikleri çıkarılan görüntüler arasında en çok benzeyen resim çiftlerini bulur. Bu fonksiyon, özelliklerin tüm 2'li kombinasyonlarını oluşturur ve her bir kombinasyon için benzerliği_hesapla fonksiyonunu çağırarak benzerlik oranını hesaplar. Eğer benzerlik oranı 1 ise, bu resim çiftini ve benzerlik oranını bir listeye ekler.
ozellikler listesine ozellikleri_cikar fonksiyonuyla görüntülerin özellikleri çıkarılır.
en_cok_benzeyen_resimleri_bul fonksiyonu kullanılarak en çok benzeyen resimler bulunur.
Bulunan sonuçlar ekrana yazdırılır. benzer_resimler listesindeki her bir resim çifti için benzerlik oranı ve resim adları yazdırılır.
Bu şekilde, verilen görüntüler arasında benzerlik oranı 1 olan çiftleri bulan bir sistem oluşturulmuştur.
Benzerlik oranının 1 olması resimlerin benzer olduğunu gösterir.

Karmaşıklık Analizi

Bu kodun zaman karmaşıklığı, özellikle en_cok_benzeyen_resimleri_bul fonksiyonunun karmaşıklığı üzerinde odaklanarak değerlendirilebilir. Diğer fonksiyonlar genellikle sabit zaman karmaşıklığına sahiptir.
1. ozellikleri_cikar fonksiyonu: Resimler listesindeki her bir görüntü için ORB dedektörünü kullanır ve görüntülerin özelliklerini çıkarır. Bu işlem, her bir görüntü için ORB dedektörünün çalışma süresine bağlı olarak lineer zaman karmaşıklığına O(n) sahiptir, burada n resimler listesinin boyutudur.
2. benzerliği_hesapla fonksiyonu: İki resim parçası arasındaki benzerlik oranını hesaplar. Bu işlem, cv2.matchTemplate işlevinin çalışma süresine bağlı olarak lineer zaman karmaşıklığına O(m) sahiptir, burada m resim parçalarının boyutudur.
3. en_cok_benzeyen_resimleri_bul fonksiyonu: Tüm olası resim çiftlerini karşılaştırır ve benzerlik oranını hesaplar. ozellikler listesindeki tüm özelliklerin kombinasyonlarını elde etmek için kullanılan combinations fonksiyonu, n resim özelliği arasında O(n^2) kombinasyon oluşturur. Her bir kombinasyon için benzerliği_hesapla fonksiyonu çağrılarak benzerlik oranı hesaplanır. Dolayısıyla, en_cok_benzeyen_resimleri_bul fonksiyonunun zaman karmaşıklığı O(n^2 * m) olarak değerlendirilebilir.
Toplam karmaşıklık, ozellikleri_cikar ve en_cok_benzeyen_resimleri_bul fonksiyonlarının karmaşıklıklarının toplamından oluşur.
Sonuç olarak toplam karmaşıklık, bu iki fonksiyonun karmaşıklıklarının toplamıdır. Dolayısıyla, toplam karmaşıklık O(n + n^2 * m) olarak ifade edilebilir.




