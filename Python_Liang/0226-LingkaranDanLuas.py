'''
====================================================
0223. Proyeksi Populasi
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan progran yang menawarkan prompt kepada 
pengguna untuk menginput jari-jari lingkaran. 
Kemudian, program menggambar 4 lingkaran di 
bagian tengah layar 
====================================================
'''
import turtle # import modul turtle
import math # import modul math

# 1. Input jari-jari lingkaran
jari2 = eval(input("Input jari-jari lingkaran : "))

# 2. Buat lingkaran
turtle.penup()
turtle.goto(0, -jari2)
turtle.pendown()
turtle.circle(jari2)

# 3. Hitung luas lingkaran
luas = math.pi * jari2 ** 2
pesan_luas = "Luas = " + str(luas)

# 4. Tulis luas lingkaran
turtle.penup()
turtle.goto(- jari2, - (jari2 * 3 / 2))
turtle.write(pesan_luas)

turtle.done()