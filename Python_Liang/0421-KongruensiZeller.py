'''
================================================================================
Programming Exercise 04.21
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.21. Kongruensi Zeller
   Tuliskan program yang meminta input tanggal. Program menentukan nama hari 
   dari tanggal tersebut.
================================================================================
'''
import sys

# 1. Input angka tahun
print("Input angka tahun setelah tahun 1582.")
input_tahun = int(input("Input tahun (mis. 2026) : "))

# 2. Validasi angka tahun
if ((input_tahun < 1582) or (input_tahun > 9999)):
    print("Input antara 1582 hingga 9999 saja.")
    sys.exit()

# 3. Input indeks nama bulan
print("\nKeterangan indeks bulan,\n \
      \t1  : Januari,\n \
      \t2  : Februari,\n \
      \t3  : Maret,\n \
      \t4  : April,\n \
      \t5  : Mei,\n \
      \t6  : Juni, \n \
      \t7  : Juli,\n \
      \t8  : Agustus,\n \
      \t9  : September,\n \
      \t10 : Oktober, \n \
      \t11 : November,\n \
      \t12 : Desember.")

indeks_bulan = int(input("Input indeks bulan (mis. 1): "))

# 4. Validasi indeks nama bulan
if (indeks_bulan == 3):
    nama_bulan = "Maret"
    m = indeks_bulan
    hitung_tahun = input_tahun

elif (indeks_bulan == 4):
    nama_bulan = "April"
    m = indeks_bulan
    hitung_tahun = input_tahun

elif (indeks_bulan == 5):
    nama_bulan = "Mei"
    m = indeks_bulan
    hitung_tahun = input_tahun

elif (indeks_bulan == 6):
    nama_bulan = "Juni"
    m = indeks_bulan
    hitung_tahun = input_tahun

elif (indeks_bulan == 7):
    nama_bulan = "Juli"
    m = indeks_bulan
    hitung_tahun = input_tahun

elif (indeks_bulan == 8):
    nama_bulan = "Agustus"
    m = indeks_bulan
    hitung_tahun = input_tahun

elif (indeks_bulan == 9):
    nama_bulan = "September"
    m = indeks_bulan
    hitung_tahun = input_tahun

elif (indeks_bulan == 10):
    nama_bulan = "Oktober"
    m = indeks_bulan
    hitung_tahun = input_tahun

elif (indeks_bulan == 11):
    nama_bulan = "November"
    m = indeks_bulan
    hitung_tahun = input_tahun

elif (indeks_bulan == 12):
    nama_bulan = "Desember"
    m = indeks_bulan
    hitung_tahun = input_tahun

elif (indeks_bulan == 1):
    nama_bulan = "Januari"
    m = indeks_bulan + 12
    hitung_tahun = input_tahun - 1  # ambil angka tahun lalu

elif (indeks_bulan == 2):
    nama_bulan = "Februari"
    m = indeks_bulan + 12
    hitung_tahun = input_tahun - 1  # ambil angka tahun lalu

else:
    print("Input angka 1 hingga 12 saja.")
    sys.exit()

# 5. Input tanggal
print("\nInput angka tanggal antara 1 hingga 31.")
input_tanggal = int(input("Input tanggal (mis. 21): "))

# 6. Validasi tanggal
# 6a. Validasi tanggal untuk bulan Februari tahun kabisat
if ((indeks_bulan == 2) 
    and (input_tahun % 4 == 0) 
    and (input_tahun % 100 != 0 or input_tahun % 400 == 0)):

    if (input_tanggal < 1) or (input_tanggal > 29):
        print("Input tanggal untuk bulan Februari tahun"
        "kabisat antara 1 hingga 29 saja.")
        sys.exit( )
    else:
        q = input_tanggal

#6b. Validasi tanggal untuk bulan Februari tahun bukan kabisat
if ((indeks_bulan == 2) and 
    (input_tahun % 4 != 0 
     or input_tahun % 100 == 0 
     and input_tahun % 400 != 0)):
    
    if (input_tanggal < 1) or (input_tanggal > 28):
        print("Input tanggal untuk bulan Februari tahun bukan" 
              "kabisat antara 1 hingga 28 saja.")
        sys.exit( )
    else:
        q = input_tanggal

#6c. Validasi tanggal untuk bulan dengan 30 hari
if (indeks_bulan == 4 
    or indeks_bulan == 6 
    or indeks_bulan == 9 
    or indeks_bulan == 11):
    
    if (input_tanggal < 1) or (input_tanggal > 30):
        print(f"Input tanggal untuk bulan {nama_bulan}"
              "antara 1 hingga 30 saja.")
        sys.exit( )
    else:
        q = input_tanggal

#6d. Validasi tanggal untuk bulan dengan 31 hari
if (indeks_bulan == 1 
    or indeks_bulan == 3 
    or indeks_bulan == 5 
    or indeks_bulan == 7 
    or indeks_bulan == 8 
    or indeks_bulan == 10 
    or indeks_bulan == 12):
    if (input_tanggal < 1) or (input_tanggal > 31):
        print(f"Input tanggal untuk bulan {nama_bulan}"
              "antara 1 hingga 31 saja.")
        sys.exit( )
    else:
        q = input_tanggal

#6e. Validasi untuk input sebelum tanggal 15 Oktober 1582
if (input_tahun == 1582) and (indeks_bulan == 10) and (input_tanggal < 15):
    print("Input tanggal sebelum 15 Oktober 1582 tidak valid.")
    sys.exit( )

# 7. Hitung indeks K
K = hitung_tahun % 100

# 8. Hitung indeks J
J = hitung_tahun // 100

# 9. Hitung indeks h
h = (q + (13 * (m + 1)) // 5 + K + (K // 4) + (J // 4) - (2 * J)) % 7

# 10. Tentukan nama hari
if (h == 0):
    nama_hari = "Sabtu"
elif (h == 1):
    nama_hari = "Minggu"
elif (h == 2):
    nama_hari = "Senin"
elif (h == 3):
    nama_hari = "Selasa"
elif (h == 4):
    nama_hari = "Rabu"
elif (h == 5):
    nama_hari = "Kamis"
elif (h == 6):
    nama_hari = "Jumat"

# 11. Tampilkan nama hari
print(f"\nTanggal {input_tanggal} {nama_bulan} {input_tahun} "
      f"adalah hari {nama_hari}.")
