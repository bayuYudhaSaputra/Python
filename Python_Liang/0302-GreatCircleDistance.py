'''
    ===========================================
    03.02. Great Circle Distance
    Oleh : #bayuyudhasaputra
    -------------------------------------------
    Great circle distance adalah jarak antar
    dua titik pada bidang lengkung, seperti
    permukaan bumi.
    Misal, (x1, y1) adalah latitude dan
    longitude pada titik pertama. Dan, (x2, y2)
    adalah latitude dan longitude pada titik
    kedua. x1 dan x2 bernilai positif jika ke
    arah utara dan negatif jika ke selatan. y1
    dan y2 bernilai positif jika ke barat, dan
    bernilai negatif jika ke timur.Buatlah
    program menentukan great circle distance
    di antara dua titik. Jika pengguna menginput
    kedua titik tersebut.

    ===========================================
'''

import math

# 1. Input latitude titik 1 dalam derajat
x1 = eval(input("Input latitude titik 1 dalam derajat : "))
x1 = math.radians(x1)

# 2. Input longitude titik 1 dalam derajat
y1 = eval(input("Input longitude titik 1 dalam derajat: "))
y1 = math.radians(y1)

# 3. Input latitude titik 2 dalam derajat
x2 = eval(input("Input latitude titik 2 dalam derajat : "))
x2 = math.radians(x2)

# 4. Input longitude titik 2 dalam derajat
y2 = eval(input("Input longitude titik 2 dalam derajat : "))
y2 = math.radians(y2)

# 5. Hitung Great Circle Distance (GCD)
radius = 6371.01
gcd = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) + math.cos(y1 - y2))

# 6. Tampilkan GCD
print("Jarak titik 1 dengan titik 2 adalah",
       gcd, "Km")

