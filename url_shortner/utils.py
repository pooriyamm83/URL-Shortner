import validators
import string

ALPHABET = string.digits + string.ascii_lowercase + string.ascii_uppercase  # Base62

def encode_base62(num: int) -> str:
    if num == 0:
        return ALPHABET[0]
    arr = []
    base = len(ALPHABET)
    while num:
        num, rem = divmod(num, base)
        arr.append(ALPHABET[rem])
    arr.reverse()
    return ''.join(arr)

def validate_url(url: str) -> bool:
    return validators.url(url)