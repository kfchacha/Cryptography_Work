from Crypto.Cipher import AES
import binascii

def pkcs7_unpad(s):
    return s[:-s[-1]]

def decrypt_aes_cbc(key_hex, ciphertext_hex):
    key = bytes.fromhex(key_hex)
    ciphertext = bytes.fromhex(ciphertext_hex)
    iv = ciphertext[:16]
    ciphertext_blocks = [ciphertext[i:i+16] for i in range(16, len(ciphertext), 16)]

    cipher = AES.new(key, AES.MODE_ECB)  # we'll manage CBC manually
    prev = iv
    plaintext = b''

    for block in ciphertext_blocks:
        decrypted = cipher.decrypt(block)
        plaintext_block = bytes([a ^ b for a, b in zip(decrypted, prev)])
        plaintext += plaintext_block
        prev = block

    return pkcs7_unpad(plaintext).decode('utf-8')

cbc_key = '140b41b22a29beb4061bda66b6747e14'
cbc_ct1 = '4ca00ff4c898d61e1edbf1800618fb2828a226d160dad07883d04e008a7897ee2e4b7465d5290d0c0e6c6822236e1daafb94ffe0c5da05d9476be028ad7c1d81'
cbc_ct2 = '5b68629feb8606f9a6667670b75b38a5b4832d0f26e1ab7da33249de7d4afc48e713ac646ace36e872ad5fb8a512428a6e21364b0c374df45503473c5242a253'

print("CBC 1:", decrypt_aes_cbc(cbc_key, cbc_ct1))
print("CBC 2:", decrypt_aes_cbc(cbc_key, cbc_ct2))
