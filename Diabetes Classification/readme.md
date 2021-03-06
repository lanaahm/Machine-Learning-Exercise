# Laporan Proyek Machine Learning - Maulana Ahmad Maliki

## Domain Proyek

<p align='center'>
  <img width='300' src='https://user-images.githubusercontent.com/57904007/169671159-182b5de1-20a5-47b3-857c-da90953da289.png' alt='Sumber : https://pusdatin.kemkes.go.id/resources/download/pusdatin/infodatin/infodatin-Diabetes-2018.pdf'>
</p>

<p align='justify'>
Diabetes adalah salah satu penyakit kronis yang mengancam jiwa dengan pertumbuhan tercepat yang telah mempengaruhi 422 juta jiwa di seluruh dunia menurut laporan World Health Organization (WHO), pada tahun 2018. Diabetes merupakan masalah kesehatan masyarakat yang menjadi salah satu dari empat penyakit tidak menular prioritas yang menyebabkan peningkatan gula darah serta banyak komplikasi yang terjadi jika diabetes tidak diobati atau tidak teridentifikasi <a href="#ref7">[7]</a>. Hal tersebut juga merupakan tujuan yang ditindak lanjuti para pemimpin dunia termasuk organisasi internasional seperti World Health Organization (WHO), sebuah badan Perserikatan Bangsa-Bangsa (PBB) yang telah menetapkan Sustainable Development Goals (SDGs) pada kategori Good Health and Well-being. Menurut laporan WHO jumlah kasus diabetes terus meningkat selama beberapa tahun terakhir <a href="#ref6">[6]</a>.
</p>

<p align='justify'>
WHO memperkirakan secara global, 422 juta orang dewasa di atas usia 18 tahun menderita diabetes. Jumlah terbesar penderita diabetes diperkirakan berasal dari Asia Tenggara dan Pasifik Barat. Herwindo et al, 2018. Memaparkan bahwa terdapat seorang wanita yang melahirkan anak pertamanya yang dikonsultasikan dengan peningkatan gula darah setelah melahirkan. Pasien dan keluarganya tidak memiliki riwayat penyakit diabetes pada anamnesis dan pemeriksaan fisik. Pengamatan dan temuan laboratorium menunjukkan bahwa pasien menderita diabetes sebelum kehamilan, tetapi hal ini tidak terkonfirmasi melalui tes pemeriksaan <a href="#ref5">[5]</a>.
</p>

<p align='justify'>
Tujuan dari pembuatan model machine learning ini adalah merancang model yang dapat memperkirakan kemungkinan terjadinya diabetes pada pasien dengan ketelitian yang maksimal. Klasifikasi adalah teknik yang menetapkan kategori pada kumpulan data untuk membantu dalam melakukan memprediks, Oleh karena itu. Perlu adanya algoritma klasifikasi machine learning untuk mendeteksi diabetes sejak dini dengan lebih mudah dan efisien.
</p>

## Business Understanding

### Problem Statements

Berdasarkan permasalahan yang sudah dijelaskan maka rumusan masalah dalam proyek ini adalah sebagai berikut:
- Bagaimana machine learning dapat melakukan prediksi diabetes?
- Bagaimana melakukan pemrosesan data diabetes agar dapat digunakan untuk melakukan prediksi?
- Bagaimana menentukan algoritma machine laerning yang digunakan untuk melakukan prediksi diabetes?
- Bagaimana cara melakukan evaluasi algoritma untuk mendapatkan hasil prediksi diabtes?

### Goals

Berikut merupakan tujuan dari dibuatnya proyek ini antara lain:
- Melakukan prediksi dengan beberapa algoritma machine larning untuk melakukan prediksi diabtes.
- Melakukan pemrosesan data diabetes dengan baik agar dapat digunakan pada model algoritma machine laerning.
- Melakukan pengujian beberapa algoritma machine learning berdasarkan hasil dari matrik evaluasi.
- Melakukan evaluasi terhadap hasil dari beberapa algoritma dengan beberapa matrik untuk dapat memperkirakan prediksi diabetes yang optimal.

### Solution statements

