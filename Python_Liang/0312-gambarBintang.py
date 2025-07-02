'''
===============================================================================================
Programming Exercise 03.12
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel/dp/0132747189
------------------------------------------------------------------------------------------------
03.12. Menggambar Bintang
    Tuliskan program untuk menggambar bentuk bintang seperti gambar 03.12.01. Panjang sisi dari 
    bintang ini diinput oleh pengguna.
    (Petunjuk : besar sudut pusat bintang adalah 36o)

=================================================================================================
'''

import turtle # import modul turtle

# 1. Input panjang sisi bintang
sisi = eval(input("Input panjang sisi bintang : "))

# 2. Menentukan titik awal
turtle.penup()
turtle.goto(-(sisi / 2), 0)
turtle.pendown()

# 3. Buat sisi ke-1
turtle.forward(sisi)
turtle.right(144)

# 4. Buat sisi ke-2
turtle.forward(sisi)
turtle.right(144)

# 5. Buat sisi ke-3
turtle.forward(sisi)
turtle.right(144)

# 6. Buat sisi ke-4
turtle.forward(sisi)
turtle.right(144)

# 7. Buat sisi ke-5
turtle.forward(sisi)
turtle.right(144)

turtle.done()