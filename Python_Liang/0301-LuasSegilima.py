'''
    ======================================
    03.01. Hitung Luas Segitima Beraturan
    Oleh: #bayuyudhasaputra
    --------------------------------------
    Buatlah program menentukan luas segilima dimana pengguna menginput jarak titik pusat segilima dengan titik sudut dari segilima tersebut.
    ======================================
'''
import math

# 1. Input jarak titik pusat ke titik sudut
jarak_titik_pusat_sudut = eval(input("Input jarak titik pusat ke titik sudut segilima: "))

# 2. Hitung panjang sisi
panjang_sisi = 2 * jarak_titik_pusat_sudut * math.sin(math.pi / 5)

# 3. Hitung luas segilima
luas = (3 * math.sqrt(3) / 2) * pow(panjang_sisi, 2)

# 4 Tampilkan luas segilima
print("Luas segilima adalah ", luas)
