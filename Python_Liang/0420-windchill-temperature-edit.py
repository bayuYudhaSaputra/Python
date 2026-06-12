'''
===============================================================================
0420. Menghitung temperatur windchill
Oleh : #bayuyudhasaputra
-------------------------------------------------------------------------------
Perhatikan latihan 02.09 mengenai temperatur wind-chill. Rumus temperatur ini
bisa digunakan pada rentang suhu antara -58 derajat fahrenheit hingga
41 derajat fahrenheit. Selain itu, rumus ini juga bisa digunakan jika kecepatan
angin lebih dari 2 mph. Tuliskan program yang meminta input temperatur dan
kecepatan angin. Program akan menampilkan temperatur wind-chill jika input 
valid. Jika input tidak valid, program akan menampilkan pesan invalid.
==============================================================================
'''

# 1, Input temperatur udara dan kecepatan udara
temperatur_udara = eval(input("Input temperatur udara (fahrenheit): "))

kecepatan_udara = eval(input("Input kecepatan udara (mph) : "))

# 2. Validasi input dan tampilkan hasilnya
if (temperatur_udara < -58 or temperatur_udara > 41):
    print("Peringatan.. Input temperatur udara tidak valid!!")
    print("Temperatur harus antara -58 hingga 41..!")

elif (kecepatan_udara <= 2):
    print("Peringatan: Input kecepatan udara tidak valid!!")
    print("Kecepatan udara harus lebih dari 2!")

else:
    temperatur_windchill = (35.74 + 0.6215 * temperatur_udara - 35.75 *
        kecepatan_udara ** 0.16 + 0.4275 * temperatur_udara * 
        kecepatan_udara ** 0.16)
    print("Temperatur windchill : ", temperatur_windchill)


