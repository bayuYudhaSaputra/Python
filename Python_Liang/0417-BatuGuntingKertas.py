'''
================================================================================
Programming Exercise 04.17
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.17. Permainan Batu, Gunting Kertas
   Tuliskan program permainan batu gunting kertas (dimana, gunting memotong 
   kertas, batu membengkokkkan gunting, dan kertas membungkus kertas). 
   Program membangkitkan bilangan acak 0, 1, dan 2 yang merepresentasikan 
   berturut-turut gunting, batu, dan kertas. Program menawarkan prompt kepada 
   pengguna untuk menginput bilangan 0, 1, dan 2 yang juga merepresentasikan 
   berturut-turut gunting, batu, dan kertas. Kemudian, program menampilkan 
   pesan siapakah pemenangnya, apakah komputer atau pengguna.
================================================================================
'''

import random

# 1. Tentukan pilihan komputer
angkaKomputer = random.randint(0, 2)

if angkaKomputer == 0:
    pilihanKomputer = "gunting"
elif angkaKomputer == 1:
    pilihanKomputer = "batu"
else:
    pilihanKomputer = "kertas"

# 2. Input pilihan pengguna
angkaPengguna = eval(input("Pilih 0 (gunting), 1 (batu), atau 2 (kertas): "))

if angkaPengguna == 0:
    pilihanPengguna = "gunting"
elif angkaPengguna == 1:
    pilihanPengguna = "batu"
elif angkaPengguna == 2:
    pilihanPengguna = "kertas"
else:
    print("Hanya boleh input 0, 1, atau 2 saja..!")

# 3. Bandingkan pilihan komputer dengan pengguna
if pilihanKomputer == pilihanPengguna:
    hasil = "draw"
elif pilihanKomputer == "batu" and pilihanPengguna == "gunting":
    hasil = "Ups.. Kamu kalah..!!"
elif pilihanKomputer == "batu" and pilihanPengguna == "kertas":
    hasil = "Yee.. Kamu menang..!!"
elif pilihanKomputer == "gunting" and pilihanPengguna == "batu":
    hasil = "Yee.. Kamu menang..!!"
elif pilihanKomputer == "gunting" and pilihanPengguna == "kertas":
    hasil = "Ups.. Kamu kalah..!!"
elif pilihanKomputer == "kertas" and pilihanPengguna == "batu":
    hasil = "Ups.. Kamu kalah..!!"
elif pilihanKomputer == "kertas" and pilihanPengguna == "gunting":
    hasil = "Yee.. kamu menang..!!"

# 4. Tampilkan hasil
print("Komputer memilih", pilihanKomputer)
print("Kamu memilih", pilihanPengguna)
print(hasil)

