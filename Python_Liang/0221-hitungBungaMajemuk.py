'''
====================================================
0221. Hitung Bunga Majemuk
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan program yang menampilkan jumlah tabungan 
seseorang dalam 6 bulan, jika orang tersebut selalu 
menabung dengan nominal yang sama. Program meminta 
input jumlah nominal tabungan per bulan dan 
diketahui persentase bunga tahunan sebesar 
5% per tahun!
====================================================

'''

# 1. Input nominal setoran rutin bulanan
setoran_rutin = eval(input("Input setoran bulanan : Rp"))

# 2. Hitung jumlah setoran bulan ke-1
setoran_1 = setoran_rutin * (1 + 5 / 1200)

# 3. Hitung jumlah setoran bulan ke-2
setoran_2 = (setoran_1 + setoran_rutin) * (1 + 5 / 1200)

# 4. Hitung jumlah setoran bulan ke-3
setoran_3 = (setoran_2 + setoran_rutin) * (1 + 5 / 1200)

# 5. Hitung jumlah setoran bulan ke-4
setoran_4 = (setoran_3 + setoran_rutin) * (1 + 5 / 1200)

# 6. Hitung jumlah setoran bulan ke-5
setoran_5 = (setoran_4 + setoran_rutin) * (1 + 5 / 1200)

# 7. Hitung jumlah setoran bulan ke-6
setoran_6 = (setoran_5 + setoran_rutin) * (1 + 5 / 1200)

# 8. Tampilkan jumlah setoran
setoran_6 = round(setoran_6, 0)
print("Jumlah setoran setelah 6 bulan adalah: Rp", setoran_6)