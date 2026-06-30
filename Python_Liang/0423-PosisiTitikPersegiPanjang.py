'''
================================================================================
Programming Exercise 04.23
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.23. Hubungan Antara Titik Dengan Persegi Panjang
    Tuliskan program yang meminta input kepada pengguna untuk menginput titik
    sembarang (x, y), panjang dan lebar persegi panjang. Program menentukan
    apakah titik sembarang (x, y) berada di dalam, pada keliling atau di luar
    persegi panjang.
    
================================================================================
'''

import sys

# 1. Input dan validasi panjang
panjang = float(input("Input panjang : "))

# 2. Validasi panjang
if panjang <= 0:
    print("\nPeringatan : Panjang harus lebih dari 0!\n")
    sys.exit()

# 3. Input dan validasi lebar
lebar = float(input("Input lebar : "))

# 4. Validasi lebar
if lebar <= 0:
    print("\nPeringatan : Lebar harus lebih dari 0!\n")
    sys.exit()

# 5. Input absis titik sembarang
absis_titik = float(input("Input absis titik sembarang : "))

# 6. Input ordinat titik sembarang
ordinat_titik = float(input("Input ordinat titik sembarang : "))

# 7. Hitung setengah jarak horizontal
setengah_jarak_horizontal = 0.5 * abs(absis_titik - 0)

# 8. Hitung setengah jarak vertikal
setengah_jarak_vertikal = 0.5 * abs(ordinat_titik - 0)

# 9. Bandingkan jarak dengan panjang dan lebar dan tampilkan hasil
if ((setengah_jarak_horizontal < panjang) 
    and (setengah_jarak_vertikal < lebar)):
    print(f"\nTitik ({absis_titik},{ordinat_titik}) di dalam "
          "persegi panjang.\n")

elif ((setengah_jarak_horizontal == panjang and 
       setengah_jarak_vertikal <= lebar) 
      or (setengah_jarak_vertikal == lebar and 
          setengah_jarak_horizontal <= panjang)):
    print(f"\nTitik ({absis_titik},{ordinat_titik}) di keliling " 
          "persegi panjang.\n")

else:
    print(f"\nTitik ({absis_titik},{ordinat_titik}) di luar "
          "persegi panjang.\n")


