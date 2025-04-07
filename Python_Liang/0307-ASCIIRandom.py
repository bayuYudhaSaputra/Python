'''
    ===========================================
    03.07. ASCII Random
    Oleh : #bayuyudhasaputra
    -------------------------------------------
    Buatlah progran yang menampilkan karakter
    sesuai dengan kode ASCII mulai dari 0
    hingga 127 secara random.
    ===========================================
'''

import time
import random

# 1. Jalankan seed (pengubah waktu random)
seed = int(time.time())

# 2. Buat kode ASCII
kode_ascii = seed % 127

# 3. Konversi kode ASCII ke dalam karakter
karakter = chr(kode_ascii)

# 4. Tampilkan karakter random
print("Hasil karakter random adalah", karakter)
