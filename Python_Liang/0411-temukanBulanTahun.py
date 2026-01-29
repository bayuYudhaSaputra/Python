'''
================================================================================
Programming Exercise 04.11
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.11. Temukan Bulan dan Tahun
   Tuliskan program yang menawarkan prompt kepada pengguna untuk menginput 
   urutan bulan dan tahun. Kemudian, program menampilkan banyaknya hari bulan 
   tersebut. Misal, pengguna menginput  bulan 2 dan tahun 2000. Program 
   menampilkan pesan “Bulan Februari 2000 memiliki 29 hari”. Jika pengguna 
   menginput bulan 3 tahun 2005. Maka, program akan menampilkan pesan 
   “Bulan Maret 2005 mempunyai 31 hari”
================================================================================
'''

import sys

# 1. Input bulan dan tahun
bulan = eval(input("Input urutan bulan (mis. 1 untuk Januari): "))
tahun = eval(input("Input tahun : "))

# 2. Cek validitas tahun
if tahun < 0:        # cek apakah tahun diinput bilangan positif
    print("Peringatan : Anda harus menginput angka tahun lebih dari 0!")
    sys.exit()

# 3. Cek bulan
if bulan == 1:
    namaBulan = "Januari"
    banyakHari = 31
elif bulan == 2:
    namaBulan = "Februari"
    # Cek tahun kabisat
    if (tahun % 4 == 0 and tahun % 100 != 0) or tahun % 400 == 0:
        banyakHari = 29
    else:
        banyakHari = 28
elif bulan == 3:
    namaBulan = "Maret"
    banyakHari = 31
elif bulan == 4:
    namaBulan = "April"
    banyakHari = 30
elif bulan == 5:
    namaBulan = "Mei"
    banyakHari = 31
elif bulan == 6:
    namaBulan = "Juni"
    banyakHari = 30
elif bulan == 7:
    namaBulan = "Juli"
    banyakHari = 31
elif bulan == 8:
    namaBulan = "Agustus"
    banyakHari = 31
elif bulan == 9:
    namaBulan = "September"
    banyakHari = 30
elif bulan == 10:
    namaBulan = "Oktober"
    banyakHari = 31
elif bulan == 11:
    namaBulan = "November"
    banyakHari = 30
elif bulan == 12:
    namaBulan = "Desember"
    banyakHari = 31
else:
    print("Peringatan : Input bulan dengan bilangan 1 hingga 12 saja!")
    sys.exit()

# 4. Tampilkan bulan dan tahun
print("Bulan", namaBulan, tahun, "memiliki", banyakHari, "hari.")


