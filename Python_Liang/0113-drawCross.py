# =============================================================================================================
# Programming Exercise 01.13.
# Oleh      : #bayuyudhasaputra
# Sumber    : https://media.pearsoncmg.com/bc/abp/cs-resources/products/product.html#product,isbn=0133050556
# -------------------------------------------------------------------------------------------------------------
# 01.13. Turtle: draw a cross
#   Write a program that draws a cross as shown here:
#   https://photos.app.goo.gl/L32s96eHqA49DXSp8
# ==============================================================================================================

import turtle # import modul turtle

# 1. Buat sumbu-y
turtle.penup() # angkat pena
turtle.goto(0, 200) # tempatkan ke titik (0, 200)
turtle.right(90) # arahkan ke bawah
turtle.pendown() # turunkan pena
turtle.forward(400) # buat garis 400px ke bawah

# 2. Buat sumbu-x
turtle.penup() # angkat pena
turtle.goto(-200, 0) # tempatkan ke titik (-200, 0)
turtle.left(90) # arahkan ke kanan
turtle.pendown() # turunkan pena
turtle.forward(400) # buat garis 400px ke kanan

# 3. Buat tulisan O di titik (10,-20)
turtle.penup() # angkat pena
turtle.goto(10, -20) # pindahkan pena ke titik (10, -20)
turtle.pendown() #turunkan pena
turtle.write("O") # tuliskan "O"

# 4. Buat tulisan Y di titik (0, 205)
turtle.penup() # angkat pena
turtle.goto(0, 205) # pindahkan pena ke titik (0, 205)
turtle.pendown() # turunkan pena
turtle.write("y") # tuliskan "y"

# 5. Buat tulisan X di titik (205, 0)
turtle.penup() # angkat pena
turtle.goto(205, 0) # pindahkan pena ke titik (205, 0)
turtle.pendown() # turunkan pena
turtle.write("x") # tuliskan "x"

turtle.done()