'''
   ====================================
   03.05. Luas Segi-n Beraturan
   Oleh : #bayuyudhasaputra
   ------------------------------------
   Buatlah program yang menerima input
   segi apa dan panjang sisi segi-n 
   tersebut. Program menentukan luas
   segi-n tersebut.
   ====================================
'''

import math

# 1. Input segi-n apa yang dimaksud.
n = eval(input("Input segi apa yang dimaksud: "))

# 2. Input panjang sisi segi-n 
sisi = eval(input("Input panjang sisi segi-n: "))

# 3. Hitung luas segi-n
luas = (n * sisi ** 2) / (4 * math.tan(math.pi / n))
luas = round(luas, 2)

# 4. Tampilkan luas
print("Luas segi-", n,
      "dengan panjang sisi", sisi,
      "adalah", luas, "."
      )

