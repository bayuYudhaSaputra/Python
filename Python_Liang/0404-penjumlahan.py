'''
===============================================================================
Programming Exercise 04.04
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
-------------------------------------------------------------------------------
04.04. Tebak Penjumlahan
   Buatlah program yang membangkitkan dua bilangan integer acak antara 
   0 hingga 100. Program menawarkan prompt kepada pengguna untuk menginput 
   hasil penjumlahan kedua bilangan ini. Program menampilkan pesan benar 
   jika yang diinput pengguna sesuai dengan hasil penjumlahan. 
   Program menampilkan pesan salah jika sebaliknya.
===============================================================================
'''

import random

# 1. Bangkitkan 2 bilangan integer antara 0 - 100
bilangan1 = random.randint(0, 101)
bilangan2 = random.randint(0, 101)

# 2. Hitung jumlah bilangan integer
jumlah = bilangan1 + bilangan2

# 3. Input hasil penjumlahan
pesanTebak = "Berapakah hasil dari " + str(bilangan1) + " + " + \
        str(bilangan2) + " ? "
tebak = eval(input(pesanTebak))
print("Anda menginput", tebak)

# 4. Cek input
if tebak == jumlah:
    print("Selamat.. Jawaban anda benar!")
else:
    print("Maaf.. Jawaban anda kurang tepat!")
