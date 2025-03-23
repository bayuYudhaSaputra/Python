'''
====================================================
0226. Gambar Lingkaran dan Tampilkan Luasnya
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan program yang menawarkan prompt kepada
pengguna. Kemudian, program mennentukan luas lingkaran
ini dan menampilkan luasnya.
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