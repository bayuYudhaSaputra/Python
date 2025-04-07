'''
    ========================================
    03.06. Konversi kode ASCII
    Oleh : #bayuyudhasaputra
    ----------------------------------------
    Buatlah program yang menerima input
    bilangan dari 0 hingga 127. Kemdian,
    Program mengkonversi bilangan ini
    menjadi karakter sesuai dengan standar
    ASCII.
    =======================================
'''

# 1. Input bilangan mulai 0 hingga 127
kode_ascii = eval(input("Input bilangan mulai dari 0 hingga 127 : "))

# 2. Konversi kode ASCII menjadi karakter
karakter = chr(kode_ascii)

# 3. Tampilkan hasil konversi
print("Karakter dengan kode ASCII", kode_ascii,
      "adalah","\"", karakter, "\"")
