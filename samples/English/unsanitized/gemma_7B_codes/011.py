from typing import List


def string_xor(a: str, b: str) -> str:
    """
    Input do strings a aur b honge jo sirf 1s aur 0s se bane honge.
    In inputs par binary XOR perform karo aur result ko bhi ek string ke roop mein return karo.
    >>> string_xor('010', '110')
    '100'
    """
    try:
        a = int(a, 2)
    except ValueError:
        return 'Error'

    try:
        b = int(b, 2)
    except ValueError:
        return 'Error'

    return format(a ^ b, 'b').zfill(len(a))


def encode_and_decode(codes: List) -> str:
    """
    This will be the string where we save all the values before returning.
    """
    message = bytes()
    for number in codes:
        try:
            message += int(number)
        except ValueError:
            return 'Cannot parse'

    encoded = int(message.hex(), 16)
    return format(encoded, 'b').zfill(256)


def decode_and_encode(codes: str) -> List:
    try:
        num = int(codes, 2)
    except ValueError:
        return 'Cannot parse string'

    decoded = bytes(num).hex().ljust(16, '0')
    return [decoded[i:i + 4] for i in range(0, len(decoded), 4)]
