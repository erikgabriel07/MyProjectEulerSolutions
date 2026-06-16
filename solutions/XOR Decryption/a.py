from string import ascii_lowercase

def score_byte(b: bytes) -> int:
    if b in [9, 10, 13]:
        return 0

    if b < 32 or b > 126:
        return -30

    c = chr(b)

    if c == ' ':
        return 8

    if c.isalpha():
        if c.lower() in 'etaoinshrdlu':
            return 5
        return 3

    if c.isdigit():
        return 1

    if c in '.,;:!?\'"()-':
        return 1

    return 0

def score_bytes(data: bytes) -> int:
    return sum(score_byte(b) for b in data)

def xor_with_byte(data: bytes, key_byte: int) -> bytes:
    return bytes(b ^ key_byte for b in data)

def split_into_columns(ciphertext: bytes, key_length: int) -> list[bytes]:
    return [ciphertext[i::key_length] for i in range(key_length)]

def find_best_char(column: bytes) -> tuple[int, str]:
    best_char = ''
    best_score = float('-inf')

    for ch in ascii_lowercase:
       key_byte = ord(ch)
       decrypted = xor_with_byte(column, key_byte)
       score = score_bytes(decrypted)

       if score > best_score:
           best_score = score
           best_char = ch

    return best_char, best_score

def recover_key(ciphertext: bytes, key_length: int) -> str:
    columns = split_into_columns(ciphertext, key_length)
    key_chars = []

    for i, column in enumerate(columns):
        ch, score = find_best_char(column)
        key_chars.append(ch)
        print(f'Posição: {i}: melhor = {ch!r}, score = {score}')

    return ''.join(key_chars)

def xor_repeating_key(data: bytes, key: str) -> bytes:
    key_bytes = key.encode('ascii')
    key_len = len(key_bytes)

    return bytes(
        b ^ key_bytes[i % key_len]
        for i, b in enumerate(data)
    )

def load_ciphertext(filename: str) -> bytes:
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    numbers = [
        int(part.strip())
        for part in content.split(',')
        if part.strip()
    ]

    for n in numbers:
        if not (0 <= n <= 255):
            raise ValueError(f'Valor inválido para byte: {n}')

    return bytes(numbers)

def solve(filepath):
    ciphertext = load_ciphertext(filepath)

    recovered_key = recover_key(ciphertext, 3)

    print(f'\nChave recuperada: {recovered_key}')

    decrypted = xor_repeating_key(ciphertext, recovered_key)

    print(f'\nTexto decifrado:\n')
    print(decrypted.decode('ascii', errors='replace'))

    ascii_sum = sum(decrypted)
    print('\nSoma dos valores ASCII:', ascii_sum)

if __name__ == '__main__':
    # the decryption key consists in three lower case characters
    solve('0059_cipher.txt')

