'''
================================================================================
Programming Exercise 04.22
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.22. Hubungan Titik Dengan Lingkaran
   Buatlah program yang menawarkan prompt kepada pengguna untuk menginput 
   titik pusat lingkaran, jari-jari lingkaran dan satu titik sembarang. 
   Program menampilkan pesan apakah titik sembarang itu di dalam, pada 
   atau di luar lingkaran.
================================================================================
'''
import sys

# 1. Input titik pusat lingkaran dan jari-jari lingkaran
absis_pusat = float(input("Input absis (x) titik pusat lingkaran: "))
ordinat_pusat = float(input("Input ordinat (y) titik pusat lingkaran: "))

# 2. Input jari-jari lingkaran
jari2 = float(input("Input jari-jari lingkaran: "))

# 3. Validasi jari-jari lingkaran
if jari2 <= 0:
   print("Jari-jari lingkaran harus lebih besar dari 0.")
   sys.exit()

# 4. Tampilkan persamaan lingkaran
print("\nPersamaan lingkaran:" 
      f"(x - {absis_pusat})^2 + (y - {ordinat_pusat})^2 = {jari2 ** 2} \n")

# 5. Input titik sembarang
absis_titik = float(input("Input absis (x) titik sembarang: "))
ordinat_titik = float(input("Input ordinat (y) titik sembarang: "))

# 6. Hitung jarak titik sembarang ke titik pusat lingkaran (d)
d = ((absis_titik - absis_pusat) ** 2 + (ordinat_titik - ordinat_pusat) ** 2) ** 0.5

# 7. Tentukan posisi titik sembarang terhadap lingkaran
if d < jari2:
   print(f"\nTitik ({absis_titik}, {ordinat_titik}) berada di dalam lingkaran " 
         f"(x - {absis_pusat})^2 + (y - {ordinat_pusat})^2 = {jari2 ** 2}. \n")
elif d == jari2:
   print(f"\nTitik ({absis_titik}, {ordinat_titik}) berada di keliling lingkaran "
         f"(x - {absis_pusat})^2 + (y - {ordinat_pusat})^2 = {jari2 ** 2}. \n")
else:
   print(f"\nTitik ({absis_titik}, {ordinat_titik}) berada di luar lingkaran "
         f"(x - {absis_pusat})^2 + (y - {ordinat_pusat})^2 = {jari2 ** 2}. \n")
