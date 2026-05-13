'''
================================================================================
Programming Exercise 04.16
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.16. Mengacak Karakter Huruf Kecil
  Buatlah program yang menampilkan huruf kecil secara acak. 
================================================================================
'''

import random

# 1. Acak bilangan integer antara 97 - 122 dan konversi ke dalam huruf sesuai
# kode ASCII
huruf = chr(random.randint(97, 122))

# 2. Tampilkan
print("Huruf kecil yang diacak adalah:", huruf)
