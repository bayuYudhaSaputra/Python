'''
================================================================================
Programming Exercise 04.06
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.06. Menghitung BMI
   Buatlah program yang menampilkan BMI serta penafsirannya. 
   Program menawarkan input berupa tinggi badan dalam satuan feet lebih 
   berapa inchi. Selain itu, pengguna juga menginput berat badan dalam 
   satuan pound.
================================================================================
'''

import sys

# 1. Input tinggi badan
tinggiFeet = eval(input("Input tinggi badan (dalam satuan feet) : "))
tinggiInchi = eval(input("lebih berapa inchi? "))

if tinggiFeet > 0 and tinggiInchi > 0:
    tinggiMeter = 0.3048 * tinggiFeet + 0.0254 * tinggiInchi
else:
    print("Tinggi harus bilangan positif..!")
    sys.exit()

# 2. Input berat badan
beratPound = eval(input("Input berat badan (dalam Pound) : "))

if beratPound <= 0:
    print("Berat badan harus bilangan positif..!")
    sys.exit()

beratKg = beratPound * 0.45359237

# 3. Hitung dan tampilkan BMI
bmi = beratKg / (tinggiMeter ** 2)
print("BMI anda adalah ", bmi)

# 4. Interpretasikan BMI
if bmi < 18.5:
    print("Berat badan anda kurang.")
elif bmi < 24.9:
    print("Berat badan anda normal.")
elif bmi < 29.9:
    print("Berat badan anda berlebih.")
else:
    print("Anda obesitas.")

