'''
====================================================
0214. Hitung Luas Segitiga
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan program yang meminta input 3 titik kepada p
engguna, yaitu (x1, y1),  (x2, y2),  dan (x3, y3). 
Titik-titik yang diinput ini adalah titik sudut 
segitiga. 
====================================================
'''

# 1. Input titik-titik sudut segitiga
# 1a. Titik A
x_a = eval(input("Input absis titik A : "))
y_a = eval(input("Input ordinat titik A : "))

# 1b. Titik B
x_b = eval(input("Input absis titik B :"))
y_b = eval(input("Input ordinat titik B : "))

# 1c. Titik C
x_c = eval(input("Input absis titik C : "))
y_c = eval(input("Input ordinat titik C : "))

# 2. Menentukan panjang sisi segitiga
# 2a. sisi a
sisi_a = ((x_c - x_b) ** 2 + (y_c - y_b) ** 2) ** (1 / 2)

# 2b. sisi b
sisi_b = ((x_b - x_a) ** 2 + (y_b - y_a) ** 2) ** (1 / 2)

# 2c. sisi c
sisi_c = ((x_c - x_a) ** 2 + (y_c - y_a) ** 2) ** (1 / 2)

# 3. Menentukan setengah keliling (s)
s = (sisi_a + sisi_b + sisi_c) / 2

# 4. Menentukan luas segitiga
luas = (s * (s - sisi_a) * (s - sisi_b) * (s - sisi_c)) ** (1 / 2)

# 5 Tampilkan luas segitiga
print("Luas segitiga dengan titik sudut",
      "A(", x_a, "," , y_a, "), ",
      "B(", x_b, ",", y_b, "), ",
      "C(", x_c, ",", y_c, ")",
      "adalah", luas
      )