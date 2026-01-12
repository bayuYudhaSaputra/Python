'''
================================================================================
Programming Exercise 04.10
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.10. Kuis Perkalian
   Buatlah program yang menampilkan dua bilangan integer acak kurang dari 100. 
   Kedua bilangan ini dikalikan. Pengguna menebak berapa hasil perkalian dari 
   kedua bilangan acak ini.
================================================================================
'''
import random
# 1. Acak dua bilangan integer acak antara 0 hingga 100
bilangan1 = random.randint(0, 100)
bilangan2 = random.randint(0, 100)

# 2. Tawarkan prompt untuk diinput pengguna
jawaban = eval(input("Berapakah hasil dari " 
                     + str(bilangan1) + " dikali " + str(bilangan2)
                     + "? "))

# 3. Kalikan kedua bilangan acak
hasilKali = bilangan1 * bilangan2

# 4. Bandingkan input dengan hasil kali
if hasilKali == jawaban:
    print("Selamat... Jawaban anda benar!")
else:
    print("Maaf... Jawaban anda belum tepat!")

