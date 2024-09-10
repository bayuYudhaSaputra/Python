# =============================================================================================================
# Programming Exercise 01.12
# Oleh      : #bayuyudhasaputra
# Sumber    : https://media.pearsoncmg.com/bc/abp/cs-resources/products/product.html#product,isbn=0133050556
# -------------------------------------------------------------------------------------------------------------
# 01.12. Turtle: draw four squares
#   Write a program that draws four squares in the center of the screen, as shown in:
#   https://photos.app.goo.gl/LTZpJL8ha2JtbqKu8
# ==============================================================================================================

import turtle # import modul turtle

# 1. Buat persegi besar
turtle.penup()          # angkat pena
turtle.goto(-100, 100)  # tempatkan ke titik (-100, 100)
turtle.pendown()        # turunkan pena
turtle.forward(200)     # gambar garis 200px
turtle.right(90)        # arahkan 90 derajat ke kanan
turtle.forward(200)     # gambar garis 200px
turtle.right(90)        # arahkan 90 derajat ke kanan
turtle.forward(200)     # gambar garis 200px
turtle.right(90)        # arahkan 90 derajat ke kanan
turtle.forward(200)     # gambar garis 200px

# 2. Bagi persegi secara horizontal
turtle.penup()          # angkat pena
turtle.right(90)        # arahkan 90 derajat ke kanan
turtle.goto(-100, 0)    # tempatkan ke titik (0, -100)
turtle.pendown()        # turunkan pena
turtle.forward(200)     # gambar garis 200px

# 3. Bagi persegi secara vertikal
turtle.penup()          # angkat pena
turtle.right(90)        # arahkan 90 derajat ke kanan
turtle.goto(0, 100)     # tempatkan ke titik (0, -100)
turtle.pendown()        # turunkan pena
turtle.forward(200)     # gambar garis 200px


turtle.done()