'''
====================================================
0214. Hitung Luas Segienam
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan program yang meminta input panjang sisi 
segienam beraturan. Kemudian, program menampilkan 
luas segienam tersebut!
====================================================
'''

# 1. Input sisi segienam
sisi = eval(input("Input panjang sisi segienam : "))

# 2. Hitung luas segienam
luas = (3 * (sisi ** 2) * (3 ** (1/2))) / 2

# 3. Tampilkan luas segienam
print("Luas segienam dengan panjang sisi", sisi,
      "adalah", luas, ".")