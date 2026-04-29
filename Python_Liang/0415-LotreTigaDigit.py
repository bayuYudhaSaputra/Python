'''
================================================================================
Programming Exercise 04.15
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.15. Tebak Lotre Tiga Digit
    Buatlah program yang mengacak tiga digit bilangan lotre. Program menawarkan 
    input kepada pengguna untuk menginput tiga digit bilangan dengan ketentuan:
    1. Jika pengguna menebak ketiga angka dengan tepat maka mendapat hadiah 
       Rp150.000.000,-
    2. Jika pengguna menebak ketiga angka tetapi dengan urutan yang berbeda 
       maka mendapat hadiah sebesar Rp30.000.000,-
    3. Jika pengguna menebak satu digit maka mendapat hadiah sebesar 
       Rp15.000.000,-
================================================================================
'''
import sys, random

# 1. Acak angka lotre
# lotre = random.randint(99, 1000)
lotre = 123

# 2. Input angka tebakan
tebakan = eval(input("Tebak angka apa yang keluar? "))

# 2a. Cek validitas input
if (tebakan < 100  or tebakan > 999) :
    print("Input tiga digit angka..!")
    sys.exit() # keluar

# 3. Ekstrak digit2 angka lotre
# 3a. Ekstrak ratusan angka lotre
lotreRatusan = lotre // 100
lotreSisa = lotre % 100

# 3b. Ekstrak puluhan angka lotre
lotrePuluhan = lotreSisa // 10
lotreSisa %= 10

# 3c. Ekstrak satuan angka lotre
lotreSatuan = lotreSisa
print("lotre ratusan : ", lotreRatusan)
print("lotre puluhan : ", lotrePuluhan)
print("lotre satuan : ", lotreSatuan)


# 4. Ekstrak digit2 angka tebakan
# 4a. Ekstrak ratusan angka tebakan
tebakanRatusan = tebakan // 100
tebakanSisa = tebakan % 100

# 4b. Ekstrak puluhan angka tebakan
tebakanPuluhan = tebakanSisa // 10
tebakanSisa %= 10

# 4c. Ekstrak satuan angka tebakan
tebakanSatuan = tebakanSisa

print("tebakan ratusan : ", tebakanRatusan)
print("tebakan puluhan : ", tebakanPuluhan)
print("tebakan satuan : ", tebakanSatuan)

# 5. Bandingkan angka lotre dengan tebakan dan tampilkan hasil
print("Nomor lotre yang keluar: ", lotre)

if (lotre == tebakan):
    print("Selamat.. Anda mendapat hadiah Rp150.000.000,-!")

elif ((lotreRatusan == tebakanPuluhan  and \
       lotrePuluhan == tebakanSatuan   and \
       lotreSatuan  == tebakanRatusan)   or \
      (lotreRatusan == tebakanSatuan   and \
       lotrePuluhan == tebakanRatusan  and \
       lotreSatuan  == tebakanPuluhan)   or \
      (lotreRatusan == tebakanRatusan  and \
       lotrePuluhan == tebakanSatuan   and \
       lotreSatuan  == tebakanPuluhan)   or \
      (lotreRatusan == tebakanPuluhan  and \
       lotrePuluhan == tebakanRatusan  and \
       lotreSatuan  == tebakanSatuan)    or \
      (lotreRatusan == tebakanSatuan   and \
       lotrePuluhan == tebakanPuluhan  and \
       lotreSatuan  == tebakanRatusan)):
    print("Selamat.. Anda mendapat hadiah Rp30.000.000,-!")

elif (lotreRatusan == tebakanRatusan or \
      lotreRatusan == tebakanPuluhan or \
      lotreRatusan == tebakanSatuan  or \
      lotrePuluhan == tebakanRatusan or \
      lotrePuluhan == tebakanPuluhan or \
      lotrePuluhan == tebakanSatuan  or \
      lotreSatuan  == tebakanRatusan or \
      lotreSatuan  == tebakanPuluhan or \
      lotreSatuan  == tebakanSatuan):
    print("Selamat.. Anda mendapat hadiah Rp15.000.000,-!")

else:
    print("Maaf.. Anda belum beruntung..!")


