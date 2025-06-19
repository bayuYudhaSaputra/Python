'''
    ===========================================
    3.8. Hitung Pecahan Dolar
    Oleh : #bayuyudhasaputra
    -------------------------------------------
    Buatlah program yang menerima input sejumlah 
    uang dalam satuan dolar Amerika Serikat (USD). 
    Program mengonversi nominal uang ini ke dalam
    beberapa:
        lembar uang 1 dolaran;
        koin quarter;
        koin dime;
        koin nickel;
        koin penny.
    ===========================================
'''

# 1. Input nominal uang dalam USD
jumlah = eval(input("Input sejumlah uang dalam USD : USD."))

# 2. Konversi uang dalam USD ini ke dalam cent
cent = int(jumlah * 100)

# 3. Konversi cent ke dalam beberapa lembar 1 dolaran
satu_dolaran = cent // 100

# 4. Tentukan sisa pembagian
sisa = cent % 100

# 5. Konversi ke dalam beberapa quarter
quarter = sisa // 25

# 6. Perbarui sisa
sisa = sisa % 25

# 7. Konversi ke dalam beberapa dime
dime = sisa // 10

# 7. Perbarui sisa
sisa = sisa % 10

# 8. Konversi ke dalam beberapa nickel
nickel = sisa // 5

# 9. Perbarui sisa
sisa = sisa % 5

# 10. Konversi ke penny
penny = sisa

# Tampilkan hasil konversi
print("Uang sebesar USD", jumlah, "dapat dinyatakan dalam:", "\n",
      "\t", satu_dolaran, "lembar uang 1 dolaran;", "\n",
      "\t", quarter, "koin uang quarter;", "\n",
      "\t", dime, "koin uang dime;", "\n",
      "\t", nickel, "koin uang nickel;", "\n",
      "\t", penny, "koin uang penny.", "\n"
      )


