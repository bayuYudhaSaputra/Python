'''
================================================================================
Programming Exercise 04.09
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.09. Membandingkan Harga Satuan
   Misal, anda belanja beras di suatu toko yang menyediakan dua paket yang 
   berbeda. Buatlah program untuk membandingkan biaya yang dikeluarkan untuk 
   masing-masing paket. Program menyediakan prompt kepada pengguna untuk
   menginput berat beras dan harga masing-masing paket. Kemudian, program
   menampilkan biaya yang paling rendah di antara paket-paket ini.
================================================================================
'''

import sys

# 01. Input paket 1
print("Input Paket 1")
berat1 = eval(input("Input berat paket 1 (dalam Kg): "))
harga1 = eval(input("Input harga paket 1 (dalam Rp): "))

# 01a. Cek berat1 dan harga1
if berat1 <= 0 or harga1 <= 0:
    print("Input bilangan lebih dari 0.")
    sys.exit()

# 02. Input paket 2
print("Input Paket 2")
berat2 = eval(input("Input berat paket 2 (dalam Kg): "))
harga2 = eval(input("Input harga paket 2 (dalam Rp): "))

#02a. Cek berat2 dan harga2
if berat2 <= 0 or harga2 <= 0:
    print("Input bilangan lebih dari 0.")
    sys.exit()

# 03. Hitung harga paket 1 dan 2 per Kg
hargaPerKg1 = harga1 / berat1
hargaPerKg2 = harga2 / berat2

# 04. Bandingkan dan tampilkan harga paket 1 dan 2 per Kg
if hargaPerKg1 > hargaPerKg2:
    print("Paket 2 lebih murah dibanding Paket 1.")
elif hargaPerKg1 < hargaPerKg2:
    print("Paket 1 lebih murah dibanding Paket 2.")
else:
    print("Harga paket 1 sama dengan Paket 2.")

