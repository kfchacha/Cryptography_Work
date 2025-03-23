from breaker_supporting.find_letters import find_letters
#from modules.xor import xorF


first_hash = input('Input ciphertext of first message: \n')
second_hash = input('\nInput second hash: \n')

def xorF(str1, str2, amount = 166):
    str1 = str1[:amount]
    str2 = str2[:amount]

    output = ''.join(hex(int(a, 16) ^ int(b, 16))[2:] for a, b in zip(str1, str2))
   
    return output

# output = xorF(first_hash, second_hash)


hash_to_break = xorF(first_hash, second_hash)
print(hash_to_break)


def breaker(hash):
    
    sec = []
    possible_message = []

    for i, x in enumerate(hash):        # divide hash into byte fractions
        if not i % 2 == 0:
            sec.append(hash[i-1] + hash[i])

    while len(possible_message) < len(hash_to_break)/2:
        for i, byte in enumerate(sec):
            pairs = find_letters(byte)

            if len(pairs) == 1 and not byte == '00' and int(byte, 16) <= 128:
                sorted = [pairs[0].pop(pairs[0].index(x)) for x in pairs[0] if not x == ' ']  # pop() every ' ' in 'pairs'

                possible_message.append(sorted[0])
            else:
                possible_message.append(str(i+1))

    message = ' - '.join(possible_message)
    return message




broken_message = breaker(hash_to_break)

print(broken_message, '\n')