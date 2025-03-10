'''
====================================================
0220. Hitung Bunga
Oleh : #bayuyudhasaputra
----------------------------------------------------
Buatlah program yang menampilkan besaran bunga 
yang ditagih pada bulan depan. Jika diketahui 
besaran modal dan persen bunga tahunan.
====================================================

'''
# 1. Input modal
modal = eval(input("Input bunga : Rp"))

# 2. Input persentase bunga tahunan
persen_bunga = eval(input("Input persentase bunga tahunan (Mis. 3 untuk 3%) : "))

# 3. Hitung nominal bunga bulanan
bunga_bulanan = modal * (persen_bunga / 1200)
bunga_bulanan = round(bunga_bulanan, 2)

# 4. Tampilkan nominal bunga
print("Nominal bunga bulanan adalah : Rp", bunga_bulanan)