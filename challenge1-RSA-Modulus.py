import gmpy2
from gmpy2 import mpz, isqrt, invert


N = mpz("17976931348623159077293051907890247336179769789423065727343008115"
        "77326758055056206869853794492129829595855013875371640157101398586"
        "47833778606925583497541085196591615128057575940752635007475935288"
        "71082364994994077189561705436114947486504671101510156394068052754"
        "0071584560878577663743040086340742855278549092581")

# Ciphertext 
ciphertext = mpz("22096451867410381776306561134883418017410069787892831071731839143676135600120538004282329650473509424343946219751512256465839967942889460764542040581564748988013734864120452325229320176487916666402997509188729971690526083222067771600019329260870009579993724077458967773697817571267229951148662959627934791540")

# Exponent
e = mpz(65537)

# Fermat's factorization
def fermat_factor(n):
    a = isqrt(n)
    if a * a < n:
        a += 1
    b2 = a * a - n
    while not gmpy2.is_square(b2):
        a += 1
        b2 = a * a - n
    b = isqrt(b2)
    return a - b, a + b

# Factor N
p, q = fermat_factor(N)

# Private exponent d
phi = (p - 1) * (q - 1)
d = invert(e, phi)

# Decrypting the ciphertext
m = pow(ciphertext, d, N)

# Convert to hex and extract plaintext
m_hex = hex(m)[2:]
m_hex = m_hex.zfill(len(m_hex) + len(m_hex) % 2)
m_bytes = bytes.fromhex(m_hex)


sep_index = m_bytes.find(b'\x00', 2)
plaintext = m_bytes[sep_index + 1:]

# Print result
print("Decrypted message:", plaintext.decode())
