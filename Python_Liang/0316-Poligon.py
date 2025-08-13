'''
=============================================================================================================
Programming Exercise 03.16
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel/dp/0132747189
-------------------------------------------------------------------------------------------------------------
03.16. Membuat Poligon
   Buatlah segitiga, segiempat, segilima, segienam dan segidelapan beraturan dengan
   sisi bawah sejajar sumbu-x. Poligon-poligon ini diberi warna yang berbeda.
==============================================================================================================
'''

import turtle # import modul turtle

turtle.pensize(2)

# 1. Buat segitiga sama sisi
turtle.penup()
turtle.goto(-400, -100)
turtle.pendown()
turtle.begin_fill()
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.left(120)
turtle.forward(100)
turtle.fillcolor("red")
turtle.end_fill()
turtle.left(120) # kursor dikembalikan ke arah kanan

# 2. Buat persegi
turtle.penup()
turtle.goto(-275, -100)
turtle.pendown()
turtle.begin_fill()
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.left(90)
turtle.forward(100)
turtle.fillcolor("#FFA500")
turtle.end_fill()
turtle.left(90) # Kursor dikembalikan ke arah kanan

# 3. Buat segilima beraturan
turtle.penup()
turtle.goto(-100, -100)
turtle.pendown()
turtle.begin_fill()
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.left(72)
turtle.forward(100)
turtle.fillcolor("yellow")
turtle.end_fill()
turtle.left(72) # Kursor dikembalikan ke arah kanan

# 4. Buat segienam beraturan
turtle.penup()
turtle.goto(100, -100)
turtle.pendown()
turtle.begin_fill()
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.left(60)
turtle.forward(100)
turtle.fillcolor("green")
turtle.end_fill()
turtle.left(60) # Kursor dikembalikan ke arah kanan

# 5. Buat segi delapan beraturan
turtle.penup()
turtle.goto(400, -100)
turtle.pendown()
turtle.begin_fill()
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.left(45)
turtle.forward(100)
turtle.fillcolor("blue")
turtle.end_fill()
turtle.left(45)


turtle.done()