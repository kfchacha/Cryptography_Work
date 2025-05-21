from Crypto.Util import Counter

def decrypt_aes_ctr(key_hex, ciphertext_hex):
    key = bytes.fromhex(key_hex)
    ciphertext = bytes.fromhex(ciphertext_hex)
    nonce = ciphertext[:16]
    encrypted = ciphertext[16:]

    
    nonce_int = int.from_bytes(nonce, byteorder='big')
    ctr = Counter.new(128, initial_value=nonce_int)
    cipher = AES.new(key, AES.MODE_CTR, counter=ctr)

    plaintext = cipher.decrypt(encrypted)
    return plaintext.decode('utf-8')


ctr_key = '36f18357be4dbd77f050515c73fcf9f2'
ctr_ct1 = '69dda8455c7dd4254bf353b773304eec0ec7702330098ce7f7520d1cbbb20fc388d1b0adb5054dbd7370849dbf0b88d393f252e764f1f5f7ad97ef79d59ce29f5f51eeca32eabedd9afa9329'
ctr_ct2 = '770b80259ec33beb2561358a9f2dc617e46218c0a53cbeca695ae45faa8952aa0e311bde9d4e01726d3184c34451'

print("CTR 1:", decrypt_aes_ctr(ctr_key, ctr_ct1))
print("CTR 2:", decrypt_aes_ctr(ctr_key, ctr_ct2))