Solusi yang dapat dilakukan untuk memenuhi tujuan dari proyek ini adalah sebagai berikut:
- Melakukan pengujian data diabetes untuk dapat melakukan prediksi yang terbaik dengan beberapa algrotima, antara lain `K-Nearest Neighbor`, `Random Forest`, dan, `AdaBoost`.
- Melakukan pemrosesan data diabetes yang dilakukan dengan beberapa teknik, diantaranya :
  - Melakukan pengecekan data yang hilang pada dataset diabetes.
  - Melakukan pengisian data yang kosong atau bernilai 0 dengan nilai rata rata (_mean substitution_) dan nilai yang sering keluar (_mode substitution_).
  - Menghapus data pencilan pada data latih dengan metode IQR _Inter Quartile Range_.
  - Melakukan konversi kategori data pada beberapa fitur.
  - Melakukan pengecek rata-rata diabetes terhadap masing-masing fitur kategori untuk mengetahui pengaruh fitur terhadap hasil diabetes.
  - Melakukan pengecek korelasi fitur numerik terhadap hasil diabetes.
  - Melakukan pembagian dataset menjadi dua bagian dengan rasio 80% untuk data latih dan 20% untuk data uji
  - Melakukan normalisasi pada fitur data numerik.

    Poin pemrosesan data akan dibahas lebih lanjut pada bagian [Data Preparation](#predata).
- Melakukan pengujian pada beberapa algoritma yang sudah disebutkan dan mencari hasil yang terbaik berdasakan hasil dari matrik evaluasi.
- Membandingkan serta mencari nilai yang terbaik dari beberapa algoritma terhadap matrik evaluasi, antara lain `Accuracy`, `F1-score`, `Precision`, dan `Recall`.

## Data Understanding
![Dataset Banner](https://user-images.githubusercontent.com/57904007/169673351-b046149e-3fb4-468a-90ef-89435520ee05.png)

| Jenis | Keterangan |
| - | - |
| Original owners| National Institute of Diabetes and Digestive and Kidney Diseases |
| Sumber | [Kaggle Dataset : Diabetes](https://www.kaggle.com/datasets/mathchi/diabetes-data-set) |
| Jenis dan Ukuran Berkas | CSV (525 kb) |
| Rating Penggunaan | 10.0 (Gold) |
| Lisensi | CC0: Public Domain |

<p align='justify'>
Berkas yang digunakan pada proyek ini adalah data konsultasi pasien diabetes dengan jenis kelamin wanita berusia minimal 21 tahun dari keturunan Pima India. Data tersebut dibuat dalam format Comma Separated Values (CSV) dengan ukuran 525kb dan didalamnya terdapat 768 data konsultasi pasien. Data konsultasi pasein memiliki 7 bertipe numerik (int64) dan 2 buah data bertipe numerik (float64). Data tersebut terlihat cukup rapih karena tidak ada nilai data yang hilang tetapi data tersebut memiliki data yang berisikan nilai 0 seperti pada data <code>Glucose</code>, <code>BloodPressure</code>, dan <code>BMI</code> dimana data tersebut seharusnya bukan bernilai 0. Penjelasan mengenai variabel-variable pada data diabetes dapat dilihat pada poin-poin berikut:
</p>

- `Pregnancies`: Jumlah berapa kali hamil
- `Glucose`: Konsentrasi glukosa plasma 2 jam dalam tes toleransi glukosa oral
- `BloodPressure`: Tekanan darah diastolik (mm Hg)
- `SkinThickness`: Ketebalan lipatan kulit trisep (mm)
- `Insulin`: Insulin serum 2 Jam (mu U/ml)
- `BMI`: Indeks massa tubuh (berat dalam kg/(tinggi dalam m)^2)
- `DiabetesPedigreeFunction`: Fungsi silsilah diabetes
- `Age`: Usia (tahun)
- `Outcome`: Variabel kelas (0 atau 1) yang menandakan diabetes atau tidak

### Visualisasi Univariate Analysis
Tujuan dari dibuatnya visualsasi univariate analysis pada data konsultasi diabetes ini adalah untuk mengetahui sebaran distribusi sebelum dilakukan proses perhitungan pada model algoritma untuk mengetahui hasil prediksi yang optimal. univariate analysis pada proyek ini akan menjelaskan data pada dataset diabetes antara lain:

#### Categorical Features
![image](https://user-images.githubusercontent.com/57904007/169673571-7bd4e501-7145-4e84-9a3e-44ae8abf1284.png)

Dapat dilihat pada tampilan visualisasi beberapa fitur data diatas memiliki distribusi data yang bervariasi yang akan dijelaskan sebagai berikut:
- Data Glucose, data tersebut merupakan data konsultasi pasien dapat dilihat sebaran data terbanyak pada kategori prediabetic dikisaran angka 250, data pasein pada kategori diabetic dikisaran angka 200-250, dan data pasein pada kategori non diabetic berada pada dikisaran 180.
- Data BloodPressure, data tersebut merupakan data pasien dengan beberapa kategori dilihat sebaran data terbanyak pada kategori normal dikisaran angka 500, data pasein yang mengalami perhepertensi dikisaran angka 100, dan data pasein hepertensi berada pada dikisaran 50-100.
- Data Insulin, data tersebut merupakan data pasien dengan 2 kategori Abnormal dan Normal. Pada kategori abnormal berada dikisaran angka 400 dan data pasein kategori normal berada pada dikisaran 250.
- Data BMI, data tersebut merupakan data pasien dengan beberapa kategori dilihat sebaran data pasien terbanyak pada kategori Obesity dikisaran angka 400, data pasein pada kategori Overweight dikisaran angka 150, data pasein pada kategori Healty Weight dikisaran angka 100, dan data pasein Underweight berada pada dikisaran 10.

#### Numerical Features
![image](https://user-images.githubusercontent.com/57904007/169673595-b94dff22-3dc7-42ce-953a-356710150bd6.png)

Dapat dilihat pada tampilan visualisasi beberapa fitur data diatas memiliki distribusi data yang bervariasi yang akan dijelaskan sebagai berikut:
- Data Pregnancies, data tersebut merupakan data konsultasi pasien dengan jumlah kehasilan yang dilaporan dapat dilihat sebaran data pasien yang belum pernah mengalami kehamilan berada pada kirasan angka 100, pasien yang pernah mengalami kehamilan 2 kali berada pada kirasan angka 120 pasien, dan seterusnya.
- Data SkinThickness, data tersebut merupakan data konsultasi pasien dengan banyak ukuran ketebalan lemak pada dimensi (mm). Pasien yang tidak memiliki ketebalan lemak dengan jumlah 200 dan seterusnya.
- DiabetesPedigreeFunction, data tersebut merupakan data konsultasi pasien dengan silsilah diabetes. Pasien yang memiliki silsilah diabetes 0.2 berada pada kisaran angka 20 dan seterusnya.
- Age, data tersebut merupakan data konsultasi pasien dengan rentan umur. Pasien yang memiliki rentang umur 20 dengan jumlah angka dikirasan 50 pasien, pasien yang memiliki umur 30 dengan jumlah angka dikirasan 20 pasien dan seterusnya.

### Visualisasi Multivariate Analysis
Multivariate merupakan hubungan antara dua atau lebih variabel pada data. Multivariate menunjukkan hubungan antara dua variabel biasa disebut sebagai bivariate EDA. Tujuan dari dibuatnya visualsasi univariate analysis pada data konsultasi diabetes ini adalah untuk mengetahui hubungan pada setia data konsultasi pasien terhadap hasil diabetes.

#### Hubungan antara data categorical features terhadap hasil diabetes
![image](https://user-images.githubusercontent.com/57904007/169673831-63a5d7b5-bec8-497b-8a05-2bd8ea5c3dcd.png)

Dapat dilihat pada tampilan visualisasi beberapa fitur data diatas memiliki hubungan terhadap hasil diagnosa diabtes yang akan dijelaskan sebagai berikut:
- Data Glucose, data tersebut menunjukan data pasien dengan beberapa kategori yang memiliki hubungan terhadap hasil diagnosa diabetes. Data pasien pada kategori Diabetic memiliki hubungan dengan hasil diabetes yang berada pada kisaran angka 0.5 - 0.6, Data pasien pada kategori non diabetic memiliki hubungan dengan hasil diabetes yang berada pada kisaran angka 0.1, dan Data pasien pada kategori prediabetic memiliki hubungan dengan hasil diabetes yang berada pada kisaran angka 0.2. 
- Data BloodPressure, data tersebut menunjukan data tekanan darah pasien dengan beberapa kategori yang memiliki hubungan terhadap hasil diagnosa diabetes. Data pasien pada kategori hypertension memiliki hubungan dengan hasil diabetes yang berada pada kisaran angka 0.5, Data pasien pada kategori normal memiliki hubungan dengan hasil diabetes yang berada pada kisaran angka 0.3, dan Data pasien pada kategori prehypertension memiliki hubungan dengan hasil diabetes yang berada pada kisaran angka 0.4.
- Data Insulin, data tersebut menunjukan data hasil pemberian insulin serum selama 2 Jam pada pasien dengan beberapa kategori yang memiliki hubungan terhadap hasil diagnosa diabetes. Data pasien pada kategori abnormal memiliki hubungan dengan hasil diabetes yang berada pada kisaran angka 0.3-0.4 dan Data pasien pada kategori normal memiliki hubungan dengan hasil diabetes yang berada pada kisaran angka 0.2.
- Data BMI, data tersebut menunjukan data index masa tubuh pasien dengan beberapa kategori yang memiliki hubungan terhadap hasil diagnosa diabetes. Data pasien pada kategori healty weight memiliki hubungan dengan hasil diabetes yang berada pada kisaran angka 0.1, Data pasien pada kategori obesity memiliki hubungan dengan hasil diabetes yang berada pada kisaran angka 0.4, Data pasien pada kategori overweight memiliki hubungan dengan hasil diabetes yang berada pada kisaran angka 0.2, dan Data pasien pada kategori underweight memiliki hubungan dengan hasil diabetes yang berada pada kisaran angka 0.0.

<h4 id='korelasi'>Korelasi Numerical Features </h4>

![image](https://user-images.githubusercontent.com/57904007/169673850-1c117af2-2e6b-4605-89e1-38aa10ceb4a2.png)

Dapat dilihat pada tampilan visualisasi korelasi fitur data diatas. Korelasi mengukur kekuatan hubungan antara dua variabel serta arahnya (positif atau negatif). Mengenai kekuatan hubungan antar variabel, semakin dekat nilainya ke 1 atau -1, korelasinya semakin kuat. Sedangkan, semakin dekat nilainya ke 0, korelasinya semakin lemah. 

<h2 id='predata'>Data Preparation</h2>
Seperti yang sudah disebutkan sebelumnya pada bagian Solution statements, berikut adalah tahapan-tahapan dalam melakukan pemrosesan data:

- Mengisi data yang bernilai 0 dengan nilai rata rata (_mean substitution_) dan nilai yang sering keluar (_mode substitution_).

![image](https://user-images.githubusercontent.com/57904007/169675127-82cca3c9-ce8b-4b7a-9c05-9a3239809b4b.png)

Dapat dilihat pada tabel diatas bawah ada beberapa data yang memiliki nilai 0 seperti pada data `Glucose`, `BloodPressure`, dan `BMI` yang merupakan data tersebut tidak mungkin memiliki nilai 0 untuk mengatasi masalah tersebut dapat dilakukan pengisian data.

![image](https://user-images.githubusercontent.com/57904007/169675137-f485fd01-e341-4a49-a483-3fbeba4dd03d.png)

Nilai kosong pada data `Glucose` dan `BloodPressure` akan dilakukan pengisian nilai dengan yang sering keluar atau modus sedangkan pada data `BMI` diisi dengan nilai rata-rata atau maen. Memanipulasi data dengan mengisi data yang kosong dengan nilai data rata-rata atau nilai yang sering keluar sehingga dengan menganggap data kosong sebagai data rata-rata, model tetap dapat memperoleh informasi dari data yang ada pada kolom lainnya.

- Menghapus data pencilan pada data latih dengan metode IQR _Inter Quartile Range_.
Outliers adalah sampel yang nilainya jauh dari rentang umum data utama yang merupakan sample data langka dan berbeda dengan data lainnya. IQR adalah singkatan dari Inter Quartile Range. Boxplot menunjukkan ukuran lokasi dan penyebaran, serta memberikan informasi tentang simetri dan outliers

![image](https://user-images.githubusercontent.com/57904007/169675397-21dd685c-467e-4125-a392-b4cfad136471.png)

Dari visualisasi Blox Plot diatas dapat dilihat masih banyak fitur data yang mengalami outlier dikarenakan data tersebut seharunya data kategori.

- konversi kategori data pada beberapa fitur
Dari dataset diabetes yang digunakan pada proyek ini memiliki beberapa fitur data yang meruapakan data kategori namun masih dalam bentuk numerik sehingga beberapa data tersebut mengalami outliers beberapa fitur tersebut antara lain:. 
  - `Glucose`: Artikel "Glucose Tolerance Testing: Reference Range, Interpretation, Collection and Panels" menjelaskan bahwa glucose tolerance digunakan untuk mengevaluasi kemampuan untuk mengatur metabolisme glukosa dan diindikasikan ketika tes glukosa darah untuk dilakukan diagnosis. Fitur Glucose pada dataset ini adalah data numerik dengan range Konsentrasi glukosa plasma 2 jam nilai numerik tersebut sudah ditentukan pada setiap kategori seperti yang dijelaskan pada artikel <a href="#ref1">[1]</a>.
  - `BloodPressure`: Artikel "High Blood Pressure Symptoms and Causes" mejelaskan bahwa tekanan darah akan berubah sepanjang hari berdasarkan aktivitas yang dilakukan. fitur BloodPressure pada dataset ini adalah data numerik. Nilai numerik tersebut sudah ditentukan pada setiap kategori seperti yang sudah dijelaskan dalam artikel <a href="#ref4">[4]</a>.
  - `Insulin`: Artikel "Insulin: Reference Range, Interpretation, Collection and Panels" menjelaskan bahwa Insulin adalah hormon anabolik yang mendorong pengambilan glukosa, glikogenesis, lipogenesis, dan sintesis protein otot rangka dan jaringan lemak melalui jalur reseptor tirosin kinase. Fitur Insulin pada dataset ini adalah data numerik dengan range 2 jam setelah pemberian glukosa yang bernilai numerik. Artikel tersebut mejelaskan bahwa nilai insulin berada pada range 16-166 mIU/L sepetelah 2 jam setelah pemberian glukosa untuk kategori normal <a href="#ref3">[3]</a>.
  - `BMI`: Artikel "About Adult BMI | Healthy Weight, Nutrition, and Physical Activity" mejelaskan bahwa BMI adalah metode pemeriksaan yang mudah untuk mengetahui kategori berat badan. fitur BMI pada dataset ini adalah data numerik. Nilai numerik tersebut sudah ditentukan pada setiap kategori seperti untuk dapat menetahui kondisi kategori berat badan <a href="#ref2">[2]</a>.

- Menghapus data yang memiliki korelasi lemah. seperti yang dapat dilihat pada <a href='#korelasi'>korelasi data</a> fitur pada data `SkinThickness` memiliki hubungan korelasi yang lemah terhadap hasil diagnosa diabetes maka data tersebut akan dilakukan penghapusan sebelum pelagukan perhitungan prediksi pada algoritma agar algoritma dapat melakukan prediksi dengan optimal.

- Melakukan pembagian dataset menjadi dua bagian dengan rasio 80% untuk data latih dan 20% untuk data uji
Menurut Raschka, 2018. melakukan pembagian dataset menjadi data latih dan data uji adalah cara yang tepat menghindari terjadinya <i>overfitting</i> atau memperkecil tingkat kesalahan akurasi prediksi pada model, Dengan kata lain. Tidak bisa mengatakan apakah tingkat akurasi model menjadi bagus tetapi untuk menggeneralisasi prediksi pada model dengan data yang tidak diketahui pada proses pengujian <a href="#ref9">[9]</a>.

- Normalisasi Data
Normalisasi data merupakan proses pembentukan struktur data sehingga dapat menghilangkan sebagian besar ambiguitas. Menurut Pyle, 1999. proses normalisasi bertujuan untuk memetakan nilai atribut data agar berada dalam rentang tertentu. Normalisasi data yang dilakukan pada proyek ini menggunakan metode Min-Max Normalization dengan formula sebagai berikut <a href="#ref8">[8]</a>.

<p align='center'>
  <img width='300' src='https://user-images.githubusercontent.com/57904007/169675533-c5276038-cbd2-428d-96ea-bdaec6e8adba.png' />
</p>

## Modeling
Setelah melakukan pemrosesan data yang baik maka data tesebut akan dilakukan pengujian dengan model algoritma berikut:
- K-Nearest Neighbor

  Algoritma K-NN adalah metode klasifikasi yang menggunakan algoritma supervised terhadap sekumpulan data berdasarkan pembelajaran data yang sudah diklasifikasikan pada sebelumnya. KNN bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat (dengan k adalah sebuah angka positif).
  
  - Kelebihan Algoritma K-NN:
    - Algoritma K-NN kuat dalam mentraining data yang noisy.
    - Algoritma K-NN sangat efektif jika datanya besar.
    - Mudah diimplementasikan.

  - Kekurangan Algoritma K-NN:
    - Algoritma K-NN perlu menentukan nilai parameter K.
    - Sensitif pada data pencilan.
    - Rentan pada variabel yang non-informatif.
  
  - Paremeter Algoritma K-NN:
    - n_neighbors: proyek ini melakukan inisialisai nilai n_neighbors atau jumlah tetangga yang akan melakukan dengan perbandingan tetangga sebanyak 10.

- Random Forest
Random Forest adalah algoritma dalam machine learning yang digunakan untuk pengklasifikasian data set dalam jumlah besar. Karena fungsinya bisa digunakan untuk banyak dimensi dengan berbagai skala dan performa yang tinggi. kelebihan dan kekurangan pada Algoritma Random Forest. Kelebihannya yaitu dapat mengatasi noise dan missing value serta dapat mengatasi data dalam jumlah yang besar. Dan kekurangan pada algoritma Random Forest yaitu interpretasi yang sulit dan membutuhkan tuning model yang tepat untuk data.

  - Paremeter Algoritma Random Forest:
    - n_estimators: jumlah trees (pohon) di forest. Proyek ini melakukan inisialisai nilai n_estimator=50.
    - max_depth: kedalaman atau panjang pohon yang merupakan ukuran seberapa banyak pohon dapat membelah (splitting) untuk membagi setiap node ke dalam jumlah pengamatan yang diinginkan. Proyek ini melakukan inisialisai nilai max_depth=16
    - random_state: digunakan untuk mengontrol random number generator yang digunakan. Proyek ini melakukan inisialisai nilai n_estimator=55.
    - n_jobs: : jumlah job (pekerjaan) yang digunakan secara paralel yang merupakan komponen untuk mengontrol thread atau proses yang berjalan secara paralel. n_jobs=-1 artinya semua proses berjalan secara paralel.

- AdaBoost
Metode AdaBoost merupakan salah satu algoritma supervised pada data mining yang diterapakan secara luas untuk membuat model klasifikasi. Metode adaBoost merupakan salah satu teknik ensamble dengan menggunakan loss function fungsi exponential untuk memperbaiki tingkat akurasi dari prediksi yang dibuat.

  - Paremeter Algoritma Random Forest:
    - learning_rate: bobot yang diterapkan pada setiap regressor di masing-masing proses iterasi boosting. Proyek ini melakukan inisialisai nilai learning_rate=0.05.
    - random_state: digunakan untuk mengontrol random number generator yang digunakan. Proyek ini melakukan inisialisai nilai n_estimator=55.

Hasil evaluasi matrix pada setiap algoritma dalam melakukan prediksi diabetes dapat dilihat pada tabel dibawah ini.
![image](https://user-images.githubusercontent.com/57904007/169675933-72b55e8a-bc41-4332-9fb6-7ddc1c1471a2.png)

Hasil dari beberapa pengujian algoritma diatas algoritma KNN lebih unggul dalam segala aspek evaluasi baik dari akurasi, f1-score, presisicon, recall. Maka dapat diambil kesimpulan bahwa algoritma KNN lebih cocok untuk melakukan klasifikasi diabetes.

## Evaluation
Model algoritma proyek ini meggunakan matrik evaluasi akurasi, f1-score, recall dan precision dalam melakukan analisis untuk mendapatkan hasil kalsifikasi terbaik. Berikut merupakan hasil dari confusion matris pada seriap algoritma.

- K-Nearest Neighbor

  ![image](https://user-images.githubusercontent.com/57904007/169676235-b8764c0a-e27a-47e7-829a-9225dd0ce6d3.png)

- Random Forest

  ![image](https://user-images.githubusercontent.com/57904007/169676245-98d9ab24-880b-4d54-a3a5-bf60f2383807.png)

- AdaBoost

  ![image](https://user-images.githubusercontent.com/57904007/169676259-0e1357e6-68d0-47fe-8b23-9f87e66a6de5.png)
  
Berikut merupakan hasil evaluasi matrix pada setiap algoritma berserta penjelasan dari matrix yang digunakan.
![image](https://user-images.githubusercontent.com/57904007/169675933-72b55e8a-bc41-4332-9fb6-7ddc1c1471a2.png)

- Precision 
  
  Presisi adalah kemampuan pengklasifikasi untuk tidak melabeli instance positif yang sebenarnya negatif. Untuk setiap kelas itu didefinisikan sebagai rasio positif benar dengan jumlah positif benar dan salah.
  ```
  TP ??? True Positives
  FP ??? False Positives

  Precision = TP/(TP + FP)
  ```
 
- Recall 
  
  Recall adalah kemampuan classifier untuk menemukan semua instance positif. Untuk setiap kelas itu didefinisikan sebagai rasio positif benar dengan jumlah positif benar dan negatif palsu.
  ```
  FN ??? False Negatives

  Recall = TP/(TP+FN)
  ```
 
- Precision 
  
  Presisi adalah kemampuan pengklasifikasi untuk tidak melabeli instance positif yang sebenarnya negatif. Untuk setiap kelas itu didefinisikan sebagai rasio positif benar dengan jumlah positif benar dan salah.
  ```
  TP ??? True Positives
  FP ??? False Positives

  Precision = TP/(TP + FP)
  ```  
 
- F1 score 
  
  Skor F1 adalah rata-rata harmonik tertimbang dari presisi dan daya ingat sehingga skor terbaik adalah 1,0 dan yang terburuk adalah 0,0. Secara umum, skor F1 lebih rendah daripada ukuran akurasi karena menyertakan presisi dan daya ingat ke dalam perhitungannya. Sebagai aturan praktis, rata-rata tertimbang F1??harus digunakan untuk membandingkan model pengklasifikasi, bukan akurasi global.  
  ```
  F1 Score = 2*(Recall * Precision) / (Recall + Precision)
  ```
 
## References
<ul type='None'>
  <li>
    <a id="ref1"></a>
    [1] Glucose Tolerance Testing: Reference Range, Interpretation, Collection and Panels [Internet]. Tersedia pada: <a href='https://emedicine.medscape.com/article/2049402-overview'>https://emedicine.medscape.com/article/2049402-overview</a>.
  </li>
  <li>
    <a id="ref2"></a>
    [2] About Adult BMI | Healthy Weight, Nutrition, and Physical Activity | CDC [Internet]. Tersedia pada: <a href='https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html#Interpreted'>https://www.cdc.gov/healthyweight/assessing/bmi/adult_bmi/index.html#Interpreted</a>.
  </li>
  <li>
    <a id="ref3"></a>
    [3] Insulin: Reference Range, Interpretation, Collection and Panels [Internet]. Tersedia pada: <a href='https://emedicine.medscape.com/article/2089224-overview'>https://emedicine.medscape.com/article/2089224-overview</a>.
  </li>
  <li>
    <a id="ref4"></a>
    [4] High Blood Pressure Symptoms and Causes | cdc.gov [Internet]. Tersedia pada: <a href='https://www.cdc.gov/bloodpressure/about.htm#whatare'> https://www.cdc.gov/bloodpressure/about.htm#whatare</a>.
  </li>
  <li>
    <a id="ref5"></a>
    [5] Brahmantyo HP, Nurshanty A, Sasiarini L. Keterlambatan Diagnosis Diabetes Mellitus pada Kehamilan. J Kedokt Brawijaya [Internet]. 6 Februari 2017 ;281???5. Tersedia pada: <a href='https://jkb.ub.ac.id/index.php/jkb/article/view/1489'>https://jkb.ub.ac.id/index.php/jkb/article/view/1489</a>.
  </li>
  <li>
    <a id="ref6"></a>
    [6] Diabetes [Internet]. 2021. Tersedia pada: <a href='https://www.who.int/news-room/fact-sheets/detail/diabetes'>https://www.who.int/news-room/fact-sheets/detail/diabetes</a>
  </li>
  <li>
    <a id="ref7"></a>
    [7] Kemenkes RI. InfoDatin Pusat Data dan Informasi Kementerian Kesehatan RI Title proper: InfoDatin Pusat Data dan Informasi. 15 April 2018. Tersedia pada: <a href='https://pusdatin.kemkes.go.id/resources/download/pusdatin/infodatin/infodatin-Diabetes-2018.pdf'>https://pusdatin.kemkes.go.id/resources/download/pusdatin/infodatin/infodatin-Diabetes-2018.pdf</a>
  </li>
  <li>
    <a id="ref8"></a>
    [8] Pyle, D., 1999. Data preparation for data mining. San Francisco  Calif.: Morgan Kaufmann.
  </li>
  <li>
    <a id="ref9"></a>
    [9] Raschka, S., 2018. Model Evaluation, Model Selection, and Algorithm Selection in Machine Learning. [daring] <a href="https://doi.org/10.48550/arxiv.1811.12808">https://doi.org/10.48550/arxiv.1811.12808</a>.
  </li>
</ul>