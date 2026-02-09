'''
================================================================================
Programming Exercise 04.12
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.12. Cek Keterbagian
   Tuliskan program yang menawarkan prompt kepada pengguna untuk menginput dua
   bilangan integer positif. Program akan menampilkan pesan apakah kedua 
   bilangan ini habis dibagi 5 dan 6, dibagi 5 atau 6; serta apakah kedua 
   bilangan ini habis dibagi 5 saja atau 6 saja?
================================================================================
'''
import sys

# 1. Input 1 bilangan integer positif
bilangan = int(input("Input bilangan integer positif: "))
print("Anda menginput bilangan", bilangan)

# 2. Cek Keterbagian bilangan
if (bilangan <= 0):
    # cek, apakah pengguna menginput integer positif?
    print("Peringatan : Input bilangan integer positif saja!!")
    sys.exit() # program keluar

else: 
    pesan1 = "Apakah " + str(bilangan) + " habis dibagi 5 dan 6? " + \
            str((bilangan % 5 == 0) and (bilangan % 6 == 0))
    pesan2 = "Apakah " + str(bilangan) + " habis dibagi 5 atau 6? " + \
            str((bilangan % 5 == 0) or (bilangan % 6 == 0))
    pesan3 = "Apakah " + str(bilangan) + " habis dibagi 5 saja atau 6 saja? " + \
            str((bilangan % 5 == 0) ^ (bilangan % 6 == 0))

# 3. Tampilkan output
print(pesan1)
print(pesan2)
print(pesan3)

