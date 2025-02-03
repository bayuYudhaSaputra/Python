'''
====================================================
0210. Menghitung temperatur windchill
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan program yang meminta input kecepatan v 
dalam satuan m/sekon (m/s) dan percepatan a (m/s2). 
Program menampilkan panjang minimum runway
====================================================
'''

kecepatan_pesawat = eval(input("Input kecepatan pesawat dalam satuan meter per sekon : "))
percepatan_pesawat = eval(input("Input percepatan pesawat dalam satuan meter per sekon kuadrat : "))

panjang_runway = (kecepatan_pesawat ** 2) / (2 * percepatan_pesawat)

print("Panjang runway minimum untuk pesawat", 
      "dengan kecepatan", kecepatan_pesawat, "m/s",
      "dan percepatan", percepatan_pesawat, "m/s kuadrat",
      "adalah: ", panjang_runway, "m."
      )