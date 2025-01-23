'''
====================================================
0208. Menghitung jumlah energi untuk memanaskan air
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan program untuk menghitung jumlah energi 
yang dibutuhkan untuk memanaskan air dari suhu 
tertentu ke suhu akhir. Program meminta pengguna 
untuk menginput nilai massa air (dalam satuan Kg), 
suhu awal dan suhu akhir.
====================================================
'''

massa = eval(input("Input massa air yang dipanaskan (dalam Kg) : "))
suhu_awal = eval(input("Input suhu awal air (dalam derajat celsius) : "))
suhu_akhir = eval(input("Input suhu akhir air (dalam derajat celsius) : "))

energi = massa * (suhu_akhir - suhu_awal) * 4184

print("Energi yang dibutuhkan untuk memanaskan ", 
      massa, "Kg air, dari", suhu_awal, "derajat celsius hingga", suhu_akhir,
      "derajat celsius adalah", energi, "joule."
      )