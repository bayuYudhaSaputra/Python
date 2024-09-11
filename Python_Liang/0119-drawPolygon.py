# =============================================================================================================
# Programming Exercise 01.19
# Oleh      : #bayuyudhasaputra
# Sumber    : https://media.pearsoncmg.com/bc/abp/cs-resources/products/product.html#product,isbn=0133050556
# -------------------------------------------------------------------------------------------------------------
# 01.19. Turtle: draw a polygon
#   Write a program that draws a polygon that connects the points (40, -69.28), (-40, -69.28), 
#   (-80, -9.8), (-40, 69), (40, 69), and (80, 0) in this order, as shown in
#   
# ==============================================================================================================

import turtle # import modul turtle

turtle.penup()              # angkat pena
turtle.goto(40, -69.28)     # Tempatkan ke titik (40, -69.28)
turtle.pendown()            # turunkan pena
turtle.goto(-40, -69.28)    # Tempatkan ke titik (-40, -69.28)
turtle.goto(-80, -9.8)      # Tempatkan ke titik (-80, -9.8)
turtle.goto(-40, 69)        # Tempatkan ke titik (-40, 69)
turtle.goto(40, 69)         # Tempatkan ke titik (40, 69)
turtle.goto(80, 0)          # Tempatkan ke titik (80, 0)
turtle.goto(40, -69.28)     # tempatkan ke titik (40, -69.28)

turtle.done()