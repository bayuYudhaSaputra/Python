'''
=============================================================================================================
Programming Exercise 03.11
Oleh      : #bayuyudhasaputra
Sumber    : https://media.pearsoncmg.com/bc/abp/cs-resources/products/product.html#product,isbn=0133050556
-------------------------------------------------------------------------------------------------------------
03.11. Membalik Digit Bilangan
Buatlah program yang meminta input kepada pengguna untuk menginput bilangan 4 digit.
Program akan menampilkan bilangan ini dengan urutan terbalik.

Contoh program:
Input bilangan 4 digit (Mis. 1689) : 1689
Urutan terbalik dari bilangan 1689 adalah 9861
==============================================================================================================
'''

# 1. Input bilangan 4 digit
bilangan = eval(input("Input bilangan 4 digit (Mis. 1689) :"))
kebalikan = 0

# 2. Ekstrak satuan
digit = bilangan % 10
kebalikan = kebalikan * 10 + digit
bilangan //= 10

# 2. Ekstrak puluhan
digit = bilangan % 10
kebalikan = kebalikan * 10 + digit
bilangan //= 10

# 3. Ekstrak ratusan
digit = bilangan % 10
kebalikan = kebalikan * 10 + digit
bilangan //= 10

# 3. Ekstrak ribuan
digit = bilangan % 10
kebalikan = kebalikan * 10 + digit
bilangan //= 10

# 4. Tampilkan output
print("Jika digitnya dibalik menjadi", kebalikan, ".")