'''
=============================================================================================================
Programming Exercise 04.02
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel/dp/0132747189
-------------------------------------------------------------------------------------------------------------
04.02. Game Penjumlahan
   Buatlah program yang membangkitkan 3 bilangan integer acak antara 0 hingga 9. 
   Kemudian, pengguna menebak jumlah dari ketiga bilangan acak ini. 
   Program menentukan apakah hasil tebakan pengguna benar atau salah.
==============================================================================================================
'''

import random

# 1. Bangkitkan 3 bilangan random integer dari 0 hingga 9
bilangan1 = random.randint(0,9)
bilangan2 = random.randint(0,9)
bilangan3 = random.randint(0,9)

# 2. Jumlahkan kedua bilangan acak
jumlah = bilangan1 + bilangan2 + bilangan3

# 3. Input jawaban dari pengguna
pertanyaan = "Berapakah jumlah dari " +\
                str(bilangan1) + " + " + str(bilangan2) + " + " + str(bilangan3) + " ? "
jawaban = eval(input(pertanyaan))

print("Anda menjawab", jawaban)

# 4. Cek jawaban yang diinput pengguna
if (jumlah == jawaban):
    print("Selamat.. Jawaban anda benar..!")
else:
    print("Oh.. Maaf.. Jawaban anda kurang tepat..!")
