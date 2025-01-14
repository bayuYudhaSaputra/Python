'''
====================================================
0206. Jumlah Digit Bilangan Ratusan
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan program yang meminta input bilangan antara 
0 hingga 1000. Kemudian, jumlahkan digit ratusan, 
puluhan dan satuan dari bilangan ratusan ini.
Misal, pengguna menginput bilangan integer 932 maka 
program akan menentukan jumlah dari (9 + 3 + 2). 
Hasil dari penjumlahan ini adalah 14.
(Petunjuk : gunakan operator % untuk mengekstrak 
digit ratusan, puluhan dan satuan. Kemudian, 
gunakan operator // untuk menghapus hasil ekstraksi. 
Misal, 932 % 10 = 2 dan 932 // 10 = 93)
====================================================
'''

# 1. Input bilangan ratusan
bilangan = eval(input("Input bilangan ratusan : "))

# 2. Ekstrak ratusan
digitRatusan = bilangan // 100
sisaRatusan = bilangan % 100

# 3. Ekstrak puluhan
digitPuluhan = sisaRatusan // 10

# 4. Ekstrak satuan
digitSatuan = sisaRatusan % 10

# 5. Jumlahkan digit ratusan, puluhan, satuan
jumlahDigit = digitRatusan + digitPuluhan + digitSatuan

# 6. Tampilkan hasil penjumlahan digit-digit
print("Jumlah digit-digit dari bilangan", 
      bilangan, "adalah", jumlahDigit)