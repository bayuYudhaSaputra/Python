'''
    ======================================================================
    03.01. Hitung Luas Segitima Beraturan
    Oleh: #bayuyudhasaputra
    ----------------------------------------------------------------------
    Tuliskan program yang menampilkan luas segilima serta luasnya dimana
    pengguna menginput jarak antara titik sudut dengan titik pusat
    segilima
    ======================================================================
'''
import turtle
import math

# 1. Input jarak titik pusat ke titik sudut (r)
r = eval(input("Input jarak titik pusat ke titik sudut segilima: "))
PI = math.pi

# 2. Hitung luas segilima
luas = ((5 * r ** 2) / 2) * math.sin((2 * PI) / 5)

# 3. Gambar segilima
turtle.color("blue")
turtle.penup()


# 4 Tampilkan luas segilima
print("Luas segilima adalah ", luas)
