# =============================================================================================================
# Programming Exercise 01.20
# Oleh      : #bayuyudhasaputra
# Sumber    : https://media.pearsoncmg.com/bc/abp/cs-resources/products/product.html#product,isbn=0133050556
# -------------------------------------------------------------------------------------------------------------
# 01.20. Turtle: display a rectanguloid
#   Write a program that displays a rectanguloid, as shown in
#   
# ==============================================================================================================

import turtle # import modul turtle

# 1. Buat sisi frontal balok bagian depan
turtle.penup()              # angkat pena
turtle.goto(-100, -50)      # tempatkan ke titik A(-100, -50)
turtle.pendown()            # turunkan pena
turtle.goto(100, -50)       # tempatkan ke titik B(100, -50)
turtle.goto(100, 50)        # tempatkan ke titik C(100, 50)
turtle.goto(-100, 50)       # tempatkan ke titik D(-100, 50)
turtle.goto(-100, -50)      # tempatkan ke titik A(-100, -50)

# 2. Buat sisi frontal balok bagian belakang
turtle.penup()              # angkat pena
turtle.goto(-50, 0)         # tempatkan ke titik E(-50, 0)
turtle.pendown()            # turunkan pena
turtle.goto(150, 0)         # tempatkan ke titik F(150, 0)
turtle.goto(150, 100)       # tempatkan ke titik G(150, 100)
turtle.goto(-50, 100)       # tempatkan ke titik H(-50, 100)
turtle.goto(-50, 0)         # tempatkan ke titik E(-50, 0)

# 3. Buat rusuk AE
turtle.penup()              # angkat pena
turtle.goto(-100, -50)      # tempatkan ke titik A(-100, -50)
turtle.pendown()            # turunkan pena
turtle.goto(-50, 0)         # tempatkan ke titik E(-50, 0)

# 4. Buat rusuk BF
turtle.penup()              # angkat pena
turtle.goto(100, -50)       # tempatkan ke titik B(100, -50)
turtle.pendown()            # turunkan pena
turtle.goto(150, 0)         # tempatkan ke titik F(150, 0)

# 5. Buat rusuk CG
turtle.penup()              # angkat pena
turtle.goto(100, 50)        # tempatkan ke titik C(100, 50)
turtle.pendown()            # turunkan pena
turtle.goto(150, 100)       # tempatkan ke titik F(150, 100)

# 5. Buat rusuk DH
turtle.penup()              # angkat pena
turtle.goto(-100, 50)       # tempatkan ke titik D(-100, 50)
turtle.pendown()            # turunkan pena
turtle.goto(-50, 100)       # tempatkan ke titik F(-50, 100)

turtle.done()