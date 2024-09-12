# =============================================================================================================
# Programming Exercise 01.21
# Oleh      : #bayuyudhasaputra
# Sumber    : https://media.pearsoncmg.com/bc/abp/cs-resources/products/product.html#product,isbn=0133050556
# -------------------------------------------------------------------------------------------------------------
# 01.21. Turtle: display a clock
#   Write a program that displays a clock to show the time 9:15:00, 
#   as shown in
#   
# ==============================================================================================================

import turtle # import modul turtle

# 1. Buat lingkaran
turtle.penup()              # angkat pena
turtle.goto(5,-100)         # tempatkan ke titik (0, -100)
turtle.pendown()            # turunkan pena
turtle.circle(100)          # buat lingkaran dengan jari-jari 100

# 2. Tambahkan tulisan 12
turtle.penup()              # angkat pena
turtle.goto(5, 80)          # tempatkan ke titik (0, 80)
turtle.pendown()            # turunkan pena
turtle.write("12")          # tulis angka "12"

# 3. Tambahkan tulisan 3
turtle.penup()              # angkat pena
turtle.goto(85, 0)          # tempatkan ke titik (80, 0)
turtle.pendown()            # turunkan pena
turtle.write("3")           # tulis angka "3"

# 4. Tambahkan tulisan 6
turtle.penup()              # angkat pena
turtle.goto(5, -90)         # tempatkan ke titik (0, -80)
turtle.pendown()            # turunkan pena
turtle.write("6")           # tulis angka "6"

# 5. Tambahkan tulisan 9
turtle.penup()              # angkat pena
turtle.goto(-85, 0)         # tempatkan ke titik (-80, 0)
turtle.pendown()            # turunkan pena
turtle.write("9")           # tulis angka "9"

# 6. buat jarum pendek
turtle.penup()              # angkat pena
turtle.goto(0, 0)           # tempatkan ke titik (0, 0)
turtle.pendown()            # turunkan pena
turtle.goto(-60, 5)         # Buat garis antara (0,0) hingga (-60, 5)

# 7. buat jarum panjang
turtle.penup()              # angkat pena
turtle.goto(0, 0)           # tempatkan ke titik (0, 0)
turtle.pendown()            # turunkan pena
turtle.goto(70, 5)          # Buat garis antara (0,0) hingga (70, 5)

# 8. buat tulisan 09:15:00
turtle.penup()               # angkat pena
turtle.goto(-20, -130)       # tempatkan ke titik (0, 0)
turtle.pendown()             # turunkan pena            
turtle.write("09:15:00")     # tulis angka "09:15:00"

# 9. tempatkan pena ke titik (0,0)
turtle.penup()               # angkat pena
turtle.left(90)              # Putar 90 derajat ke kiri
turtle.goto(0,0)             # tempatkan ke titik (0, 0)
turtle.pendown()             # turunkan pena

turtle.done()