'''
====================================================
0209. Menghitung temperatur windchill
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan program yang meminta input temperatur antara 
-58 derajat fahrenheit hingga 41 derajat fahrenheit 
serta kecepatan angin lebih dari atau sama dengan 2 mph. 
Kemudian, program menampilkan temperatur wind-chill 
sesuai dengan rumus tersebut!
====================================================
'''

kecepatan_udara = eval(input("Input kecepatan udara (dalam satuan mph) : "))
temperatur_udara = eval(input("Input temperatur udara (dalam satuan derajat fahrenheit) : "))

temperatur_windchill = 35.74 + 0.6215 * temperatur_udara - 35.75 * kecepatan_udara ** 0.16 + 0.4275 * temperatur_udara * kecepatan_udara ** 0.16

print("Temperatur windchill : ", temperatur_windchill)