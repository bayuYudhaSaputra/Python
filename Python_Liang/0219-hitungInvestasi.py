'''
====================================================
0219. Hitung Investasi
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan program yang menampilkan nilai akhir 
investasi jika pengguna menginput nilai nilai 
investasi awal, bunga tahunan dan jangka waktu 
investasi dalam satuan tahun.
====================================================

'''

# 1. Input nilai investasi awal, persentase bunga tahunan dan jangka waktu
nilaiAwal = eval(input("Input nilai awal investasi : Rp"))
bunga = eval(input("Input persentase bunga tahunan : "))
tahun = eval(input("Input jangka waktu investasi (dalam satuan tahun) : "))

# 2. Menentukan nilai akhir investasi.
nilaiAkhir = nilaiAwal * (1 + (bunga / 100)) ** tahun
nilaiAkhir = round(nilaiAkhir, 2)

# 3. Tampilkan hasil perhitungan nilai akhir investasi.
print("Nilai akhir investasi adalah Rp", nilaiAkhir)