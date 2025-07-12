'''
==============================================================================================
Programming Exercise 03.14
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel/dp/0132747189
-----------------------------------------------------------------------------------------------
03.14. Logo Olimpiade
    Tuliskan program yang menawarkan pengguna untuk menginput jari-jari lingkaran.
    Kemudian, program membuat logo Olimpiade yang terdiri dari 5 lingkaran berwarna 
    biru, hitam, merah, kuning dan hijau. Jari-jari setiap lingkaran ini sama. 
    Panjang jari-jari lingkaran-lingkaran ini sesuai dengan nilai diinput oleh pengguna.
=================================================================================================
'''

import turtle # import modul turtle

# 1. Input jari2 lingkaran
jari2 = eval(input("Input panjang jari-jari logo Olimpiade : "))
turtle.pensize(jari2 / 10) # atur ketebalan pena


# 2. Buat lingkaran pertama
x = -(23 / 10) * jari2 # absis posisi
y = (1 / 2) * jari2 # ordinat posisi
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.color("blue")
turtle.circle(jari2)

# 3. Buat lingkaran kedua
x = 0 * jari2 # absis posisi
y = (1 / 2) * jari2 # ordinat posisi
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.color("black")
turtle.circle(jari2)

# 4. Buat lingkaran ketiga
x = (23 / 10) * jari2 # absis posisi
y = (1 / 2) * jari2 # ordinat posisi
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.color("red")
turtle.circle(jari2)

# 5. Buat lingkaran keempat
x = -(12 / 10) * jari2 # absis posisi
y = -(1 / 2) * jari2 # ordinat posisi
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.color("yellow")
turtle.circle(jari2)

# 6. Buat lingkaran kelima
x = (12 / 10) * jari2 # absis posisi
y = -(1 / 2) * jari2 # ordinat posisi
turtle.penup()
turtle.goto(x,y)
turtle.pendown()
turtle.color("green")
turtle.circle(jari2)


turtle.hideturtle()

turtle.done()