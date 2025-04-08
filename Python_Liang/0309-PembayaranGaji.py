'''
    ============================================
    03.09. Pembayaran Gaji
    Oleh : #bayuyudhasaputra
    -------------------------------------------
    Buatlah program untuk pembayaran gaji
    dengan input sebagai berikut,

    Nama karyawan :
    Jam kerja per minggu :
    Gaji per jam :
    Pajak penghasilan (dalam %) :
    Pajak daerah (dalam %) :

    Dan output sebagai berikut,

    Gaji kotor :
    Nominal pajak penghasilan :
    Nominal pajak daerah :
    Gaji net :

    ===========================================

'''

# 1. Buat input
nama = input("Nama karyawan : ")
jam_kerja = eval(input("Jam kerja per minggu : "))
gaji_per_jam = eval(input("Gaji per jam : Rp "))
persen_pph = eval(input("Pajak penghasilan (dalam %) : "))
persen_pajak_daerah = eval(input("Pajak daerah (dalam persen) : "))

# 2. Hitung gaji kotor
gaji_kotor = jam_kerja * gaji_per_jam

# 3. Hitung gaji setelah PPh
pph = (persen_pph / 100) * gaji_kotor

# 4. Hitung pajak daerah
pajak_daerah = (persen_pajak_daerah / 100) * gaji_kotor

# 5. Hitung total pengurang
pengurang = pph + pajak_daerah

# 6. Hitung gaji bersih
gaji_bersih = gaji_kotor - pengurang

# 7. Tampilkan output
print("Gaji kotor : Rp",gaji_kotor, "\n",
      "Pengurang: \n",
      "\t PPh : Rp", pph, "\n",
      "\t Pajak daerah : Rp", pajak_daerah, "\n",
      "Gaji bersih : Rp", gaji_bersih, "\n"
      )


