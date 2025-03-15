# =============================================================================================================
# Programming Exercise 01.11
# Oleh      : #bayuyudhasaputra
# Sumber    : https://media.pearsoncmg.com/bc/abp/cs-resources/products/product.html#product,isbn=0133050556
# -------------------------------------------------------------------------------------------------------------
# 01.11. Population projection
#   The US Census Bureau projects population based on the following assumptions:
#       One birth every 7 seconds
#       One death every 13 seconds
#       One new immigrant every 45 seconds
#   Write a program to display the population for each of the next five years. 
#   Assume the current population is 312032486 and one year has 365 days. 
#   Hint: in Python, you can use integer division operator // to perform division. 
#   The result is an integer. For example, 5 // 4 is 1 (not 1.25) and 10 // 4 is 2 (not 2.5).
# ==============================================================================================================

print( 
    "Total populasi 5 tahun lagi adalah ", 
    312032486 +                 # jumlah populasi semula
    ( 5 *                       # selama 5 tahun  
    ((365 * 24 * 3600) // 7) -  # jumlah kelahiran
    ((365 * 24 * 3600) // 13) + # jumlah kematian
    ((365 * 24 * 3600) // 45)   # jumlah imigran baru
    ), 
    " jiwa."
    )