'''
================================================================================
Programming Exercise 04.18
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.18. Konversi Nilai Tukar US. Dollar Ke Yuan dan Sebaliknya
    Tulis program yang menawarkan prompt kepada pengguna untuk mengonversi
    USD ke Renminbi (RMB) dan sebaliknya. Jika pengguna menginput 0 maka USD
    dikonversi menjadi Renminbi. Jika pengguna menginput 1 maka Renminbi
    dikonversi menjadi USD. Kemudian, program mengonversi USD ke Renminbi atau
    sebaliknya
================================================================================
'''

# 1. Input pilihan konversi
print("Input 0 : Konversi USD ke RMB.")
print("Input 1 : KOnversi RMB ke USD.")
pilihan = eval(input("Input : "))

# 2. Konversi dari USD ke RMB dan sebaliknya
if pilihan == 0:
    # 2a. Konversi USD ke RMB
    satuUSD = eval(input("1 USD sama dengan berapa RMB? "))
    USD = eval(input("Berapa nominal USD yang dikonversi? "))
    RMB = USD * satuUSD
    print("USD.", USD, "sama dengan RMB.", RMB)

elif pilihan == 1:
    # 2b. Konversi RMB ke USD
    satuRMB = eval(input("1 RMB sama dengan berapa USD? "))
    RMB = eval(input("Berapa nominal RMB yang dikonversi? "))
    USD = RMB * satuRMB
    print("RMB. ", RMB, "sama dengan USD.", USD)

else:
    print("Peringatan : hanya input bilangan 0 saja atau 1 saja!!")

