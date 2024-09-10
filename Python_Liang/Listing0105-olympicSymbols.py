# =============================================================================================================
# Programming Exercise xx.xx
# Oleh      : #bayuyudhasaputra
# Sumber    : https://media.pearsoncmg.com/bc/abp/cs-resources/products/product.html#product,isbn=0133050556
# -------------------------------------------------------------------------------------------------------------
# xx.xx. Judul Exercise
#   (Tuliskan soal di sini)
# ==============================================================================================================

import turtle # import modul turtle

# 1. Buat lingkaran biru
turtle.color("blue") # ubah warna biru
turtle.penup() # angkat pena
turtle.goto(-110, -25) # tempatkan ke titik (-110, -50)
turtle.pendown() # turunkan pena
turtle.circle(45) # buat lingkaran dengan jari-jari 45px

# 2. Buat lingkaran hitam
turtle.color("black") # ubah warna hitam
turtle.penup() # angkat pena
turtle.goto(0, -25) # tempatkan ke titik (0, -25)
turtle.pendown() # turunkan pena
turtle.circle(45) # buat lingkaran dengan jari-jari 45px

# 3. Buat lingkaran merah
turtle.color("red") # ubah warna merah
turtle.penup() # angkat pena
turtle.goto(110, -25) # tempatkan ke titik (110, -25)
turtle.pendown() # turunkan pena
turtle.circle(45) # buat lingkaran dengan jari-jari 45px

# 4. Buat lingkaran kuning
turtle.color("yellow") # ubah warna kuning
turtle.penup() # angkat pena
turtle.goto(-55, -75) # tempatkan ke titik (-55, -75)
turtle.pendown() # turunkan pena
turtle.circle(45) # buat lingkaran dengan jari-jari 45px

# 5. Buat lingkaran hijau
turtle.color("green") # ubah warna hijau
turtle.penup() # angkat pena
turtle.goto(55, -75) # tempatkan ke titik (55, -75)
turtle.pendown() # turunkan pena
turtle.circle(45) # buat lingkaran dengan jari-jari 45px

# 6. Hentikan program turtle
turtle.done()