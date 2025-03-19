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

# 1. Input jari-jari lingkaran
jari2 = eval(input("Input jari-jari lingkaran : "))

# 2. Buat lingkaran 1
turtle.penup()
turtle.goto(- jari2, jari2)
turtle.pendown()
turtle.circle(jari2)

# 3. Buat lingkaran 2
turtle.penup()
turtle.goto(- jari2, - jari2)
turtle.pendown()
turtle.circle(jari2)

# 4. Buat lingkaran 3
turtle.penup()
turtle.goto(jari2, - jari2)
turtle.pendown()
turtle.circle(jari2)

# 5. Buat lingkaran 4
turtle.penup()
turtle.goto(jari2, jari2)
turtle.pendown()
turtle.circle(jari2)

turtle.done()