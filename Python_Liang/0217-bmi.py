'''
====================================================
0217. Body Mass Index
Oleh : #bayuyudhasaputra
----------------------------------------------------
Buatlah program yang menampilkan body mass index 
(BMI) jika pengguna menginput berat badan (dalam Kg) 
dan tinggi badan (dalam meter).
====================================================
'''

# 1. Input massa dan tinggi badan
massa = eval(input("Input massa badan dalam kilogram : "))
tinggi = eval(input("Input tinggi badan dalam meter : "))

# 2. hitung BMI
bmi = massa / (tinggi ** 2)

# 3. Tampilkan BMI
print("BMI seseorang dengan massa badan",
      massa, "kg dan", 
      tinggi, "meter adalah",
      bmi, ".")