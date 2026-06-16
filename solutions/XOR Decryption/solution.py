from string import ascii_lowercase


def score_byte(b: int) -> int:
    """
    Atribui uma pontuação a um byte decifrado.
    Quanto maior a pontuação, mais provável que o byte faça parte
    de um texto natural.
    """
    # Permite tab, LF e CR sem penalidade
    if b in (9, 10, 13):
        return 0

    # ASCII imprimível: 32 (' ') até 126 ('~')
    if b < 32 or b > 126:
        return -30

    c = chr(b)

    # Espaço
    if c == ' ':
        return 8

    # Letras
    if c.isalpha():
        if c.lower() in 'etaoinshrdlu':
            return 5
        return 3

    # Dígitos
    if c.isdigit():
        return 1

    # Pontuação comum
    if c in '.,;:!?\'"()-':
        return 1

    # Outros caracteres imprimíveis
    return 0


def score_bytes(data: bytes) -> int:
    """
    Soma a pontuação de todos os bytes.
    """
    return sum(score_byte(b) for b in data)


def xor_with_byte(data: bytes, key_byte: int) -> bytes:
    """
    Aplica XOR entre cada byte de 'data' e 'key_byte'.
    """
    return bytes(b ^ key_byte for b in data)


def split_into_columns(ciphertext: bytes, key_length: int) -> list[bytes]:
    """
    Divide o ciphertext em colunas.
    Cada coluna contém os bytes cifrados com o mesmo byte da chave.
    """
    return [ciphertext[i::key_length] for i in range(key_length)]


def find_best_key_char(column: bytes) -> tuple[str, int]:
    """
    Testa todas as letras minúsculas ('a' a 'z') e retorna
    o caractere da chave com maior score para a coluna.
    """
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
    """
    Recupera a chave assumindo:
      - tamanho conhecido;
      - apenas letras minúsculas.
    """
    columns = split_into_columns(ciphertext, key_length)
    key_chars = []

    for i, column in enumerate(columns):
        ch, score = find_best_key_char(column)
        key_chars.append(ch)
        print(f'Posição {i}: melhor = {ch!r}, score = {score}')

    return ''.join(key_chars)


def xor_repeating_key(data: bytes, key: str) -> bytes:
    """
    Aplica XOR com chave repetida.
    Serve tanto para cifrar quanto para decifrar.
    """
    key_bytes = key.encode('ascii')
    key_len = len(key_bytes)

    return bytes(
        b ^ key_bytes[i % key_len]
        for i, b in enumerate(data)
    )


def load_ciphertext(filename: str) -> bytes:
    """
    Lê um arquivo no formato:
        38,12,23,0,...
    e converte para bytes.
    """
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read().strip()

    # Divide por vírgulas, remove espaços e ignora entradas vazias
    numbers = [
        int(part.strip())
        for part in content.split(',')
        if part.strip()
    ]

    # Validação opcional
    for n in numbers:
        if not (0 <= n <= 255):
            raise ValueError(f'Valor inválido para byte: {n}')

    return bytes(numbers)


if __name__ == '__main__':
    # Carrega o ciphertext do arquivo CSV de bytes
    ciphertext = load_ciphertext('0059_cipher.txt')

    # Recupera a chave de tamanho 3
    recovered_key = recover_key(ciphertext, 3)

    print('\nChave recuperada:', recovered_key)

    # Decifra com a chave recuperada
    decrypted = xor_repeating_key(ciphertext, recovered_key)

    print('\nTexto decifrado:\n')
    print(decrypted.decode('ascii', errors='replace'))

    # Se desejar, também pode imprimir a soma dos códigos ASCII
    ascii_sum = sum(decrypted)
    print('\nSoma dos valores ASCII:', ascii_sum)
