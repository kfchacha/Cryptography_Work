import gmpy2
from gmpy2 import mpz, isqrt, is_square

N = mpz("6484558428080716696628242653467722787263437207069762630604390703787"
         "9730861808111646271401527606141756919558732184025452065542490671989"
         "2428844841839353281972988531310511738648965962582821502504990264452"
         "1008852816733037111422964210278402893076574586452336833570778346897"
         "15838646088239640236866252211790085787877")

def fermat_factor(n):
    a = isqrt(n) + 1
    while True:
        b2 = a*a - n
        if is_square(b2):
            b = isqrt(b2)
            return a - b, a + b
        a += 1

p, q = fermat_factor(N)

print("Challenge 2 Factors:")
print("p =", p)
print("q =", q)
print("Verification p*q == N:", p * q == N)
