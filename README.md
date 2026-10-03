## Pertemuan 05 Perulangan Python

## Identitas
- Nama: Gugun Ramdani
- NIM: 2225250061
- Kelas: 3A
- Mata Kuliah: Algoritma dan Pemrograman

## Tujuan
Pada pertemuan ini saya mempelajari dan mempraktikkan:
1. Konsep iterasi dan perulangan.
2. Penggunaan `for` dan `range`.
3. Penggunaan `while` dan kondisi berhenti.
4. Validasi input menggunakan `while`.
5. Penggunaan `if` di dalam perulangan.
6. Akumulasi dan pencacahan.
7. Tracing dan debugging perulangan.
8. Pengujian program menggunakan beberapa test case.
9. Penggunaan Git dan GitHub untuk mengumpulkan hasil pekerjaan.

## Struktur Folder
1. Pertemuan_05_Perulangan_2225250061
2. README.md
3. .gitignore
4. latihan/
- 01_tabel_perkalian.py
- 02_jumlah_bilangan.py
- 03_validasi_input.py
- 04_hitung_genap.py
5. kuis/
- kuis1_formatif_pertemuan 05.docx
- kuis2_deret_aritmetika.py

## Cara Menjalankan
Pastikan Python sudah terpasang.
# Contoh menjalankan latihan:
```bash
python latihan/01_tabel_perkalian.py
```
```bash
python latihan/02_jumlah_bilangan.py
```
```bash
python latihan/03_validasi_input.py
```
```bash
python latihan/04_hitung_genap.py
```
Untuk menjalankan Kuis 2:
```bash
python kuis/kuis2_deret_aritmetika.py
```

## Algoritma Kuis 2

1. Menampilkan judul program.
2. Membaca suku pertama `a`.
3. Membaca beda `d`.
4. Membaca banyak suku `n`.
5. Jika `n <= 0`, program meminta input `n` kembali menggunakan `while`.
6. Menginisialisasi `total = 0`.
7. Melakukan perulangan sebanyak `n` kali menggunakan `for`.
8. Menghitung suku dengan rumus:
```text
suku = a + i × d
```
9. Menambahkan setiap suku ke dalam `total`.
10. Menampilkan setiap suku.
11. Menampilkan jumlah seluruh suku dengan dua angka di belakang koma.

## Hasil Pengujian

### Test Case 1
Input:
```text
a = 2
d = 3
n = 5
```
Hasil:
```text
2.00, 5.00, 8.00, 11.00, 14.00
Jumlah = 40.00
```
Status: Berhasil

### Test Case 2
Input:
```text
a = 10
d = -2
n = 4
```
Hasil:
```text
10.00, 8.00, 6.00, 4.00
Jumlah = 28.00
```
Status: Berhasil

### Test Case 3
Input:
```text
a = 1.5
d = 0.5
n = 3
```
Hasil:
```text
1.50, 2.00, 2.50
Jumlah = 6.00
```
Status: Berhasil

### Test Validasi
Input `n`:
```text
0
-2
5
```
Program menolak `0` dan `-2`, kemudian menerima `5`.
Status: Berhasil

## Refleksi
Pada pertemuan ini saya memahami bahwa `for` dan `while` digunakan untuk kebutuhan yang berbeda. `for` lebih sesuai ketika jumlah iterasi sudah diketahui, sedangkan `while` digunakan ketika perulangan bergantung pada suatu kondisi.
Kesalahan yang perlu diperhatikan pada `while` adalah lupa memperbarui variabel kontrol. Jika variabel kontrol tidak berubah menuju kondisi `False`, program dapat mengalami infinite loop.
Saya juga memahami bahwa variabel akumulator seperti `total` harus diinisialisasi sebelum loop. Jika `total = 0` diletakkan di dalam loop, nilai yang telah dikumpulkan akan terus dihapus dan hasil akhirnya menjadi salah.
Selain itu, saya belajar menggunakan `if` di dalam loop untuk melakukan seleksi terhadap setiap nilai yang sedang diproses.

## Kesimpulan
Perulangan merupakan salah satu struktur dasar dalam pemrograman yang digunakan untuk menjalankan proses secara berulang. Pada pertemuan ini saya dapat menggunakan `for`, `while`, `if` dalam loop, akumulasi, pencacahan, validasi input, serta melakukan pengujian program.
Saya juga mempraktikkan penggunaan Git untuk melakukan commit dan GitHub untuk mengunggah hasil pekerjaan.
