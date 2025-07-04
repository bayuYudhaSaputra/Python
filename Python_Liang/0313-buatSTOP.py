'''
=============================================================================================================
Programming Exercise 03.13
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel/dp/0132747189
-------------------------------------------------------------------------------------------------------------
03.13. Membuat Tanda STOP
    (Tuliskan soal di sini)
==============================================================================================================
'''

import turtle # import modul turtle

# 1. Buat bangun bangun Segienam beraturan
turtle.penup()
turtle.goto(-200,0)
turtle.pendown()
turtle.begin_fill() # Tanda awal diwarnai
turtle.color("red") # Warna bangun

# 1a. Sisi ke-1
turtle.right(60)
turtle.forward(200)

# 1b. Sisi ke-2
turtle.left(60)
turtle.forward(200)

# 1c. Sisi ke-3
turtle.left(60)
turtle.forward(200)

# 1d. Sisi ke-4
turtle.left(60)
turtle.forward(200)

# 1e. Sisi ke-5
turtle.left(60)
turtle.forward(200)

# 1f. Sisi ke-6
turtle.left(60)
turtle.forward(200)

turtle.end_fill() # Tanda akhir pewarnaan


# 2. Tulis STOP
turtle.penup()
turtle.goto(-140,-60)
turtle.pendown()
turtle.begin_fill()
turtle.color("white")
turtle.write("STOP", font= ("Arial", 81, "normal"))
turtle.end_fill()

turtle.hideturtle() # sembunyikan turtle



turtle.done()