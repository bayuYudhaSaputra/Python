'''
================================================================================
Programming Exercise 04.24
Oleh      : #bayuyudhasaputra
Sumber    : https://www.amazon.com/Introduction-Programming-Using-Python-Daniel
            /dp/0132747189
--------------------------------------------------------------------------------
04.24. Simulasi Pengambilan Kartu
   Tulis program yang mensimulasikan pengambilan kartu remi yang terdiri dari 
   52 kartu. Program ini harus menampilkan rank yang terdiri dari 
   Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, dan King 
   serta suit yang terdiri dari Clubs, Diamonds, Hearts, Spades!
================================================================================
'''

import sys

# 1. Input rank
indeks_rank = int(input("Input rank: "))

# 2. Validasi rank
if indeks_rank == 1:
    rank = "Ace"

elif (2 <= indeks_rank <= 10):
    rank = str(indeks_rank)

elif indeks_rank == 11:
    rank = "Jack"

elif indeks_rank == 12:
    rank = "Queen"

elif indeks_rank == 13:
    rank = "King"

else:
    print("Error: Input angka 1 hingga 13 saja!")
    sys.exit()

# 3. Input suit
indeks_suit = int(input("Input suit: "))

# 4. Validasi suit
if indeks_suit == 1:
    suit = "Clubs"

elif indeks_suit == 2:
    suit = "Diamonds"

elif indeks_suit == 3:
    suit == "Hearts"

elif indeks_suit == 4:
    suit == "Spades"

else:
    print("Error : Input angka 1 hingga 4 saja!")
    sys.exit()

# 5. Tampilkan hasil
print(f"Kartu yang muncul adalah {rank} {suit}.")


