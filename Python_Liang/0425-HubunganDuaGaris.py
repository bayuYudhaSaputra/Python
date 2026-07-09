'''
================================================================================
Programming Exercise 04.25
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.25. Hubungan Dua Garis
   Suatu garis dapat dibentuk dari dua titik. Misal, titik k melalui
   titik A(x1, y1) dan B(x2, y2) serta garis l melalui titik C(x3, y3) dan 
   D(x4, y4). Buatlah program yang meminta input titik-titik A, B, C, dan D.
   Program menentukan apakah garis k berpotongan, berpotongan tegak lurus dan
   sejajar dengan garis l.
================================================================================
'''
print(40 * "=")
print("Garis k.")
print(40 * "-")

# 1. Input titik ke-1 garis k
absis_k_1 = float(input("Input absis titik ke-1 garis k: "))
ordinat_k_1 = float(input("Input ordinat titik pertama garis k: "))

print(f"Anda menginput titik A({absis_k_1} , {ordinat_k_1}).")
print(40 * "-")

# 2. Input titik ke-2 garis k
absis_k_2 = float(input("Input absis titik ke-2 garis k: "))
ordinat_k_2 = float(input("Input ordinat titik ke-2 garis k: "))

print(f"Anda menginput titik B({absis_k_2} , {ordinat_k_2}).")
print(40 * "-")

# 3. Tentukan garis k
koef_x_k = ordinat_k_1 - ordinat_k_2
koef_y_k = absis_k_2 - absis_k_1
kons_k = koef_x_k * absis_k_1 + koef_y_k * ordinat_k_1

print(f"Garis k : ({koef_x_k})x + ({koef_y_k})y = {kons_k}")
print(40 * "=", "\n")

# 4. Tentukan gradien garis k
if (absis_k_2 - absis_k_1 == 0):
    gradien_k = "tidak ada"
else:
    gradien_k = (ordinat_k_2 - ordinat_k_1) / (absis_k_2 - absis_k_1)

print(40 * "=")
print("Garis l.")
print(40 * "-")

# 5. Input titik ke-1 garis l
absis_l_1 = float(input("Input absis titik ke-1 garis l: "))
ordinat_l_1 = float(input("Input ordinat titik ke-2 garis l: "))

print(f"Anda menginput titik C({absis_l_1} , {ordinat_l_1}).")
print(40 * "-")

# 6. Input titik ke-2 garis l
absis_l_2 = float(input("Input absis titik ke-2 garis l: "))
ordinat_l_2 = float(input("Input ordinat titik ke-2 garis l: "))

print(f"Anda menginput titik D({absis_l_2} ,{ordinat_l_2}).")
print(40 * "-")

# 7. Tentukan garis l
koef_x_l = ordinat_l_1 - ordinat_l_2
koef_y_l = absis_l_2 - absis_l_1
kons_l = koef_x_l * absis_l_1 + koef_y_l * ordinat_l_1

print(f"Garis l : ({koef_x_l})x + ({koef_y_l})y = {kons_l}")
print(40 * "=", "\n")

# 8. Tentukan gradien garis l
if (absis_l_2 - absis_l_1 == 0):
    gradien_l = "tidak ada"
else:
    gradien_l = (ordinat_l_2 - ordinat_l_1) / (absis_l_2 - absis_l_1)

# 9. Bandingkan garis k dengan l
print(40 * "=")

if (gradien_k != gradien_l):
    print("Garis k dan l berpotongan.")
else:
    print("Garis k tidak berpotongan dengan l.")

print(40 * "=")

