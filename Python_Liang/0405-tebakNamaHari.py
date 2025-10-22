'''
===============================================================================
Programming Exercise 04.05
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
-------------------------------------------------------------------------------
04.05.Menemukan Nama Hari 
   Tuliskan program yang menerima input berupa bilangan integer 0 hingga 6
   dengan 0, 1, 2, 3, 4, 5, dan 6 berturut-turut merepresentasikan hari 
   Senin, Selasa, Rabu, Kamis, Jumat, Sabtu, dan Minggu. Kemudian, program
   menawarkan prompt kepada pengguna lagi untuk menginput jumlah hari setelah
   hari yang diinput sebelumnya. Program menampilkan nama hari yang diinput
   dan nama hari beberapa hari kemudian.
===============================================================================
'''

import sys

# 1. Input index hari
keterangan = ("Input bilangan integer yang merepresentasikan nama hari "
         "dengan ketentuan: \n"
         "\t 0 : Senin \n"
         "\t 1 : Selasa \n"
         "\t 2 : Rabu \n"
         "\t 3 : Kamis \n" 
         "\t 4 : Jumat \n"
         "\t 5 : Sabtu \n"
         "\t 6 : Minggu")

print("========================================================================")
print(keterangan)
print("------------------------------------------------------------------------")

indexHariIni = eval(input("Input bilangan integer : "))

# 2. Tentukan nama hari
if indexHariIni == 0:
    namaHariIni = "Senin"
    print("Hari ini adalah hari", namaHariIni)
elif indexHariIni == 1:
    namaHariIni = "Selasa"
    print("Hari ini adalah hari", namaHariIni)
elif indexHariIni == 2:
    namaHariIni = "Rabu"
    print("Hari ini adalh hari", namaHariIni)
elif indexHariIni == 3:
   namaHariIni = "Kamis"
   print("Hari ini adalah hari", namaHariIni)
elif indexHariIni == 4:
    namaHariIni = "Jumat"
    print("Hari ini adalah hari", namaHariIni)
elif indexHariIni == 5:
    namaHariIni = "Sabtu"
    print("Hari ini adalah hari", namaHariIni)
elif indexHariIni == 6:
    namaHariIni = "Minggu"
    print("Hari ini adalah hari", namaHariIni)
else:
    print("Input angka 0 hingga 6 saja!")
    sys.exit()

# 3. Input bilangan yang menyatakan "berapa hari dari sekarang?"
keterangan = ("Input bilangan yang menyatakan "
              " Berapa hari lagi? "
              )
banyakHariEsok = eval(input(keterangan))

if banyakHariEsok >= 0:
    # 4. Jumlahkan
    jumlah = indexHariIni + banyakHariEsok

    # 5. Tentukan indeks hari esok
    indexHariEsok = jumlah % 7

    # 6. Tentukan nama hari esok
    print("-------------------------------------------------------------------")
    if indexHariEsok == 0:
        namaHariEsok = "Senin"
        print(banyakHariEsok, "hari lagi adalah ", namaHariEsok)
    elif indexHariEsok == 1:
        namaHariEsok = "Selasa"
        print(banyakHariEsok, "hari lagi adalah ", namaHariEsok)
    elif indexHariEsok == 2:
        namaHariEsok = "Rabu"
        print(banyakHariEsok, "hari lagi adalah ", namaHariEsok)
    elif indexHariEsok == 3:
        namaHariEsok = "Kamis"
        print(banyakHariEsok, "hari lagi adalah ", namaHariEsok)
    elif indexHariEsok == 4:
        namaHariEsok = "Jumat"
        print(banyakHariEsok, "hari lagi adalah ", namaHariEsok)
    elif indexHariEsok == 5:
        namaHariEsok = "Sabtu"
        print(banyakHariEsok, "hari lagi adalah ", namaHariEsok)
    elif indexHariEsok == 6:
        namaHariEsok = "Minggu"
        print(banyakHariEsok, "hari lagi adalah ", namaHariEsok)
else:
    print("Input bilangan bulat non-negatif")
    sys.exit()
    
print("========================================================================")
