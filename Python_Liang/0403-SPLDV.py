'''
===============================================================================
Programming Exercise 04.03
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
/dp/013274718
-------------------------------------------------------------------------------
04.03. Sistem Persamaan Linier Dua Variabel
Buatlah program untuk menentukan solusi dari sistem persamaan linier dua
variabel. Pengguna menginput koefisien dari variabe; dan konstanta
persamaan linier ini.
===============================================================================
'''

# 1. Input koefisien dan konstanta persamaan ke-1

print("\n")
print("=============================================================")

a = eval(input("Input koefisien x persamaan ke-1 : "))
b = eval(input("Input koefisien y persamaan ke-1 : "))
e = eval(input("Input konstanta persamaan ke-1 : "))

# 2. Tampilkan persamaan ke-1

print("-------------------------------------------------------------")

if a == 0:
    print(b, "y = ", e, ".... Persamaan 1)")
elif a == 1:
    if b == -1:
        print("x", "-", "y", "=", e, ".... Persamaan 1)")
    elif b < 0:
        print("x", "-", abs(b), "y", "=", e, ".... Persamaan 1)")
    elif b == 0:
        print("x", "=", e, ".... Persamaan 1)")
    elif b == 1:
        print("x", "+", "y", "=", e, ".... Persamaan 1)")
    else:
        print("x", "+", b, "y", "=", e, ".... Persamaan 1)")
elif a == -1:
    if b == -1:
        print("-x", "-", "y", "=", e, ".... Persamaan 1)")
    elif b < 0:
        print("-x", "-", abs(b), "y", "=", e, ".... Persamaan 1)")
    elif b == 0:
        print("-x", "=", e, ".... Persamaan 1)")
    elif b == 1:
        print("-x", "+", "y", "=", e, ".... Persamaan 1)")
    else:
        print("-x", "+", b, "y", "=", e, ".... Persamaan 1)")
else:
    if b == -1:
        print(a, "x", "-", "y", "=", e, ".... Persamaan 1)")
    elif b < 0:
        print(a, "x", "-", abs(b), "y", "=", e, ".... Persamaan 1)")
    elif b == 0:
        print(a, "x", "=", e, ".... Persamaan 1)")
    elif b == 1:
        print(a, "x", "+", "y", "=", e, ".... Persamaan 1)")
    else:
        print(a, "x", "+", b, "y", "=", e, ".... Persamaan 1)")

print("-------------------------------------------------------------")

# 3. Input koefisien dan konstanta persamaan ke-2

c = eval(input("Input koefisien x persamaan ke-2: "))
d = eval(input("Input kefisien y persamaan ke-2: "))
f = eval(input("Input konstanta persamaan ke-2: "))

# 4. Tampilkan persamaan ke-2

print("-------------------------------------------------------------")

if c == 0:
    print(d,"y", "=", f, ".... Persamaan 2)")
elif c == 1:
    if d < 0:
         print("x", "-", abs(d), "y", "=", f, ".... Persamaan 2)")
    elif d == -1:
         print("x", "-", "y", "=", f, ".... Persamaan 2)")
    elif d == 0:
         print("x", "=", f, ".... Persamaan 2)")
    elif d == 1:
         print("x", "+", "y", "=", f, ".... Persamaan 2)")
    else:
         print("x", "+", d, "y", "=", f, ".... Persamaan 2)")
elif c == -1:
    if d == -1:
        print("-x", "-", "y", "=", f, ".... Persamaan 2)")
    elif d < 0:
        print("-x", "-", abs(d), "y", "=", f, ".... Persamaan 2)")
    elif d == 1:
        print("-x", "+", "y", "=", f, ".... Persamaan 2)")
    else:
        print("-x", "+", d, "y", "=", f, ".... Persamaan 2)")
else:
    if d == -1:
        print(c, "x", "-", "y", "=", f, ".... Persamaan 2)")
    elif d < 0:
        print(c, "x", "-", abs(d), "y", "=", f, ".... Persamaan 2)")
    elif d == 0:
        print(c, "x", "=", f, ".... Persamaan 2)")
    elif d == 1:
        print(c,"x", "+", "y", "=", f, ".... Persamaan 2)" )
    else:
        print(c, "x", "+", d, "y", "=", f, ".... Persamaan 2)")

print("-------------------------------------------------------------")


# 5. Hitung ad - bc

penyebutSolusi = a * d - b * c

# 6. Cek ad - bc

if penyebutSolusi == 0:
    print("Persamaan linier 1 dan 2 tidak mempunyai solusi.")
else:
    x1 = (e * d - b * f) / penyebutSolusi
    y1 = (a * f - e * c) / penyebutSolusi
    print("Solusi persamaan 1 dan 2 adalah", "x1 =", x1, "dan", "y1 =", y1)


print("============================================================= \n")


