'''
    ===========================================
    0306. Menentukan Kode ASCII
    Oleh : #bayuyudhasaputra
    -------------------------------------------
    Buatlah program yang menerima input berupa
    bilangan integer dari 0 hingga 127. Program
    mengonversi bilangan ini ke dalam karakter
    sesuai dengan kode ASCII.
    ===========================================
'''
# 1. Input bilangan integer
bilangan = eval(input("Input kode ASCII : "))

# 2. Konversi kode ASCII menjadi karakter
karakter = chr(bilangan)

# 3. Tampilkan hasil konversi
print("Karakter dengan kode ASCII", bilangan,
      "adalah", karakter)
