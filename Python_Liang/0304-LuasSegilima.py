'''
   =======================================
   03.04. Luas Segilima
   Oleh : #bayuyudhasaputra
   ---------------------------------------
   Buatlah program yang menentukan luas 
   segilima jika program menerima input 
   panjang sisi segilima tersebut
   =======================================
'''

import math
import turtle
# 1. Input panjang sisi segilima
sisi = eval(input("Input panjang sisi segilima : "))

# 2. Hitung luas segilima
luas = (5 * pow(sisi, 2)) / (4 * math.tan(math.pi / 5))

# 3. Tampilkan luas
print("Luas segilima adalah ", luas)
