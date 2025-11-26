'''
================================================================================
Programming Exercise 04.07
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.07. Monetary Unit
   Buatlah program yang menawarkan prompt kepada pengguna untuk menginput 
   nominal uang dalam satuan dolar Amerika Serikat. Kemudian, program 
   menyatakan uang ini dalam beberapa koin uang penny, nickel, dime, dan 
   quarter. Dimana, 1 penny setara 1 cent, 1 nickel setara 5 cent, 1 dime 
   setara 10 cent, dan 1 quarter setara 25 cent. Selain itu, program tidak 
   menampilkan nilai jika hasilnya adalah 0 koin. Dan, program akan 
   menampilkan bentuk jamak untuk jumlah koin lebih dari 1 koin. Bentuk jamak 
   masing-masing koin adalah pennies, nickels, dimes, dan quarters.
================================================================================
'''

import sys

# 1. Input mata uang dalam USD
nominal = eval(input("Input uang dalam satuan USD: "))

if nominal <= 0:
    print("Peringatan! \nInput nominal uang dengan bilangan positif.\n")
    sys.exit()
    # Cek apakah nilai nominal lebih dari 0

# 2. Ubah mata uang dalam satuan cent
cent = int(nominal * 100)

# 3. Tentukan banyak koin quarter
banyakQuarter = cent // 25
sisa = cent % 25

# 4. Tentukan banyak koin dime
banyakDime = sisa // 10
sisa %= 10

# 5. Tentukan banyak koin nickel
banyakNickel = sisa // 5
sisa %= 5

# 6. Tentukan banyak penny
banyakPenny =  sisa

# 7. Tampilkan hasil penukaran
# 7a. Tampilkan Quarter
if banyakQuarter == 0:
    pesanQuarter = ""
elif banyakQuarter == 1:
    pesanQuarter = str(banyakQuarter) + " koin quarter; \n"
else:
    pesanQuarter = str(banyakQuarter) + " koin quarters; \n"

# 7b. Tampilkan Dime 
if banyakDime == 0:
    pesanDime = ""
elif banyakDime == 1:
    pesanDime = str(banyakDime) + " koin dime; \n"
else:
    pesanDime = str(banyakDime) + " koin dimes; \n"

# 7c. Tampilkan Nickel 
if banyakNickel == 0:
    pesanNickel = ""
elif banyakNickel == 1:
    pesanNickel = str(banyakNickel) + " koin nickel; \n"
else:
    pesanNickel = str(banyakNickel) + " koin nickels; \n"

# 7d. Tampilkan Penny 
if banyakPenny == 0:
    pesanPenny = ""
elif banyakPenny == 1:
    pesanPenny = str(banyakPenny) + " koin penny."
else:
    pesanPenny = str(banyakPenny) + " koin pennies."

# 7e. Tampilkan semua
pesan = "Uang sebesar USD" + str(nominal) + " dapat ditukar menjadi: \n" + \
        pesanQuarter + \
        pesanDime + \
        pesanNickel + \
        pesanPenny
        
print(pesan)

