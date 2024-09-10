# =============================================================================================================
# Programming Exercise 01.17
# Oleh      : #bayuyudhasaputra
# Sumber    : https://media.pearsoncmg.com/bc/abp/cs-resources/products/product.html#product,isbn=0133050556
# -------------------------------------------------------------------------------------------------------------
# 01.17. Turtle: draw a line
#   Write a program that draws a red line connecting two points (-39, 48) 
#   and (50, -50) and displays the coordinates of the two points, as shown in:
#   
# ==============================================================================================================

import turtle # import modul turtle

turtle.penup()              # angkat pena
turtle.goto(-39, 48)        # tempatkan ke titik (-39, 48))
turtle.pendown()            # turunkan pena
turtle.write("(-39, 48)")   # tuliskan teks "(-39, 48)"   
turtle.goto(50, -50)        # tempatkan ke titik (50, -50)
turtle.write("(50, -50)")    # tuliskan teks "(50, -50)"

turtle.done()