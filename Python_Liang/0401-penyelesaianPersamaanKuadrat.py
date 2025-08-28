'''
=============================================================================================================
Programming Exercise 04.01
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel/dp/0132747189
-------------------------------------------------------------------------------------------------------------
04.01. Judul Exercise
    Tuliskan program menentukan penyelesaian dari persamaan kuadrat, 
    dengan bentuk umum ax^2 + bx + c. 
    Jika program menerima input koefisien dari x2 dan x serta konstanta. 
==============================================================================================================
'''

# 1. Input koefisien x^2 dan x serta konstanta c dari persamaan kuadrat
a = eval(input("Input koefisien x kuadrat : "))
b = eval(input("Input koefisien x : "))
c = eval(input("Input konstanta : "))

# 2. Hitung diskriminan
D = b ** 2 - 4 * a * c

# 3. Tentukan akar
if D > 0:
    akar1 = (-b + D ** (1/2)) / (2 * a)
    akar2 = (-b - D ** (1/2)) / (2 * a)
    akar1 = round(akar1, 3)
    akar2 = round(akar2, 3)
    print("Akar-akar persamaan kuadrat",
          a, "x^2", "+", b, "x", "+", c, "= 0",
          "adalah", akar1, "atau", akar2)
elif D == 0:
    akar = (-b) / (2 * a)
    print("Akar-akar persamaan kuadrat",
          a, "x^2", "+", b, "x", "+", c, "= 0",
          "adalah", akar, "saja")
else:
    print("Persamaan kuadrat",
          a, "x^2", "+", b, "x", "+", c, "= 0",
          "tidak mempunyai akar real.")