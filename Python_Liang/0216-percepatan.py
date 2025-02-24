'''
====================================================
0216. Percepatan
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan program yang menampilkan percepatan 
rata-rata (dalam satuan meter per sekon kuadrat) 
jika pengguna menginput kecepatan v1 dan v0 
(dalam satuan meter per sekon) dan selang waktu t 
dalam satuan sekon
====================================================
'''

# 1. Input kecepatan awal, akhir dan selang waktu
v0 = eval(input("Input kecepatan awal dalam satuan meter per sekon : "))
v1 = eval(input("Input kecepatan akhir dalam satuan meter per sekon : "))
t  = eval(input("Input selang waktu dalam satuan sekon : "))

# 2. Hitung percepatan
a = (v1 - v0) / t

# Tampilkan percepatan
print("Percepatan rata-rata benda dengan,\n",
      "\t kecepatan awal", v0, "m/s \n",
      "\t kecepatan akhir", v1, "m/s \n",
      "\t selang waktu", t, "sekon \n",
      "adalah", a, "meter per sekon kuadrat.\n"
      )