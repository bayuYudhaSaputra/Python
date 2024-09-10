# =============================================================================================================
# Programming Exercise 01.15.
# Oleh      : #bayuyudhasaputra
# Sumber    : https://media.pearsoncmg.com/bc/abp/cs-resources/products/product.html#product,isbn=0133050556
# -------------------------------------------------------------------------------------------------------------
# 01.15. Turtle: draw two triangles
#   Write a program that draws two triangles as shown in
#   https://photos.app.goo.gl/rbq1pJe2mE28jhKm9
# ==============================================================================================================

import turtle # import modul turtle

turtle.right(60)    # arahkan 60 derajat ke kanan
turtle.forward(100) # buat garis 100px
turtle.right(120)   # arahkan 120 derajat ke kanan
turtle.forward(100) # buat garis 100px
turtle.right(120)   # arahkan 120 derajat ke kanan
turtle.forward(200) # buat garis 200px
turtle.left(120)    # arahkan 120 derajat ke kiri
turtle.forward(100) # buat garis 100px
turtle.left(120)    # arahkan 120 derajat ke kiri
turtle.forward(100) # buat garis 100px

turtle.done()