'''
    ===========================================
    03.03. Luas 4 Titik Geografis
    Oleh : #bayuyudhasaputra
    -------------------------------------------
    Temukan latitude dan longitude dari kota:
    - Atlanta
    - Orlando
    - Savannah
    - Charlotte
    Hitung luas yang melingkupi keempat kota
    tersebut!
    ===========================================
'''
import math

#  1. Latitude dan longitude Atlanta (1)
x1 = 33.753746
y1 = -84.386330
x1 = math.radians(x1)
y1 = math.radians(y1)

#  2. Latitude dan longitude Orlando (2)
x2 = 28.538336
y2 = -81.379234
x2 = math.radians(x2)
y2 = math.radians(y2)

#  3. Latitude dan longitude Savannah (3)
x3 = 32.0809263
y3 = -81.0911768
x3 = math.radians(x3)
y3 = math.radians(y3)

#  4. Latitide dan Longitude Charlotte (4)
x4 = 35.227085
y4 = -80.843124
x4 = math.radians(x4)
y4 = math.radians(y4)

radius = 6371.01 # radius rata-rata bumi

#  5. Jarak Atlanta dan Orlando (12)
jarak12 = radius * math.acos(math.sin(x1) * math.sin(x2) + math.cos(x1) * math.cos(x2) * math.cos(y1 - y2))

#  6. Jarak Orlando dan Savannah (23)
jarak23 = radius * math.acos(math.sin(x2) * math.sin(x3) + math.cos(x2) * math.cos(x3) * math.cos(y2 - y3))

#  7. Jarak Savannah dengan Atlanta (31)
jarak31 = radius * math.acos(math.sin(x1) * math.sin(x3) + math.cos(x3) * math.cos(x1) * math.cos(y3 - y1))

#  8. Luas Area Atlanta, Savannah, Orlando (123)
s123 = (jarak12 + jarak23 + jarak31) / 2 # setengah keliling segitiga 123

luas123 = (s123 * (s123 - jarak12) * (s123 - jarak23) * (s123 - jarak31) ) ** (1/2)

#  9. Jarak Savannah dan Charlotte (34)
jarak34 = radius * math.acos(math.sin(x3) * math.sin(x4) + math.cos(x3) * math.cos(x4) * math.cos(y3 - y4))

# 10. Jarak Atlanta dan Charlotte (14)
jarak14 = radius * math.acos(math.sin(x1) * math.sin(x4) + math.cos(x1) * math.cos(x4) * math.cos(y1 - y4))


# 11. Luas area Atlanta, Savannah, Charlotte (134)
s134 = (jarak31 + jarak34 + jarak14) / 2 # setengah keliling segitiga 134

luas134 = (s134 * (s134 - jarak31) * (s134 - jarak34) * (s134 - jarak14)) ** (1/2)

# 12. Luas Atlanta, Orlando, Savannah, Charlotte
luas1234 = luas123 + luas134

luas1234 = round(luas1234, 2) # dibulatkan 2 angka desimal

# 13. Tampilkan luas Atlanta, Orlando, Savannah, Charlotte.
print("Luas daerah yang melingkupi kota",
       "Atlanta,",
       "Orlando,",
       "Savannah, dan",
       "Charlotte adalah",
       luas1234, "Km persegi."
      )


