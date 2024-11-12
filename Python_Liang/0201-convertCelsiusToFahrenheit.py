# ====================================================
# 0201. Konversi Celsius ke Fahrenheit
# Oleh : #bayuyudhasaputra
# ====================================================

celsius = eval(input("Input suhu dalam satuan Celsius : "))

# Konversi celsius ke fahrenheit
fahrenheit = (9 / 5) * celsius + 32

# konversi celsius ke reamur
reamur = (4 / 5) * celsius

# Konversi celsius ke kelvin
kelvin = celsius + 273

# Tampilkan hasil konversi
print(
    "Suhu", celsius, "derajat celsius",
    "sama dengan \n", 
    "\t",fahrenheit, "derajat fahrenheit \n",
    "\t", reamur, " derajat reamur \n",
    "\t", kelvin, "kelvin. \n"
)