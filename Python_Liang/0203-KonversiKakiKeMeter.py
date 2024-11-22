# ====================================================
# 0203. Konversi Kaki Ke Meter
# Oleh : #bayuyudhasaputra
# ----------------------------------------------------
# Tuliskan program yang meminta input satuan dalam kaki
# kemudian dikonversi ke satuan meter jika 
# 1 kaki = 0.305 meter
# ====================================================

# Input satuan dalam kaki
kaki = eval(input("Input panjang dalam satuan kaki (Misal. 16.5) : "))

# Konversi panjang dari kaki ke meter
meter = 0.305 * kaki

# Tampilkan panjang dalam meter
print("Panjang ", kaki, " kaki sama dengan ", meter, "meter.")