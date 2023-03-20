
# Tugas Kecerdasan Buatan (A)

#### Anggota kelompok
Nama | NRP | 
--- | --- | 
Daud Dhiya' Rozan | 5025211021 | 
Anas Azhar | 5025211043 | 
Altriska Izzati Khairunnisa Hermawan | 5025211187 | 

## Pengertian Greedy Best-First Search dan 
Greedy Best First Search (GBFS)adalah algoritma pencarian jalur terpendek yang menggunakan heuristik untuk mengevaluasi setiap node dan memilih node yang paling dekat dengan tujuan akhir. Algoritma ini tidak mempertimbangkan path cost yang ditempuh sehingga dapat memilih jalur yang tidak optimal atau membuang waktu dengan mengeksplorasi node yang tidak diperlukan.

A* adalah algoritma pencarian jalur terpendek yang menggunakan nilai heuristik dan juga path cost. Algoritma ini mempertimbangkan final path dengan menyeimbangkan antara mengikuti path yang sudah dikenal dan mengeksplorasi jalur yang mungkin lebih baik. Dengan ini A* dapat menemukan jalur terpendek yang optimal dan lebih cepat dibandingkan GBFS.

## Analisis algoritma Greedy Best-First Search dan A*
Pada tugas ini, kami membuat dua program dengan mengimplementasikan algoritma informed search: GBFS dan A* Search pada Peta Jawa Timur dengan asal kota `Magetan` dan kota tujuan `Surabaya`. Dengan output sebagai berikut:
##### Greedy Best-First Search
```
----------------------------
| GREEDY BEST FIRST SEARCH |
----------------------------
Asal                    : Magetan
Tujuan                  : Surabaya
Kota yang dilewati      : Magetan -> Madiun -> Nganjuk -> Jombang -> Surabaya
Jarak                   : 394
Waktu                   : 0.0009968280780923802
```                         


##### A*
```
1679303946.0146503
1679303946.0156472
----------------------------
| A* SEARCH |
----------------------------
Asal                                    : Magetan
Tujuan                                  : Surabaya
Kota yg dilewati dg jarak terpendek     : ['Magetan', 'Ngawi', 'Bojonegoro', 'Lamongan', 'Gresik', 'Surabaya']
Jumlah kota yang dilewati               : 6
Total jarak                             : 144
Waktu                                   : 0.0009968280792236328
```
Dari output yang dihasilkan, dapat dilihat bahwa ada beberapa perbedaan antara kedua algoritma tersebut. Kota yang dikunjungi oleh program yang mengimplementasikan algoritma GBFS lebih sedikit dibandingkan A*, namun jarak yang ditempuh A* lebih sedikit dibandingkan dengan GBFS. Untuk selisih waktu antara sebelum  dan setelah dilakukannya fungsi algoritma, GBFS memiliki selisih waktu yang lebih sedikit dibansingkan dengan A* atau lebih cepat.

Oleh karena itu, dapat disimpulkan bahwa A* lebih lambat daripada GBFS karena harus mempertimbangkan cost sejauh ini untuk setiap kota yang dilalui, sementara GBFS hanya mempertimbangkan nilai heuristiknya. Namun, karena A* merupakan algoritma yang lebih optimal karena dapat menemukan jalur terpendek.
