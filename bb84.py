import numpy as np

def bb84_protocol(n=32):

    alice_bits = np.random.randint(2, size=n)
    alice_bases = np.random.randint(2, size=n)
    bob_bases = np.random.randint(2, size=n)

    key = []

    for i in range(n):
        if alice_bases[i] == bob_bases[i]:
            key.append(alice_bits[i])

    return ''.join(map(str, key))