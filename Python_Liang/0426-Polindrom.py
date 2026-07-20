'''
================================================================================
Programming Exercise 04.26
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.26. Polindrom
    Tuliskan program yang menawarkan prompt kepada pengguna untuk menginput 
    bilangan tiga digit. Program menguji apakah bilangan yang diinput termasuk 
    bilangan polindrom atau bukan. Bilangan polindrom adalah bilangan yang 
    dibaca sama baik dibaca dari kiri maupun kanan, seperti 121.    
================================================================================
'''

import sys

# 1. Input bilangan tiga digit
bilangan = int(input("Input bilangan tiga digit: "))

# 2. Validasi bilangan yang diinput
if (bilangan <= 100) or (bilangan >= 999) :
    print("Error: Bilangan yang diinput harus tiga digit!")
    sys.exit()

# 3. Ekstrak bilangan tiga digit
# 3a. Ekstrak ratusan
ratusan = bilangan // 100
sisa = bilangan % 100

# 3b. Ekstrak puluhan
puluhan = sisa // 10
sisa %= 10

# 3c. Ekstrak satuan
satuan = sisa

# 4. Cek bilangan polindrom
if ratusan == satuan:
    print(f"{bilangan} adalah bilangan polindrom.")
else:
    print(f"{bilangan} bukan bilangan polindrom.")






