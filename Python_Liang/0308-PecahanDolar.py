'''
    ===========================================
    3.7. Hitung Pecahan Dolar
    Oleh : #bayuyudhasaputra
    -------------------------------------------
    Buatlah program yang menerima input
    sejumlah uang dalam satuan dolar. Program
    mengonversinya ke dalam:
    - quarter
    - dime
    - penny
    - cent
    ===========================================
'''

# 1. Input nominal uang dalam dolar
dolar = eval(input("Input nominal uang dalam dolar : "))
dolar = dolar * 100

# 2. Hitung banyak quarter
quarter = int(dolar // 25)
sisa = dolar % 25

# 3. Hitung banyak dime
dime = int(sisa // 10)
sisa = sisa % 10

# 4. Hitung banyak nickel
nickel = int(sisa // 5)
sisa = sisa % 5

# 5. Hitung banyak sen
sen = int(sisa)

# 6. Kembalikan dolar
dolar = dolar / 100

# 7. Tampilkan hasil
print("Uang sejumlah USD.", dolar, "sama dengan \n",
      "\t", quarter, "quarter; \n",
      "\t", dime, "dime; \n",
      "\t", nickel, "nickel; \n",
      "\t", sen, "cent."
      )

