'''
=============================================================================================================
Programming Exercise 03.15
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel/dp/0132747189
-------------------------------------------------------------------------------------------------------------
03.15. Emoji Senyum
    Buatlah program untuk menggambar emoji senyum
==============================================================================================================
'''

import turtle # import modul turtle

turtle.pensize(5)

# 1. Buat kepala
turtle.penup()
turtle.goto(0,-100)
turtle.pendown()
turtle.begin_fill()
turtle.circle(100)
turtle.fillcolor("yellow")
turtle.end_fill()

# 2. Buat mata ke-1
turtle.penup()
turtle.goto(-30,20)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.fillcolor("black")
turtle.end_fill()

# 3. Buat mata ke-2
turtle.penup()
turtle.goto(30,20)
turtle.pendown()
turtle.begin_fill()
turtle.circle(10)
turtle.fillcolor("black")
turtle.end_fill()

# 4. Buat mulut
turtle.penup()
turtle.goto(-45, -45)
turtle.pendown()
turtle.goto(0,-70)
turtle.goto(45,-45)

# 5. Buat hidung
turtle.penup()
turtle.goto(-35,-35)
turtle.pendown()
turtle.goto(0,10)
turtle.goto(35,-35)


turtle.hideturtle()
turtle.done()