# ====================================================
# 0202. Menentukan Volume dan luas Tabung
# Oleh : #bayuyudhasaputra
# ====================================================

# import library math
import math

# mendefinisikan variabel phi
phi = math.pi

# input jari-2 dan tinggi tabung
jari2 = eval(input("Input jari-jari tabung (Misal. 10) : "))
tinggi = eval(input("Input tinggi tabung (Misal. 15) : "))

# Hitung volume tabung
volume = phi * jari2 ** 2 * tinggi

# Hitung luas tabung
luas = 2 * phi * jari2 ** 2 + 2 * phi * jari2 * tinggi

# tampilkan nilai volume dan luas tabung
print("Volume tabung : ", volume, "satuan")
print("Luas tabung : ", luas, " satuan.")