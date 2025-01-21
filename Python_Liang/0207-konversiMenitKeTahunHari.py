'''
====================================================
0207. Konversi Menit Ke Tahun Lebih Beberapa Hari
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan program yang menawarkan prompt kepada 
pengguna untuk menginput selang waktu dalam satuan 
menit. Program mengonversi satuan menit ini ke 
tahun lebih beberapa hari. Untuk menyederhanakan 
perhitungan, asumsikan 1 tahun sama dengan 365 hari.
====================================================
'''

# 1. Input nilai waktu dalam menit
nilaiMenit = eval(input("Input selang waktu dalam satuan menit: "))

# 2. Konversi waktu dalam menit menjadi tahun
nilaiTahun = nilaiMenit // (365 * 24 * 60)

# 3. tentukan sisa pembagian nilaiMenit
sisaMenit = nilaiMenit % (365 * 24 * 60)

# 4. Konversi sisaMenit menjadi hari
nilaiHari = sisaMenit // (24 * 60)

# 5. Tampilkan hasil konversi
print(nilaiMenit, " menit kira-kira sama dengan ", 
      nilaiTahun, "tahun lebih", nilaiHari, "hari.")
