# Laporan Proyek Machine Learning - Maulana Ahmad Maliki

## Project Overview
![image](https://user-images.githubusercontent.com/57904007/171079976-6bb121eb-a617-446f-9a9a-09450aa291e0.png)

<p align='justify'>
film telah menjadi salah satu hiburan favorit utama masyarakat. Jumlah film pertahun terhitung mencapai ribuan. Hal ini membuat penggemar film kesulitan dalam memilih film mana yang tepat untuk ditonton sesuai keinginan. Besarnya kekuatan film kemudian melahirkan industri film yang menjadikan film sebagai komuditas yang mempunyai harga jual dan konsumen (pengguna film). Usaha peredaran film untuk mencapai konsumennya mengalami berbagai perubahan menyesuaikan perkembangan teknologi komunikasi dan informasi <a href="#ref2">[2]</a>.
</p>

<p align='justify'>
Di era digital ini, Internet menghidupkan sumber informasi digital dengan kemudahan akses dari berbagai perangkat teknologi informasi dan komunikasi secara cerdas, praktis dan terintegrasi. Terjadilah ledakan data dan informasi digital di mana sosial media, proses bisnis, publikasi-publikasi digital berperan meningkatkan volume dan pertumbuhan informasi digital. Pada bisnis film sendiri, tingginya produksi film secara global dan tingginya minat masyarakat akan film yang mendasari dibuatnya Internet Movie Database (IMDb). Database ini meliputi katalog perfilman yang memuat semua informasi mengenai film yang dimaksud, seperti judul, sutradara, aktor, genre, sinopsis dan rating. Pada IMDb, masyarakat diberikan kemudahan untuk dapat mencari film berdasarkan kata kunci yang diinputkan oleh pengguna dengan mudah tanpa harus mencari secara manual layaknya di media cetak. Selain itu, masyarakat dapat melihat berbagai film baik terbaru maupun lama sewaktu-waktu dan dimanapun dengan mengakses internet. Namun, pertumbuhan jumlah film di seluruh dunia yang begitu cepat memicu pertumbuhan database yang semakin cepat <a href="#ref1">[1]</a>.
</p>

<p align='justify'>
Pertumbuhan jumlah situs internet memicu terjadinya ledakan informasi di dunia maya yang menyulitkan pengguna dalam mencari suatu informasi yang diperlukan secara cepat dan relevan. Khusus di bidang film, industri ini bisa memproduksi sekitar 5000 judul film internasional setiap tahunnya. Kondisi tersebut menyebabkan penikmat film mengalami kesulitan dalam mencari film yang akan ditonton dan sesuai dengan selera masing-masing individu. Sehingga dibutuhkan sistem rekomendasi yang bertujuan untuk memberikan saran film mana yang akan dipilih atau dinonton dimasa depan. 
</p>

## Business Understanding

### Problem Statements

Berdasarkan permasalahan yang sudah dijelaskan maka rumusan masalah dalam proyek ini adalah sebagai berikut:
- Bagaimana cara membuat sistem rekomendasi untuk pengguna?
- Apakah sistem rekomendasi yang cocok pada kasus ini?
- Bagaimana sistem rekomendasi dapat merekomendasikan film untuk pengguna di IMDb?

### Goals

Berikut adalah tujuan dari dibuatnya proyek ini:
- Membuat sistem rekomendasi film untuk pengguna.
- Membuat sistem rekomendasi dengan kemiripan data film atau content base filtering.
- Memberikan rekomendasi untuk film yang memiliki kemiripan content pada pengguna.

### Solution statements

- Pra-pemrosesan data dengan beberapa teknik diantaranya:
  - Melakukan pengecekan nilai kosong pada setiap kolom.
  - Melakukan pengisian data kosong pada kolom Meta_score dan certification.
  - Memperbaiki tipe data pada setiap kolom.
  - Melakukan pembersihkan data duplikasi.

  Setelah hal tersebut dilakukan, selanjutnya dilakukan visualisasi data yang dapat dilihat lebih lengkap pada bagian Data Understanding.

- Persiapan data (Data Preparation) dilakukan beberapa teknik diantaranya:
  - Melakukan Konversi label kategori dengan metode one-hot encoding.
  - Melakukan Normalisasi data numerik.
  
  Penjelasan lengkap mengenai persiapan data dapat dilihat lebih lengkap pada bagian Data Preparation.

- Pembuatan sistem rekomendasi content based filtering dengan 2 pendekatan diantaranya:
  - K-Nearest Neighbor. Algoritma tersebut dipilih karena cocok pada kasus clustering untuk melakukan sistem rekomendasi. KNN bekerja dengan membandingkan jarak satu sampel ke sampel pelatihan lain dengan memilih sejumlah k tetangga terdekat.
  - Cosine similarity. Algoritma akan dijadikan pembandingan dengan sistem rekomendasi dengan model KNN. Cosine similarity digunakan untuk mengukur kemiripan antara dua buah vektor dan kesamaan arahnya dengan cara menghitung sudut kosinus dari kedua vektornya. 

## Data Understanding
<p align='center'>
  <img  width='100%' src='https://user-images.githubusercontent.com/57904007/170904420-aa173c83-573b-434b-a316-525faa908e35.png' alt='Sumber: https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows'>
</p>

| Jenis | Keterangan |
| - | - |
| Sumber | [Kaggle Dataset : IMDB Movies Dataset](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows/metadata) |
| Jenis dan Ukuran Berkas | CSV (438.1 kB) |
| Rating Penggunaan | 10.0 (Silver) |
| Lisensi | CC0: Public Domain |


Informasi dataset pada berkas `mdb_top_1000.csv`:

![image](https://user-images.githubusercontent.com/57904007/171077834-c9e84392-ca7d-42a8-8eb0-4858da091545.png)

<p align='justify'>
Tampilan data informasi diatas merupakan tampilan informasi pada dataset. Data tersebut dibuat dalam format Comma Separated Values (CSV) dengan ukuran 438.1kb dan didalamnya terdapat 1000 data film. Data film memiliki 13 kolom bertipe object dan 2 kolom bertipe numerik (float64). Data tersebut memiliki beberapa data dengan nilai yang hilang atau kosong `Meta_score`, `certificat` dan `gross`. Penjelasan mengenai variabel-variable pada data diabetes dapat dilihat pada poin-poin berikut:
</p>

- `Poster_Link`: Link poster film.
- `Series_Title`: Nama film.
- `Released_Year`: Tahun rilis film.
- `Certificate`: Sertifikat yang diperoleh dari film tersebut.
- `Runtime`: Durasi film.
- `Genre`: Genre film.
- `IMDB_Rating`: Peringkat film pada situs IMDB.
- `Overview`: Sinopsis / ringkasan dari film tersbut.
- `Meta_score`: Skor yang diperoleh dari film tersbut.
- `Director`: Director dari film.
- `Star1,Star2,Star3,Star4`: Pemeran bintang  pada film tersebut.
- `No_of_Votes`: Jumlah total vote dari film tersebut.
- `Gross`: Penghasilan yang diperoleh film tersebut.

<p align='justify'>
Berdasarkan pejelaskan yang sudah dijelaskan pada masing-masing variabel pada dataset. dapat dilakukan analisis untuk beberapa data diantaranya yaitu melakukan pengecekan nilai kosong dan pengecekan tipe data pada semua kolom dataset. pengecekan tersebut bertujuan untuk mengetaui apakah kolom data tersebut akan digunakan untuk melakukan sistem rekomendasi. data `Released_Year` terlihat ganjal dimana seharusnya tahun rilis adalah bilangan bulat tetapi pada data tersebut bernilai object, dan data `certification` memiliki beberapa data kosong yang cukup banyak. data `Overview` tidak digunakan karena untuk menghindari kemiripan rekomendasi agar rekomendasi akan menjadi lebih general. data `Gross` tidak digunakan pada kasus ini dikarenkan tidak terlalu berpengaruh terhadap rekomendasi pengguna.
</p>

### Visualisasi Univariate Analysis
Tujuan dari dibuatnya visualsasi univariate analysis pada data kasus ini adalah untuk mengetahui sebaran distribusi sebelum dilakukan proses perhitungan pada model algoritma untuk mengetahui hasil rekomendasi yang optimal. univariate analysis pada kasus ini akan menjelaskan data pada dataset film antara lain:

#### Categorical Features
![image](https://user-images.githubusercontent.com/57904007/171079512-3fecbe76-3faf-452a-9416-c3bb0eb85cea.png)

Pada tampilanvisualisasi data diatas dapat dilihat bawah distribusi kategori pada kolom Certificate memiliki distribusi data dengan kategori U berada pada rentang nilai 200, kategori A diretang 150-190, kategori UA berada pada rentang 150-180, dan seterusnya.

#### Numerical Features
![image](https://user-images.githubusercontent.com/57904007/171079555-5d9c6f88-aad1-43a6-b66d-3214b8d6a4d8.png)

Dapat dilihat pada tampilan visualisasi beberapa kolom data diatas memiliki distribusi data yang bervariasi yang akan dijelaskan sebagai berikut:
- Kolom Runtime, data tersebut merupakan data durasi yang dimiliki setiap film dalam menit dapat dilihat sebaran data runtime film yang memiliki durasi 100 menit berada pada rentang 80, film yang memiliki durasi 150 berapa pada rentang 20-30, dan seterusnya.
- Kolom IMDB_Rating, data tersebut merupakan data rating dari film berdasarkan rata" dari hasil voting pada situs IMDB dapat dilihat sebaran data IMDB_Rating film yang memiliki rating 7.5 menit berada pada rentang 140-160, film yang memiliki rating 8.0 berapa pada rentang 140, dan seterusnya.
- Kolom Meta_Score, data tersebut merupakan data skor yang diberikan untuk ulasan film dari sekelompok besar kritikus paling dihormati di dunia dapat dilihat sebaran data Meta_Score film yang memiliki Meta_Score 60 menit berada pada rentang 20-25, film yang memiliki Meta_Score 70 berapa pada rentang 30-40, dan seterusnya.
- Kolom No_of_votes, data tersebut merupakan data jumlah total vote dari film tersebut dapat dilihat sebaran data No_of_votes pada film yang memiliki vote kurang dari 5 juta vote berada pada rentang 100-360, film yang memiliki vote 5 juta berapa pada rentang 30-5, dan seterusnya.

### Visualisasi Multivariate Analysis
Tujuan dari dibuatnya visualsasi univariate analysis pada data film ini adalah untuk mengetahui hubungan pada data pasien terhadap jumlah voting.

#### Categorical Features
![image](https://user-images.githubusercontent.com/57904007/171079606-9a99de91-bea7-4a17-b719-fda9e507d84a.png)

Dapat dilihat pada tampilan visualisasi fitur Certificate data diatas memiliki hubungan terhadap hasil jumlah votes film. hasil visualisasi tersebut menunjukan data certificate dengan beberapa kategori yang memiliki hubungan terhadap jumlah. Film yang Certificate A memiliki hubungan dengan hasil jumlah vote yang berada pada kisaran angka 4juta, Film yang Certificate U memiliki hubungan dengan hasil jumlah vote yang berada pada kisaran angka 2juta. dan seterusnya

#### Numerical Features
![download](https://user-images.githubusercontent.com/57904007/171079687-5f6796ed-7133-4e9f-8302-0e6aaf868fee.png)

Tampilan visualisasi diatas menunjukkan relasi pasangan dalam dataset. Pada kasus ini hanya fokus terhadap No_of_Votes dari pola sebaran data (titik-titik) pada tampilan di atas, pola data grafik No_of_Votes memiliki korelasi positif. Hal ini ditandai dengan meningkatnya variabel pada sumbu y saat terjadi peningkatan variabel pada sumbu x yang terdapat pada tampilan IMDB_Rating dan Meta_score.

#### Korelasi Numerical Features
![image](https://user-images.githubusercontent.com/57904007/171079811-ccfde567-d152-4b9c-9af5-45e08c531a1f.png)

Dapat dilihat pada tampilan visualisasi korelasi fitur data diatas. Korelasi mengukur kekuatan hubungan antara dua variabel serta arahnya (positif atau negatif). Mengenai kekuatan hubungan antar variabel, semakin dekat nilainya ke 1 atau -1, korelasinya semakin kuat. Sedangkan, semakin dekat nilainya ke 0, korelasinya semakin lemah. Tampilan diatas menunjukan bahwa kolom data Meta_Score memiliki hubungan yang lemah terhadap hasil voteing sehingga dapat dilakukan pengapusan pada kolom data tersebut.

## Data Preparation

Seperti yang sudah dijelaskan pada bagian Solution approach dan Data Understanding, berikut adalah tahapan-tahapan dalam melakukan pra-pemrosesan data diantaranya:

- Melakukan pengecekan nilai kosong dan memperbaiki tipe data pada setiap kolom. Hal ini dilakukan karena beberapa tipe data pada setiap kolom memiliki kejangalan. Berikut ini merupakan rincian proses yang dilakukan:
  - Kolom `Meta_score`: Melakukan pengisian data kosong.
  - Kolom `Runtime`: Menghapus string "min" dan mengganti tipe data kolom menjadi int.
  - Kolom `Released_Year`: Menghapus data ganjal yang bernilai 'PG' dan mengganti tipe data kolom menjadi int.
  - Kolom `Certificate`: Melakukan pengisian data kosong.
- Melakukan pengisian data kosong pada kolom Meta_score. Hal ini dilakukan karena banyak sekali data rating yang kosong dan apabila dihapus yang akan mengakibatkan model yang dibuat kehilangan banyak informasi untuk membangun sistem rekomendasi. Proses yang dilakukan untuk mengisi data kosong atau data hilang adalah dengan menggunakan KNNImputer dari sklearn. KNNImputer mengimputasi data menggunakan K-Nearest Neighbor dengan mencari tetang terdekat pada kasus ini menggunakan 50 tetangga diakarenakan memiliki data yang cukup banyak. Dengan demikian data Rating akan tetap terjaga distribusi datanya.
- Melakukan pengecekan data duplikat dan menghapusnya jika ada.
- Melakukan penghapusan data yang tidak digunakan seperti yang dijelaskan pada bagian Data Understanding diantaranya `Poster_Link`, `Overview`, dan `Gross`.
- Menghapus data yang memiliki korelasi lemah. seperti yang dapat dilihat pada korelasi data fitur pada data Meta_score memiliki hubungan korelasi yang lemah terhadap jumlah voting maka data tersebut akan dilakukan penghapusan untuk dapat memiliki hasil rekomendasi yang optimal.
- Melakukan Konversi data kategori menjadi one-hot encoding. Hal ini dilakukan untuk memudahkan pencarian nilai terdekat dari setiap film. Data yang dilakukan proses encoding ini merupakan data kategori yang diubah menjadi data numerik dengan value 0 dan 1. Proses ini dialkukan menggunakan method get_dummies pada kolom yang mengandung data ketegori kemudian data tersebut digabungkan kembali pada dataset. Beberapa data tersebut antara lain: `Genre`, `Certificate`, `Director`, dan `Star`
- Normalisasi Data Normalisasi data merupakan proses pembentukan struktur data sehingga dapat menghilangkan sebagian besar ambiguitas. Menurut Pyle, 1999. proses normalisasi bertujuan untuk memetakan nilai atribut data agar berada dalam rentang tertentu. Normalisasi data yang dilakukan pada proyek ini menggunakan metode Min-Max Normalization dengan formula sebagai berikut <a href="#ref5">[5]</a>.

## Modeling
Setelah dilakukan pra-pemrosesan data, selanjutnya adalah membuat sistem rekomendasi content based filtering dengan dua pendekatan diantaranya.
- K-Nearest Neighbor
  Algoritma K-NN adalah metode klasifikasi yang menggunakan algoritma supervised terhadap sekumpulan data berdasarkan pembelajaran data yang sudah diklasifikasikan pada sebelumnya. KNN bekerja dengan membandingkan jarak satu sampel ke sampel lain dengan memilih sejumlah k tetangga terdekat (dengan k adalah sebuah angka positif). Parameter yang digunakan pada kasus ini adalah metriks euclidian, dengan jumlah tetangga (n_neighbors) default atau 5. setelah dilakukan pelatihan pada model knn selanjutnya akan dilakukan pembuatan sebuah fungsi `getRecommenderMovies_KNN` untuk memberikan rekomendasi film dengan hipotesis apabila pengguna menyukai atau melakukan vote pada jenis film tersebut, maka berikan rekomendasi film yang memiliki kemiripan pada film tersebut dengan hasil seperti berikut.

  ![image](https://user-images.githubusercontent.com/57904007/171085624-c26a71a2-16b8-4373-8eb0-9b8f1232dcd5.png)

- Cosine similarity.
  Cosine similarity mengukur kesamaan antara dua vektor dan menentukan apakah kedua vektor tersebut menunjuk ke arah yang sama. Ia menghitung sudut cosinus antara dua vektor. Proses yang dilakukan dengan menggunakan cosine_similarity adalah memanggil dataframe sebagai objeknya yang telah dilakukan perhitungan pada dataframe baru. Dataframe baru tersebut merupakan nilai yang dihasilkan dari perhitungan cosine_similarity. Untuk dapat memberi rekomendasinya dibuatkan fungsi `getRecommenderMovies_cosine` dimana fungsi tersebut akan memberikan rekomendasi terhadap suatu nama film dengan hipotesis yang sama seperti algoritma KNN.
  Dalam fungsi ini, pencarian kolom dilakukan pada nama film pada dataframe baru yang diperoleh dari menghitung kesamaan cosine_similarity. Nilai-nilai tersebut kemudian diurutkan menurut nilai kesamaan cosinus tertinggi dan urutannya. Setiap barisan dari 2 terakhir hingga n terakhir merupakan kandidat dengan nilai cosinus similarity yang sama, dan akan ditampilkan sebagai hasil rekomendasi. Urutan terakhir adalah nilai kesamaan cosinus kolom dengan nama film yang sama dengan hasil seperti berikut.
  ![image](https://user-images.githubusercontent.com/57904007/171086732-d1716a76-862f-490d-9537-e59a80366106.png)


## Evaluation
1. Precission
  Presisi adalah kemampuan pengklasifikasi untuk tidak melabeli instance positif yang sebenarnya negatif. Untuk setiap kelas itu didefinisikan sebagai rasio positif benar dengan jumlah positif benar dan salah. berikut merupakan formula dari precission.
  ```
    TP – True Positives
    FP – False Positives

    Precision = TP/(TP + FP)
  ```
  - KNN
    Precision pada hasil pendekatan KNN didapatkan nilai `90%`. dikarenakan hasil prediksi yang memiliki genre serupa berjumlah 9 dan 1 rekomendasi memiliki genre Fantasy
  - Cosine Similarity
    Precision pada hasil pendekatan Cosine Similarity didapatkan nilai `70%`. dikarenakan hasil prediksi yang memiliki genre serupa berjumlah 7 dan 3 rekomendasi memiliki genre Fantasy dan Animation

2. Davies Bouldin 
  Davies Bouldin adalah matriks evaluasi internal, di mana validasi seberapa baik pengelompokan telah dilakukan dilakukan dengan menggunakan jumlah dan fitur yang melekat pada dataset. Davies-Bouldin mengukur rasio antara jarak dalam cluster dan antara jarak cluster dan menghitung rata-rata keseluruhan cluster. Oleh karena itu relatif sederhana, dibatasi – 0 hingga 1, skor yang lebih rendah lebih baik <a href="#ref3">[3]</a>. Formula evaluasi matriks Davies Bouldin dapat dilihat dibawah ini.
  ![image](https://user-images.githubusercontent.com/57904007/171087253-b00a8475-5ca7-4dc3-9287-1a6b7e1310c8.png)

  - Kelebihan dari metriks ini adalah:
    - Komputasinya lebih mudah daripada Skor Silhouette.
    - Skor yang dihitung hanya jumlah dan fitur yang melekat pada dataset.
  - Kekurangan dari metriks ini adalah:
    - Metriks ini hanya baik digunakan pada kasus convex cluster.
    - Penggunaan jarak centroid membatasi metriks jarak ke ruang Euclidean
  
  Hasil penerapan evaluasi matriks Davies Bouldin pada kasus ini  
  ![image](https://user-images.githubusercontent.com/57904007/171143600-e44af6ff-b699-4e0e-be5a-a94bf5bca922.png)
  
  Pada kasus ini evaluasi yang ditujukan dengan metode evaluasi matriks Davies Bouldin memiliki akurasi yang rendah atau dapat dibilang baik yang menandakan bahwa sudah memiliki kluster yang cukup optimal. Hal ini dibuktikan juga dengan hasil rekomendasi film yang memiliki cukup kemiripan.
  
3. Calinski Harabasz
  Calinski Harabasz adalah matriks evaluasi yang digunakan untuk menghitung kriteria rasio varian. Metriks ini digunakan pada model clustering seperti yang saat ini sedang digunakan. Calinski-Harabasz membandingkan varians antar-cluster dengan varians dalam setiap cluster. Semakin tinggi skor semakin baik pemisahannya <a href="#ref4">[4]</a>. Formula evaluasi matriks Davies Bouldin dapat dilihat dibawah ini.
  ![image](https://user-images.githubusercontent.com/57904007/171087718-e1649438-e7db-4924-9743-15a0706bc24b.png)

  - Kelebihan dari metriks ini adalah :
    - Skornya tinggi apabila kluster padat dan terpisah dengan baik, yang mana bergantung pada konsep standar dari sebuah kluster.
    - Skornya cepat untuk dihitung.
  - kekurangannya dari metriks ini adalah:
    - Metriks ini hanya baik digunakan pada kasus convex cluster.

  Hasil penerapan evaluasi matriks Calinski Harabasz pada kasus ini  
  ![image](https://user-images.githubusercontent.com/57904007/171143420-7f82e3af-c308-4756-8c30-58688abec814.png)
  
  Pada kasus ini evaluasi yang ditujukan dengan metode evaluasi matriks Calinski Harabasz menunjukkan bahwa kluster masih belum terpisahkan dengan baik karena nilai skor yang rendah dan memungkinkan rekomendasi pada beberapa film masih terdapat rekomendasi yang tidak sesuai.
  
   
## References
<ul type='None'>
  <li>
    <a id="ref1"></a>
    [1] Sistem Rekomendasi Film menggunakan User-based Collaborative Filtering dan K-modes Clustering | Hadi | Jurnal Infra. <a href='https://publication.petra.ac.id/index.php/teknik-informatika/article/view/9800'>https://publication.petra.ac.id/index.php/teknik-informatika/article/view/9800</a>.
  </li>
  <li>
    <a id="ref2"></a>
    [2] Prabowo R, Toto A, #2 W, Rismala R. Pairwise Preference Regression on Movie Recommendation System. Indones J Comput. 2019;4(1):57–64. <a href='https://doi.org/10.21108/INDOJC.2019.4.1.255'>doi:10.21108/INDOJC.2019.4.1.255</a>.
  </li>
  <li>
    <a id="ref3"></a>
    [3] Ron  tom. Davies-Bouldin Index. <a href='https://tomron.net/2016/11/30/davies-bouldin-index/'>https://tomron.net/2016/11/30/davies-bouldin-index/</a>. Published 30 November 2016.
  </li>
  <li>
    <a id="ref4"></a>
    [4] Davies DL, Bouldin DW. A Cluster Separation Measure. IEEE Trans Pattern Anal Mach Intell. 1979;PAMI-1(2):224–227. <a href='https://doi.org/10.1109/TPAMI.1979.4766909'>doi:10.1109/TPAMI.1979.4766909</a>.
  </li>
  <li>
    <a id="ref5"></a>
    [5] Pyle, D., 1999. Data preparation for data mining. San Francisco  Calif.: Morgan Kaufmann.
  </li>
</ul>
