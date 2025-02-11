'''
====================================================
0213. Mengurutkan Terbalik Bilangan Ribuan
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan program yang meminta input kepada pengguna 
untuk menginput bilangan 4 digit. Kemudian, 
program menampilkan angka-angka dengan urutan 
terbalik.
====================================================
'''

# 1. Meminta input bilangan ribuan
bilangan = eval(input("Input bilangan 4 digit (Mis. 3125) : "))

# Ekstrak angka ribuan
ribuan = bilangan // 1000

# Ambil 3 digit terakhir
sisaRibuan = bilangan % 1000

# Ekstrak angka ratusan
ratusan = sisaRibuan // 100

# Ambil 2 digit terakhir
sisaRatusan = sisaRibuan % 100

# Ekstrak angka puluhan
puluhan = sisaRatusan // 10

# Ekstrak angka satuan
satuan = sisaRatusan % 10

# Konversi ke string
ribuan = str(ribuan)
ratusan = str(ratusan)
puluhan = str(puluhan)
satuan = str(satuan)

# Urutkan terbalik
bilanganTerbalik = satuan + puluhan + ratusan + ribuan

print("Urutan terbalik dari bilangan", bilangan, "adalah", bilanganTerbalik)
