'''
====================================================
0205. Finansial : Menghitung Tip
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan program yang menerima input subtotal 
(biaya sebelum memberikan tip kepada pelayan) dan 
persentase tip yang harus diberikan kepada pelayan. 
Program akan menghitung nominal tip yang akan diberikan 
kepada pelayan dan total uang yang dibayarkan setelah 
ditambah tip yang akan dibayarkan kepada pelayan.
Misal, pengguna menginput subtotal 10 dan persentase 
tip 15 maka program akan menampilkan nominal tip yang 
diberikan sebesar 1.5 dan total yang harus dibayarkan 
adalah 11.5.
====================================================
'''
# 1. meminta input nominal subtotal kepada pengguna
nominalSubtotal = eval(input("Input nominal subtotal : "))

# 2. meminta input persentase tip kepada pengguna
persenTip = eval(input("Input persentase tip : "))

# 3. menentukan nominal tip
nominalTip = (persenTip / 100) * nominalSubtotal

# 4. menentukan total
total = nominalSubtotal + nominalTip

# 5. menampilkan nominal tip dan total
print("Nominal tip yang diberikan adalah", nominalTip)
print("dan total pembayaran sebesar", total)