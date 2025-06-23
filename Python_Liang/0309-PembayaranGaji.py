'''
    ============================================================
    03.09. Pembayaran Gaji
    Oleh : #bayuyudhasaputra
    -------------------------------------------------------------
    Buatlah program untuk pembayaran gaji dengan 
    input sebagai berikut,
    Nama karyawan :
    Jam kerja per minggu :
    Gaji per jam :
    Pajak penghasilan (dalam %) :
    Pajak daerah (dalam %) :

    Contoh Program:
     Input nama karyawan : Suparno
     Input jam kerja per minggu : 48
     Input gaji per jam : Rp50000
     Input pajak penghasilan (dalam %) : 11
     Input pajak daerah (dalam %) : 9.5

    ===================================================
    Nama Karyawan : Suparno
    Jam kerja per minggu : 48
    Nominal gaji per jam : Rp50000
    Nominal gaji Kotor : Rp2400000
    Pengurang:
        Pajak penghasilan : Rp264000
        Pajak penghasilan daerah : Rp228000
    ----------------------------------------------------
    Gaji bersih : Rp1908000
    ====================================================

    ============================================================

'''

# 1. Buat input
nama = input("Input nama karyawan : ")
jam_kerja = eval(input("Input jam kerja per minggu : "))
gaji_per_jam = eval(input("Input gaji per jam : Rp"))
persen_pph = eval(input("Input pajak penghasilan (dalam %) : "))
persen_pajak_daerah = eval(input("Input pajak daerah (dalam persen) : "))

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
print(
    "==================================================", "\n",
    "Nama karyawan : ", nama, "\n",
    "Jam kerja per minggu : ", jam_kerja, "\n",
    "Nominal gaji per jam : Rp", gaji_per_jam, "\n",
    "Nominal gaji kotor : Rp", gaji_kotor, "\n",
    "Gaji kotor : Rp",gaji_kotor, "\n",
    "Pengurang: \n",
      "\t Pajak penghasilan : Rp", pph, "\n",
      "\t Pajak penghasilan daerah : Rp", pajak_daerah, "\n",
    "--------------------------------------------------", "\n",
    "Gaji bersih : Rp", gaji_bersih, "\n",
    "==================================================", "\n"
      )
