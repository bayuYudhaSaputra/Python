'''
====================================================
0211. Hitung Nilai Awal Investasi
Oleh : #bayuyudhasaputra
----------------------------------------------------
Tuliskan program yang meminta input nilai akhir 
tabungan (dalam rupiah), persentase bunga tahunan 
dan jangka waktu. Program menampilkan nilai 
awal tabungan.
====================================================
'''

tabungan_akhir = eval(input("Input nominal tabungan akhir Rp"))
bunga = eval(input("Input bunga (dalam %) : "))
tahun = eval(input("Input jangka waktu (dalam tahun) : "))

# bunga dikali 0.01 karena dinyatakan dalam persen (per seratus)
tabungan_awal = tabungan_akhir / ((1 + 0.01 * bunga) ** tahun)

# nilai tabungan_awal dibulatkan hingga 2 tempat desimal
tabungan_awal = round(tabungan_awal, 2)

print(
        "Nominal uang yang harus ditabung agar terkumpul dana sebesar Rp", tabungan_akhir,
        "dengan bunga", bunga, "%",
        "selama", tahun, "tahun",
        "adalah Rp", tabungan_awal
    )