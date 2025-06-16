'''
    ===========================================
    03.07. ASCII Random
    Oleh : #bayuyudhasaputra
    -------------------------------------------
    Buatlah progran yang menampilkan huruf 
    kapital
    sesuai dengan kode ASCII mulai dari 0
    hingga 127 secara random.
    ===========================================
'''
import random

# 1. membangkitkan bilangan random tidak kurang dari 65 dan tidak lebih dari 90.
kode_ascii = random.randint(65, 90)

# 2 Mengonversi kode ASCII menjadi huruf kapital
karakter = chr(kode_ascii)

# 3. Menampilkan huruf kapital random
print("Huruf kapital random yang dihasilkan adalah : ", karakter)