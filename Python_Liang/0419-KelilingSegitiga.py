'''
================================================================================
Programming Exercise 04.19
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.19. Keliling Segitiga
    Tuliskan program yang membaca panjang tiga sisi segitiga. Program
    menentukan keliling segitiga jika input valid. Jika input tidak valid,
    program menampilkan pesan. Input dikatakan valid jika jumlah dua sisi
    lebih besar daripada satu sisi yang lain.
================================================================================
'''

# 1. Input ketiga panjang sisi segitiga
sisi1 = eval(input("Input panjang sisi ke-1 segitiga: "))
sisi2 = eval(input("Input panjang sisi ke-2 segitiga: "))
sisi3 = eval(input("Input panjang sisi ke-3 segitga: "))

# 2. Uji validitas ketiga sisi segitiga
if (sisi1 <= 0 or sisi2 <= 0 or sisi3 <= 0):
    # 2a. panjang sisi 0 atau negatif
    print("Input bilangan positif..!!")

elif ((sisi1 + sisi2 < sisi3) or \
        (sisi1 + sisi3 < sisi2) or \
        (sisi2 + sisi3 < sisi1)):
    # 2b. Jumlah dua pasang sisi kurang dari sisi lainnya = tidak valid
    print("Panjang sisi-sisi tidak valid!")
    print("Coba input nilai lain!")

else:
    # 2c. Tentukan keliling 
    keliling = sisi1 + sisi2 + sisi3
    
    # 2d. Tampilkan keliling
    print("Keliling segitiga adalah", keliling)


