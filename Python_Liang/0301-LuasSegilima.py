'''
    ======================================================================
    03.01. Hitung Luas Segitima Beraturan
    Oleh: #bayuyudhasaputra
    ----------------------------------------------------------------------
    Tuliskan program yang menampilkan luas segilima serta luasnya dimana
    pengguna menginput jarak antara titik sudut dengan titik pusat
    segilima
    ======================================================================
'''
import turtle
import math

# 1. Input jarak titik pusat ke titik sudut (r)
r = eval(input("Input jarak titik pusat ke titik sudut segilima: "))
PI = math.pi

# 2. Hitung luas segilima
luas = ((5 * r ** 2) / 2) * math.sin((2 * PI) / 5)
luas = format(luas, ".2f") #dibulatkan 2 angka desimal
output_luas = "Luas segilima adalah " + str(luas)

# 3. Gambar segilima
# 3a. Membuat segilima
turtle.penup()
turtle.goto(0, -r)
turtle.pendown()
turtle.color("blue") # sisi berwarna biru
turtle.circle(r, steps = 5) # membuat segilima beraturan

# 3b. Menulis pesan
turtle.penup()
turtle.goto(-r, (-r - 50))
turtle.write(output_luas)
turtle.hideturtle() # turtle disembunyikan

turtle.done() # layar turtle berhenti.


# 4 Tampilkan luas segilima
print(output_luas)
