'''
================================================================================
Programming Exercise 04.14
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.14. Game : Gambar Atau Angka
    Tuliskan program yang menawarkan prompt kepada pengguna untuk menebak mata
    koin apa yang muncul. Mata koin terdiri dari angka dan gambar. Program 
    mengacak bilangan 0 untuk merepresentasikan mata koin angka dan 1 untuk
    mata koin gambar. Program menampilkan pesan jika tebakan pengguna sesuai
    atau tidak sesuai.
================================================================================
'''

import sys

# 1. Acak bilangan 0 atau 1
import random
angkaAcak = random.randint(0,1)

if (angkaAcak == 0):
    pesanHasilAcak = "angka"
elif (angkaAcak == 1):
    pesanHasilAcak = "gambar"

# 2. Input 0 atau 1
angkaInput = eval(input("Input bilangan 0 atau 1 : "))
if (angkaInput != 0 and angkaInput != 1):
    print("Input bilangan 0 dan 1 saja.")
    sys.exit()
elif (angkaInput == 0):
    pesanHasilInput = "angka"
elif (angkaInput == 1):
    pesanHasilInput = "gambar"

# 3. Bandingkan hasil acak dengan input dan tampilkan pesan
print("Komputer menampilkan mata koin", pesanHasilAcak)
print("Anda menebak mata koin", pesanHasilInput)

if (angkaAcak == angkaInput):
    print("Selamat.. Tebakan anda benar!")
else:
    print("Maaf.. Tebakan anda belum tepat!")


