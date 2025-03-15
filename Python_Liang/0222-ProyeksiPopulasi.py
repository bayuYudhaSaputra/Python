'''
====================================================
0222. Proyeksi Populasi
Oleh : #bayuyudhasaputra
----------------------------------------------------
Hasil sensus penduduk dapat digunakan untuk melakukan
proyeksi jumlah populasi dengan asumsi sebagai berikut:
    1 kelahiran setiap 7 detik
    1 kematian setiap 13 menit
    1 imigran baru masuk setiap 45 menit
Tuliskan program yang menampilkan proyeksi jumlah penduduk 
berdasarkan jumlah penduduk awal dan berapa tahun proyeksi
ini diinput oleh pengguna!
====================================================
'''

# 1. Input jumlah penduduk awal.
jumlah_awal = eval(input("Input jumlah penduduk semula : "))

# 2. Input jumlah tahun proyeksi
tahun_proyeksi = eval(input("Input tahun proyeksi : "))

# 3. Hitung jumlah proyeksi kelahiran
proyeksi_kelahiran = tahun_proyeksi * ((365 * 24 * 3600) // 7)

# 4. Hitung jumlah proyeksi kematian
proyeksi_kematian = tahun_proyeksi * ((365 * 24 * 3600) // 13)

# 5. Hitung jumlah proyeksi imigran baru
proyeksi_imigran = tahun_proyeksi * ((365 * 24 * 3600) // 45)

# 6. Hitung hasil proyeksi
hasil_proyeksi = jumlah_awal + proyeksi_kelahiran - proyeksi_kematian + proyeksi_imigran

# 7. Tampilkan hasil proyeksi
print("Dalam", tahun_proyeksi, "tahun,",
      "Jumlah penduduk diperkirakan menjadi",
      hasil_proyeksi, "jiwa.")