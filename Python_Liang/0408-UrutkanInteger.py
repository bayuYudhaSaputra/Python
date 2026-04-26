'''
================================================================================
Programming Exercise 04.08
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.08. Urutkan Tiga Bilangan
   Buatlah program mengurutkan tiga bilangan integer yang diinput pengguna
   mulai dari terkecil hingga terbesar.
================================================================================
'''

# 1. Input tiga  integer
bilangan1 = eval(input("Input integer pertama : "))
bilangan2 = eval(input("Input integer kedua : "))
bilangan3 = eval(input("Input integer ketiga : "))
print("Anda menginput:", bilangan1, ",", bilangan2, ",", bilangan3, ".")

# 2. Urutkan integer
if (bilangan1 < bilangan3 < bilangan2):
    bilangan2, bilangan3 = bilangan3, bilangan2
    # Tukar nilai bilangan2 dengan bilangan3

elif (bilangan2 < bilangan1 < bilangan3):
    bilangan1, bilangan2 = bilangan2, bilangan1
    # Tukar nilai bilangan1 dengan bilangan2

elif (bilangan2 < bilangan3 < bilangan1):
    bilangan1, bilangan2 = bilangan2, bilangan1
    # Tukar nilai bilangan1 dengan bilangan2
    bilangan2, bilangan3 = bilangan3, bilangan2
    # Tukar nilai bilangan2 dengan bilangan3

elif (bilangan3 < bilangan1 < bilangan2):
    bilangan1, bilangan2 = bilangan2, bilangan1
    # Tukar nilai bilangan1 dengan bilangan2
    bilangan1, bilangan3 = bilangan3, bilangan1
    # Tukar nilai bilangan1 dengan bilangan3

elif (bilangan3 < bilangan2 < bilangan1):
   bilangan1, bilangan3 = bilangan3, bilangan1 
    # Tukar nilai bilangan1 dengan bilangan3

# 3. Tampilkan hasil pengurutan
print("Urutan bilangan terbesar hingga terkecil:")
print(bilangan1, ",", bilangan2, ",", bilangan3, ".")


