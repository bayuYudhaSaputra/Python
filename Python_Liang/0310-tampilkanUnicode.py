'''
=============================================================================================================
Programming Exercise 03.10
Oleh      : #bayuyudhasaputra
Sumber    : https://media.pearsoncmg.com/bc/abp/cs-resources/products/product.html#product,isbn=0133050556
-------------------------------------------------------------------------------------------------------------
03.10. Tampilkan Unicode
Tampilkan huruf Yunani dengan kode:
\u03b1 \u03b2 \u03b3 \u03b4 \u03b5 \u03b6 \u03b7 \u03b8
pada layar Turtle.
# ==============================================================================================================
'''

import turtle # import modul turtle

# 1. buat huruf alpha
turtle.penup()
turtle.goto(-30,0)
turtle.pendown()
turtle.write("\u03b1")

# 2. buat huruf beta
turtle.penup()
turtle.goto(-20,0)
turtle.pendown()
turtle.write("\u03b2")

# 3. Buat huruf gamma
turtle.penup()
turtle.goto(-10,0)
turtle.pendown()
turtle.write("\u03b3")

# 4. Buat huruf delta
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.write("\u03b4")

# 5. Buat huruf epsilon
turtle.penup()
turtle.goto(10,0)
turtle.pendown()
turtle.write("\u03b5")

# 6. Buat huruf zeta
turtle.penup()
turtle.goto(20,0)
turtle.pendown()
turtle.write("\u03b6")

# 7. Buat huruf eta
turtle.penup()
turtle.goto(30,0)
turtle.pendown()
turtle.write("\u03b7")

# 8. Buat huruf theta
turtle.penup()
turtle.goto(40,0)
turtle.pendown()
turtle.write("\u03b8")

turtle.done()