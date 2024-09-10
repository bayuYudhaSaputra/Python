# =============================================================================================================
# Programming Exercise 01.16
# Oleh      : #bayuyudhasaputra
# Sumber    : https://media.pearsoncmg.com/bc/abp/cs-resources/products/product.html#product,isbn=0133050556
# -------------------------------------------------------------------------------------------------------------
# 01.16. Turtle: draw four circles
#   Write a program that draws four circles in the center of the screen, as shown in
#   https://photos.app.goo.gl/eCZj8f4g9kJXcvcv9
# ==============================================================================================================

import turtle # import modul turtle

# 1. Buat lingkaran 1
turtle.penup()          # angkat pena
turtle.goto(-50, 50)    # arahkan ke titik (-50, 50)
turtle.pendown()        # turunkan pena
turtle.circle(50)       # buat lingkaran berjari-jari 50px

# 2. Buat lingkaran 2
turtle.penup()          # angkat pena
turtle.goto(50, 50)     # arahkan ke titik (-50, 50)
turtle.pendown()        # turunkan pena
turtle.circle(50)       # buat lingkaran berjari-jari 50px

# 3. Buat lingkaran 3
turtle.penup()          # angkat pena
turtle.goto(50, -50)    # arahkan ke titik (50, -50)
turtle.pendown()        # turunkan pena
turtle.circle(50)       # buat lingkaran berjari-jari 50px

# 4, Buat lingkaran 4
turtle.penup()          # angkat pena
turtle.goto(-50, -50)   # arahkan ke titik (-50, -50)
turtle.pendown()        # turunkan pena
turtle.circle(50)       # buat lingkaran berjari-jari 50px

turtle.done()